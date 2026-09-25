/**
 * ALMOX CENTRAL — servidor na sua conta Google (Google Apps Script)
 *
 * Instalação (uma vez só, uns 5 minutos):
 *  1. Crie uma planilha em https://sheets.new e dê o nome "Almox Central".
 *  2. No menu da planilha: Extensões > Apps Script.
 *  3. Apague o que estiver em Código.gs e cole ESTE arquivo inteiro.
 *  4. Clique no "+" ao lado de Arquivos > HTML, dê o nome Index (sem .html)
 *     e cole o conteúdo inteiro do arquivo almox-central.html.
 *  5. Salve (Ctrl+S). Clique em Implantar > Nova implantação > engrenagem > App da Web.
 *     Executar como: Eu. Quem pode acessar: Qualquer pessoa. Clique em Implantar e autorize.
 *  6. Copie o URL do app da Web e envie para a equipe. Esse é o endereço do sistema.
 *
 * Os dados ficam nesta planilha, uma aba por tipo de registro.
 * Para publicar uma versão nova do sistema depois:
 *   Implantar > Gerenciar implantações > lápis > Versão: Nova versão > Implantar.
 */

// Opcional: preencha com um código (ex.: 'almox2026') para exigir esse código
// no primeiro acesso de cada aparelho. Deixe vazio para acesso livre pelo link.
const SENHA_EQUIPE = '';

const COLECOES = ['materiais', 'movs', 'modems', 'config', 'arquivo'];
const SINCRONIZADAS = ['materiais', 'movs', 'modems', 'config'];

function doGet() {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('Almox Central')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, viewport-fit=cover');
}

function checar_(token) {
  if (SENHA_EQUIPE && String(token || '') !== String(SENHA_EQUIPE)) throw new Error('SENHA_INVALIDA');
}

function planilha_() {
  const ativa = SpreadsheetApp.getActiveSpreadsheet();
  if (ativa) return ativa;
  const props = PropertiesService.getScriptProperties();
  const id = props.getProperty('PLANILHA_ID');
  if (id) return SpreadsheetApp.openById(id);
  const nova = SpreadsheetApp.create('Almox Central — dados');
  props.setProperty('PLANILHA_ID', nova.getId());
  return nova;
}

function aba_(ss, nome) {
  let sh = ss.getSheetByName(nome);
  if (!sh) {
    sh = ss.insertSheet(nome);
    sh.getRange(1, 1, 1, 3).setValues([['id', 'atualizado_em', 'dados']]).setFontWeight('bold');
    sh.setFrozenRows(1);
    sh.setColumnWidth(3, 700);
  }
  return sh;
}

function linhas_(sh) {
  const n = sh.getLastRow();
  return n < 2 ? [] : sh.getRange(2, 1, n - 1, 3).getValues();
}

function lerColecao_(ss, nome) {
  const out = [];
  linhas_(aba_(ss, nome)).forEach(function (r) {
    if (r[0] === '' || r[2] === '') return;
    try {
      const o = JSON.parse(r[2]);
      o._id = String(r[0]);
      out.push(o);
    } catch (e) { /* linha editada à mão com JSON inválido: ignora */ }
  });
  return out;
}

function mesclar_(alvo, fonte) {
  Object.keys(fonte).forEach(function (k) {
    const v = fonte[k];
    if (v && typeof v === 'object' && !Array.isArray(v) && alvo[k] && typeof alvo[k] === 'object' && !Array.isArray(alvo[k])) mesclar_(alvo[k], v);
    else alvo[k] = v;
  });
}

// Número de versão dos dados. Fica no cache para não gastar a cota diária de Propriedades.
function versao_() {
  const cache = CacheService.getScriptCache();
  const v = cache.get('VER');
  if (v !== null) return Number(v);
  const p = Number(PropertiesService.getScriptProperties().getProperty('VER') || 0);
  cache.put('VER', String(p), 21600);
  return p;
}

