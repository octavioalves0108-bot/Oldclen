"""Embute as fotos da vitrine dentro do index.html.

A página referencia as fotos pelo nome do arquivo (campo `foto` em
PRODUTOS). Aberto sozinho — baixado, anexado numa mensagem, enviado por
WhatsApp — o index.html não acha os .jpg ao lado dele e os cards voltam
para a ilustração. Este script copia cada foto citada em PRODUTOS para
dentro da página, entre os marcadores FOTOS:INICIO e FOTOS:FIM, e a
página passa a funcionar como um arquivo único.

Rode de novo sempre que trocar ou adicionar uma foto:

    python3 embutir-fotos.py
"""
import base64
import json
import pathlib
import re

PASTA = pathlib.Path(__file__).resolve().parent
PAGINA = PASTA / "index.html"
INICIO, FIM = "<!-- FOTOS:INICIO -->", "<!-- FOTOS:FIM -->"
TIPOS = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}

html = PAGINA.read_text(encoding="utf-8")
config = html[html.index("const PRODUTOS = ["):]
config = config[: config.index("];")]
citadas = sorted(set(re.findall(r'foto:\s*"([^"]+)"', config)))

fotos, faltando = {}, []
for nome in citadas:
    arquivo = PASTA / nome
    tipo = TIPOS.get(arquivo.suffix.lower())
    if not tipo or not arquivo.is_file():
        faltando.append(nome)
        continue
    fotos[nome] = f"data:{tipo};base64," + base64.b64encode(arquivo.read_bytes()).decode()

bloco = (
    f"{INICIO}\n<script>\n"
    "/* Fotos da vitrine embutidas na página — geradas por embutir-fotos.py\n"
    "   a partir dos arquivos desta pasta. Não edite à mão. */\n"
    f"const FOTOS_EMBUTIDAS = {json.dumps(fotos, indent=1)};\n"
    f"</script>\n{FIM}"
)
if INICIO in html:
    html = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIM), lambda _: bloco, html, flags=re.S)
else:
    ancora = "<script>\n/* ====================================================================="
    html = html.replace(ancora, bloco + "\n" + ancora, 1)
PAGINA.write_text(html, encoding="utf-8")

print(f"{len(fotos)} foto(s) embutida(s): {', '.join(fotos) or '—'}")
if faltando:
    print(f"não encontradas (o card mostra a ilustração ou busca o arquivo): {', '.join(faltando)}")
