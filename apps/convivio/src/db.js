// Camada de acesso ao banco (SQLite via better-sqlite3).
// As consultas usam sempre parâmetros vinculados (prepared statements),
// o que elimina injeção de SQL. Nada de concatenar entrada do usuário.

import Database from 'better-sqlite3';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { mkdirSync } from 'node:fs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const dataDir = join(__dirname, '..', 'data');
mkdirSync(dataDir, { recursive: true });

const db = new Database(join(dataDir, 'convivio.sqlite'));
db.pragma('journal_mode = WAL');
db.pragma('foreign_keys = ON');

// Estrutura das tabelas.
// - password_hash guarda apenas o hash bcrypt, jamais a senha em texto.
// - sessions dá persistência às sessões do express-session.
db.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    email         TEXT NOT NULL UNIQUE,
    display_name  TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    created_at    TEXT NOT NULL DEFAULT (datetime('now'))
  );

  CREATE TABLE IF NOT EXISTS sessions (
    sid        TEXT PRIMARY KEY,
    data       TEXT NOT NULL,
    expires_at INTEGER NOT NULL
  );
`);

// e-mails são comparados sempre em minúsculas e sem espaços nas pontas.
export function normalizeEmail(email) {
  return String(email || '').trim().toLowerCase();
}

export function findUserByEmail(email) {
  return db
    .prepare('SELECT id, email, display_name, password_hash FROM users WHERE email = ?')
    .get(normalizeEmail(email));
}

export function createUser({ email, displayName, passwordHash }) {
  const info = db
    .prepare(
      'INSERT INTO users (email, display_name, password_hash) VALUES (?, ?, ?)'
    )
    .run(normalizeEmail(email), displayName, passwordHash);
  return info.lastInsertRowid;
}

export function countUsers() {
  return db.prepare('SELECT COUNT(*) AS n FROM users').get().n;
}

export default db;
