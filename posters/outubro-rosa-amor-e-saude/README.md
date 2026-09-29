# Pôster Outubro Rosa — Amor e Saúde clínica

- `poster-outubro-rosa.png` — versão final em alta (2160×2700, formato 4:5 do feed do Instagram).
- `poster-outubro-rosa.jpg` — mesma arte, arquivo menor para enviar por WhatsApp.
- `poster-outubro-rosa-cartoon.png` / `.jpg` — mesma arte com o rosto em estilo cartoon.
- `fonte/` — arquivos editáveis (HTML + imagens + fontes).

Para gerar a imagem de novo depois de editar `fonte/poster.html`:

```
node fonte/render.js fonte/poster.html poster-outubro-rosa.png 2
```

Versão cartoon (`fonte/pessoa-cartoon.png` é gerada a partir da foto e do recorte):

```
python3 fonte/cartoon.py fonte/foto.jpg fonte/pessoa.png fonte/pessoa-cartoon.png 5 0.55 90
node fonte/render.js fonte/poster-cartoon.html poster-outubro-rosa-cartoon.png 2
```