function subirVersao_() {
  const props = PropertiesService.getScriptProperties();
  const v = Number(props.getProperty('VER') || 0) + 1;
  props.setProperty('VER', String(v));
  CacheService.getScriptCache().put('VER', String(v), 21600);
  return v;
}

// Nome de cada aparelho (quem registrou cada lançamento).
function nomes_() {
  const cache = CacheService.getScriptCache();
  const c = cache.get('NOMES');
  if (c !== null) return JSON.parse(c);
  const p = PropertiesService.getScriptProperties().getProperty('NOMES') || '{}';
  cache.put('NOMES', p, 21600);
  return JSON.parse(p);
}

// Quem está com o sistema aberto agora (últimos 45 segundos).
function presenca_(req) {
  const cache = CacheService.getScriptCache();
  let mapa = {};
  try { mapa = JSON.parse(cache.get('ONLINE') || '{}'); } catch (e) { mapa = {}; }
  const agora = Date.now();
  if (req.dev) mapa[String(req.dev).slice(0, 40)] = { n: String(req.nome || '').slice(0, 60), v: String(req.view || '').slice(0, 20), t: agora };
  Object.keys(mapa).forEach(function (k) { if (agora - mapa[k].t > 45000) delete mapa[k]; });
  cache.put('ONLINE', JSON.stringify(mapa), 120);
  return Object.keys(mapa).map(function (k) { return { dev: k, n: mapa[k].n, v: mapa[k].v }; });
}

// Chamado pelo sistema a cada poucos segundos. Só devolve os dados quando algo mudou.
function almoxSync(req) {
  req = req || {};
  checar_(req.token);
  const ver = versao_();
  const out = { ver: ver, online: presenca_(req), nomes: nomes_() };
  const nome = String(req.nome || '').slice(0, 60);
  if (req.dev && nome && out.nomes[req.dev] !== nome) {
    out.nomes[req.dev] = nome;
    const s = JSON.stringify(out.nomes);
    if (s.length < 8500) {
      PropertiesService.getScriptProperties().setProperty('NOMES', s);
      CacheService.getScriptCache().put('NOMES', s, 21600);
    }
  }
  if (req.ver !== ver) {
    const ss = planilha_();
    out.data = {};
    SINCRONIZADAS.forEach(function (c) { out.data[c] = lerColecao_(ss, c); });
    out.planilha = ss.getUrl();
    out.url = ScriptApp.getService().getUrl();
  }
  return out;
}

