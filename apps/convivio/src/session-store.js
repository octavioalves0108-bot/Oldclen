// Armazenamento de sessão do express-session usando o mesmo banco SQLite.
// Mantém as sessões no servidor (o cookie carrega apenas o id assinado),
// então nenhum dado sensível trafega ou fica guardado no navegador.

import session from 'express-session';
import db from './db.js';

const Store = session.Store;

export default class SqliteStore extends Store {
  constructor() {
    super();
    this.stmts = {
      get: db.prepare('SELECT data, expires_at FROM sessions WHERE sid = ?'),
      upsert: db.prepare(
        `INSERT INTO sessions (sid, data, expires_at) VALUES (@sid, @data, @expires_at)
         ON CONFLICT(sid) DO UPDATE SET data = @data, expires_at = @expires_at`
      ),
      destroy: db.prepare('DELETE FROM sessions WHERE sid = ?'),
      touch: db.prepare('UPDATE sessions SET expires_at = ? WHERE sid = ?'),
      clearExpired: db.prepare('DELETE FROM sessions WHERE expires_at < ?'),
    };
    // Limpa sessões expiradas periodicamente.
    this.cleanup = setInterval(() => {
      try {
        this.stmts.clearExpired.run(Date.now());
      } catch {
        /* ignora falhas de limpeza */
      }
    }, 60 * 60 * 1000);
    this.cleanup.unref?.();
  }

  #expiry(sess) {
    const maxAge = sess?.cookie?.maxAge;
    return Date.now() + (Number.isFinite(maxAge) ? maxAge : 24 * 60 * 60 * 1000);
  }

  get(sid, cb) {
    try {
      const row = this.stmts.get.get(sid);
      if (!row) return cb(null, null);
      if (row.expires_at < Date.now()) {
        this.stmts.destroy.run(sid);
        return cb(null, null);
      }
      return cb(null, JSON.parse(row.data));
    } catch (err) {
      return cb(err);
    }
  }

  set(sid, sess, cb) {
    try {
      this.stmts.upsert.run({
        sid,
        data: JSON.stringify(sess),
        expires_at: this.#expiry(sess),
      });
      return cb?.(null);
    } catch (err) {
      return cb?.(err);
    }
  }

  destroy(sid, cb) {
    try {
      this.stmts.destroy.run(sid);
      return cb?.(null);
    } catch (err) {
      return cb?.(err);
    }
  }

  touch(sid, sess, cb) {
    try {
      this.stmts.touch.run(this.#expiry(sess), sid);
      return cb?.(null);
    } catch (err) {
      return cb?.(err);
    }
  }
}
