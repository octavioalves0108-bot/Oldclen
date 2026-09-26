# Vídeo de apresentação — Casa Container

Vídeo gerado a partir das 5 fotos em `fotos/`, com movimento de câmera suave,
legendas animadas, transições e trilha sonora própria (sintetizada, sem direitos autorais).

| Arquivo | Formato | Uso indicado |
|---|---|---|
| `saida/apresentacao-horizontal.mp4` | 1920×1080 (16:9) | YouTube, site, anúncio do imóvel, TV |
| `saida/apresentacao-vertical.mp4` | 1080×1920 (9:16) | Reels, Stories, TikTok, status do WhatsApp |
| `saida/*-capa.jpg` | imagem | Capa/miniatura do vídeo |

## Roteiro (~47 s)

1. Abertura — fachada à noite, "Bem-vindo à Casa Container"
2. Área externa — deck e terraço
3. Área externa — jardim iluminado
4. Sala — ambiente integrado com acesso ao deck
5. Cozinha equipada
6. Quarto aconchegante
7. Banheiro com cabine de hidromassagem
8. Mosaico — "Moderna. Aconchegante. Completa."
9. Encerramento — "Venha conhecer"

## Como alterar textos e gerar de novo

Os textos ficam no topo de `gerar_video.py` (`NOME` e `TEXTOS`).
Troque pelo nome real do imóvel, cidade, WhatsApp etc. e rode:

```bash
pip install Pillow numpy imageio-ffmpeg
python3 gerar_video.py                  # gera os dois formatos
python3 gerar_video.py --formato v      # só o vertical
python3 gerar_video.py --previa 3,20    # salva quadros de prévia (PNG) para conferir
```

Fontes: Playfair Display e Montserrat (Google Fonts, licença OFL) em `fontes/`.