// Grava um lote de alterações: [{op: 'set'|'update'|'del', path: 'colecao/id', data: {...}}]
function almoxCommit(ops, token) {
  checar_(token);
  if (!Array.isArray(ops) || !ops.length) return { ver: versao_() };
  ops.forEach(function (op) {
    const p = String((op && op.path) || '').split('/');
    if (p.length !== 2 || COLECOES.indexOf(p[0]) < 0 || !p[1]) throw new Error('Caminho inválido: ' + (op && op.path));
    if (['set', 'update', 'del'].indexOf(op.op) < 0) throw new Error('Operação inválida: ' + op.op);
  });
  const lock = LockService.getScriptLock();
  lock.waitLock(28000);
  let mudou = false;
  try {
    const ss = planilha_();
    const agora = Date.now();
    const abas = {};
    const aba = function (c) {
      if (!abas[c]) {
        const sh = aba_(ss, c);
        const mapa = {};
        linhas_(sh).forEach(function (r, i) { if (r[0] !== '') mapa[String(r[0])] = { row: i + 2, json: String(r[2] || '') }; });
        abas[c] = { sh: sh, mapa: mapa, novas: [], apagar: [] };
      }
      return abas[c];
    };
    ops.forEach(function (op) {
      const p = String(op.path).split('/');
      const t = aba(p[0]);
      const id = p[1];
      const atual = t.mapa[id];
      if (op.op === 'del') {
        if (atual && !atual.apagado) {
          atual.apagado = true;
          if (atual.nova != null) t.novas[atual.nova] = null; else t.apagar.push(atual.row);
          mudou = true;
        }
        return;
      }
      let obj;
      if (op.op === 'set') obj = op.data || {};
      else {
        if (!atual || atual.apagado) return;
        obj = JSON.parse(atual.json || '{}');
        mesclar_(obj, op.data || {});
      }
      const json = JSON.stringify(obj);
      if (json.length > 49000) throw new Error('Registro grande demais para uma célula da planilha');
      if (atual && !atual.apagado) {
        atual.json = json;
        if (atual.nova != null) t.novas[atual.nova][2] = json;
        else t.sh.getRange(atual.row, 2, 1, 2).setValues([[agora, json]]);
      } else {
        t.novas.push(["'" + id, agora, json]);
        t.mapa[id] = { nova: t.novas.length - 1, json: json };
      }
      mudou = true;
    });
    Object.keys(abas).forEach(function (c) {
      const t = abas[c];
      const novas = t.novas.filter(function (r) { return r; });
      if (t.apagar.length > 5) {
        // Muitas exclusões: reescreve a aba de uma vez (bem mais rápido que apagar linha a linha).
        const del = {};
        t.apagar.forEach(function (r) { del[r] = true; });
        const manter = linhas_(t.sh)
          .filter(function (r, i) { return !del[i + 2] && r[0] !== ''; })
          .map(function (r) { return ["'" + String(r[0]), r[1], r[2]]; });
        const todas = manter.concat(novas);
        const ultima = t.sh.getLastRow();
        if (ultima > 1) t.sh.getRange(2, 1, ultima - 1, 3).clearContent();
        if (todas.length) t.sh.getRange(2, 1, todas.length, 3).setValues(todas);
      } else {
        if (novas.length) t.sh.getRange(t.sh.getLastRow() + 1, 1, novas.length, 3).setValues(novas);
        t.apagar.sort(function (a, b) { return b - a; }).forEach(function (row) { t.sh.deleteRow(row); });
      }
    });
  } finally {
    if (mudou) {
      SpreadsheetApp.flush();
      subirVersao_();
    }
    lock.releaseLock();
  }
  return { ver: versao_() };
}

// Lê uma coleção inteira sob demanda (usado para o histórico arquivado).
function almoxGet(nome, token) {
  checar_(token);
  if (COLECOES.indexOf(nome) < 0) throw new Error('Coleção inválida');
  return lerColecao_(planilha_(), nome);
}

// Evita que duas pessoas arquivem o histórico ao mesmo tempo.
function almoxLease(chave, dono, token) {
  checar_(token);
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const cache = CacheService.getScriptCache();
    const k = 'LEASE_' + String(chave).replace(/[^A-Za-z0-9_]/g, '_');
    const atual = cache.get(k);
    if (atual && atual !== String(dono)) return false;
    cache.put(k, String(dono), 180);
    return true;
  } finally {
    lock.releaseLock();
  }
}

// Escreve um relatório legível numa aba da planilha ("Relatório Estoque", etc.).
function almoxRelatorio(nome, linhas, token) {
  checar_(token);
  const ss = planilha_();
  const titulo = 'Relatório ' + String(nome).slice(0, 40);
  let sh = ss.getSheetByName(titulo);
  if (!sh) sh = ss.insertSheet(titulo); else sh.clear();
  if (Array.isArray(linhas) && linhas.length) {
    const largura = linhas[0].length;
    const valores = linhas.map(function (r) {
      const linha = [];
      for (let i = 0; i < largura; i++) {
        const v = r[i];
        if (v === null || v === undefined) linha.push('');
        else if (typeof v === 'string' && /^[=+\-@0-9]/.test(v)) linha.push("'" + v);
        else linha.push(v);
      }
      return linha;
    });
    sh.getRange(1, 1, valores.length, largura).setValues(valores);
    sh.getRange(1, 1, 1, largura).setFontWeight('bold').setBackground('#FFC21A');
    sh.setFrozenRows(1);
    sh.autoResizeColumns(1, largura);
  }
  return { url: ss.getUrl() + '#gid=' + sh.getSheetId() };
}
