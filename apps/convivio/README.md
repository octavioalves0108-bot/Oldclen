# SkyTikTok — autenticação segura (exemplo completo)

Página de login com **design original**, inspirada em interfaces modernas de
rede social, mas **sem copiar nenhuma plataforma específica**. Traz front-end,
back-end e banco de dados, com autenticação legítima e boas práticas de
segurança.

> **Privacidade:** o sistema apenas autentica o usuário localmente contra o
> banco. **Nenhuma credencial é enviada, registrada ou encaminhada** a e-mail
> ou a qualquer outro destinatário/terceiro.

## O que tem aqui

| Item | Onde |
|------|------|
| Estrutura HTML completa | `public/index.html` |
| CSS responsivo (tema claro/escuro) | `public/styles.css` |
| Validação e envio no cliente | `public/app.js` |
| Back-end de login seguro | `src/server.js` |
| Banco de dados (SQLite) + consultas parametrizadas | `src/db.js` |
| Sessões persistidas no servidor | `src/session-store.js` |
| Criação de usuário com senha em hash | `src/seed.js` |

## Como rodar

Requisitos: Node.js 18+ (testado no 22).

```bash
cd apps/convivio
npm install
cp .env.example .env          # defina um SESSION_SECRET forte
npm run seed                  # cria o usuário de teste
npm start                     # sobe em http://localhost:3000
```

Credenciais de teste criadas pelo seed:

- **e-mail:** `demo@skytiktok.app`
- **senha:** `SkyTikTokDemo123`

Crie outros usuários assim (a senha vira hash na hora, não fica em texto):

```bash
node src/seed.js ana@exemplo.com "Ana Souza" "umaSenhaForte123"
```

## Boas práticas de segurança aplicadas

- **Senhas com hash bcrypt** (custo 12). O banco guarda só o hash; a senha em
  texto nunca é armazenada nem registrada.
- **Comparação em tempo constante** (`bcrypt.compare`) e um hash-isca quando o
  e-mail não existe, para o tempo de resposta não revelar contas válidas.
- **Mensagem de erro genérica** ("e-mail ou senha inválidos") — evita
  enumeração de usuários.
- **Consultas parametrizadas** (prepared statements) — sem injeção de SQL.
- **Rate limiting** no login (10 tentativas por IP a cada 15 min) contra força
  bruta.
- **Sessão no servidor**: o cookie só carrega o id assinado (`HttpOnly`,
  `SameSite=Lax`, `Secure` em produção). Nenhum dado sensível vai para o
  navegador.
- **Regeneração da sessão** no login, contra fixação de sessão.
- **Cabeçalhos de segurança** via Helmet: CSP restritiva, `X-Content-Type-Options`,
  anti-clickjacking (`frame-ancestors 'none'`), HSTS.
- **Validação dupla**: no cliente (experiência) e no servidor (a que vale).
- **Sem vazamento em logs**: e-mail e senha não são escritos em log algum.

## Para produção — leia antes de publicar

- Sirva **sempre por HTTPS** e defina `NODE_ENV=production` (ativa o cookie
  `Secure`) e um `SESSION_SECRET` forte e secreto.
- Considere **verificação de e-mail**, **2FA** e uma política de senhas (o
  exemplo exige apenas 8+ caracteres).
- Para escala, troque o SQLite por um banco gerenciado (PostgreSQL, etc.) e o
  store de sessão por Redis.
- Adicione um **token CSRF** dedicado se for aceitar formulários de outras
  origens (aqui o `SameSite=Lax` + API same-origin já cobre o caso comum).
- Revise o rate limit e adicione monitoramento de tentativas suspeitas.
