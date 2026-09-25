// Cria/atualiza um usuário no banco com a senha já convertida em hash bcrypt.
//
// Uso:
//   node src/seed.js                       -> cria o usuário de teste padrão
//   node src/seed.js ana@ex.com "Ana" senhaForte123
//
// A senha é lida do argumento e transformada em hash na hora; o texto puro
// não é gravado nem exibido. Em uso real, prefira passar por variável de
// ambiente ou prompt para não deixar a senha no histórico do shell.

import 'dotenv/config';
import bcrypt from 'bcryptjs';
import { createUser, findUserByEmail, normalizeEmail, countUsers } from './db.js';
import db from './db.js';

const COST = 12; // fator de custo do bcrypt (bom equilíbrio em 2026)

const [, , argEmail, argName, argPassword] = process.argv;

const email = normalizeEmail(argEmail || 'demo@convivio.app');
const displayName = argName || 'Usuário Demo';
const password = argPassword || 'ConvivioDemo123';

async function main() {
  const passwordHash = await bcrypt.hash(password, COST);
  const existing = findUserByEmail(email);

  if (existing) {
    db.prepare('UPDATE users SET display_name = ?, password_hash = ? WHERE email = ?')
      .run(displayName, passwordHash, email);
    console.log(`Usuário atualizado: ${email}`);
  } else {
    createUser({ email, displayName, passwordHash });
    console.log(`Usuário criado: ${email}`);
  }

  if (!argPassword) {
    console.log('\nCredenciais de teste (troque em produção):');
    console.log(`  e-mail: ${email}`);
    console.log(`  senha:  ${password}`);
  }
  console.log(`\nTotal de usuários no banco: ${countUsers()}`);
}

main().catch((err) => {
  console.error('Falha ao semear usuário:', err.message);
  process.exit(1);
});
