// Servidor de autenticação do Convívio.
//
// Princípios de segurança aplicados aqui:
//  - Senhas nunca são guardadas em texto: só o hash bcrypt fica no banco.
//  - Comparação de senha com bcrypt.compare (tempo constante contra timing).
//  - Consultas parametrizadas no db.js -> sem injeção de SQL.
//  - Mensagem de erro genérica ("e-mail ou senha inválidos") para não revelar
//    se um e-mail existe (evita enumeração de usuários).
//  - Rate limiting nas rotas de login para frear força bruta.
//  - Sessão no servidor; o cookie é httpOnly, sameSite=lax e Secure em produção.
//  - Regeneração da sessão no login (evita fixação de sessão).
//  - helmet para cabeçalhos de segurança; body limitado; sem log de credenciais.
//  - NENHUMA credencial é enviada, encaminhada ou registrada para terceiros
//    (nem por e-mail, nem por webhook, nem em arquivo de log). O sistema apenas
//    autentica localmente contra o banco.

import 'dotenv/config';
import express from 'express';
import helmet from 'helmet';
import session from 'express-session';
import rateLimit from 'express-rate-limit';
import bcrypt from 'bcryptjs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import crypto from 'node:crypto';

import { findUserByEmail, normalizeEmail } from './db.js';
import SqliteStore from './session-store.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const app = express();
const isProd = process.env.NODE_ENV === 'production';

app.set('trust proxy', 1); // necessário para cookie Secure atrás de proxy/HTTPS

// ---- Cabeçalhos de segurança ------------------------------------------------
app.use(
  helmet({
    contentSecurityPolicy: {
      useDefaults: true,
      directives: {
        'default-src': ["'self'"],
        'style-src': ["'self'"],
        'script-src': ["'self'"],
        'img-src': ["'self'", 'data:'],
        'form-action': ["'self'"],
        'frame-ancestors': ["'none'"], // impede que a página seja embutida (clickjacking)
        'base-uri': ["'self'"],
      },
    },
    referrerPolicy: { policy: 'same-origin' },
  })
);

app.use(express.json({ limit: '10kb' })); // corpo pequeno: só e-mail e senha

// ---- Sessão -----------------------------------------------------------------
if (!process.env.SESSION_SECRET && isProd) {
  console.error('SESSION_SECRET é obrigatório em produção. Abortando.');
  process.exit(1);
}

app.use(
  session({
    name: 'convivio.sid',
    store: new SqliteStore(),
    secret: process.env.SESSION_SECRET || crypto.randomBytes(32).toString('hex'),
    resave: false,
    saveUninitialized: false,
    rolling: true,
    cookie: {
      httpOnly: true, // JS do navegador não lê o cookie
      sameSite: 'lax', // mitiga CSRF em navegações entre sites
      secure: isProd, // só trafega por HTTPS em produção
      maxAge: 1000 * 60 * 60 * 24, // 24h
    },
  })
);

// ---- Limite de tentativas de login -----------------------------------------
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutos
  max: 10, // no máximo 10 tentativas por IP na janela
  standardHeaders: true,
  legacyHeaders: false,
  message: {
    ok: false,
    error: 'Muitas tentativas. Tente novamente em alguns minutos.',
  },
});

// ---- Validação de entrada ---------------------------------------------------
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function validateCredentials(body) {
  const email = normalizeEmail(body?.email);
  const password = typeof body?.password === 'string' ? body.password : '';
  const errors = {};
  if (!EMAIL_RE.test(email) || email.length > 254) {
    errors.email = 'Informe um e-mail válido.';
  }
  if (password.length < 8 || password.length > 200) {
    errors.password = 'A senha deve ter entre 8 e 200 caracteres.';
  }
  return { email, password, errors };
}

// ---- Rotas ------------------------------------------------------------------

// Estado atual da sessão (para o front saber se já está logado).
app.get('/api/me', (req, res) => {
  if (req.session.user) {
    return res.json({ ok: true, user: req.session.user });
  }
  return res.status(401).json({ ok: false });
});

app.post('/api/login', loginLimiter, async (req, res) => {
  const { email, password, errors } = validateCredentials(req.body);

  if (Object.keys(errors).length > 0) {
    return res.status(400).json({ ok: false, fields: errors });
  }

  try {
    const user = findUserByEmail(email);

    // Comparação sempre executada, mesmo sem usuário, com um hash-isca,
    // para o tempo de resposta não denunciar se o e-mail existe.
    const DUMMY_HASH = '$2a$12$C6UzMDM.H6dfI/f/IKcEeO5tZ0V6Vf5tW0z3n0cE0wS1yqQ2q3q3q';
    const hash = user ? user.password_hash : DUMMY_HASH;
    const passwordOk = await bcrypt.compare(password, hash);

    if (!user || !passwordOk) {
      // Mensagem única, sem dizer qual campo falhou (anti-enumeração).
      return res
        .status(401)
        .json({ ok: false, error: 'E-mail ou senha inválidos.' });
    }

    // Regenera a sessão para evitar fixação e só então grava o usuário.
    req.session.regenerate((err) => {
      if (err) {
        return res
          .status(500)
          .json({ ok: false, error: 'Não foi possível iniciar a sessão.' });
      }
      req.session.user = {
        id: user.id,
        email: user.email,
        displayName: user.display_name,
      };
      req.session.save((saveErr) => {
        if (saveErr) {
          return res
            .status(500)
            .json({ ok: false, error: 'Não foi possível iniciar a sessão.' });
        }
        return res.json({
          ok: true,
          message: `Bem-vindo(a) de volta, ${user.display_name}!`,
          user: req.session.user,
        });
      });
    });
  } catch {
    // Não registramos e-mail nem senha em log algum.
    return res
      .status(500)
      .json({ ok: false, error: 'Erro inesperado. Tente novamente.' });
  }
});

app.post('/api/logout', (req, res) => {
  req.session.destroy(() => {
    res.clearCookie('convivio.sid');
    res.json({ ok: true });
  });
});

// ---- Arquivos estáticos (front-end) ----------------------------------------
app.use(
  express.static(join(__dirname, '..', 'public'), {
    extensions: ['html'],
  })
);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Convívio rodando em http://localhost:${PORT}`);
  if (!isProd) {
    console.log('Modo desenvolvimento. Rode "npm run seed" para criar o usuário de teste.');
  }
});
