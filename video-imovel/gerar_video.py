#!/usr/bin/env python3
"""Gera o vídeo de apresentação do imóvel a partir das fotos em ./fotos.

Uso:
    python3 gerar_video.py                  # horizontal (16:9) e vertical (9:16)
    python3 gerar_video.py --formato h      # só horizontal
    python3 gerar_video.py --previa 2,9,20  # salva quadros de prévia em PNG

Dependências: pip install Pillow numpy imageio-ffmpeg
"""
import argparse
import functools
import math
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

from trilha import gerar_trilha

AQUI = os.path.dirname(os.path.abspath(__file__))
FOTOS = os.path.join(AQUI, "fotos")
FONTES = os.path.join(AQUI, "fontes")
SAIDA = os.path.join(AQUI, "saida")

# ------------------------------------------------------------------ textos
NOME = "Casa Container"
MARCA = NOME.upper()
TEXTOS = {
    "abertura": dict(sobre="BEM-VINDO À", titulo=NOME, sub="Design moderno em meio à natureza"),
    "deck": dict(sobre="01 — ÁREA EXTERNA", titulo="Deck e terraço", sub="Espaços ao ar livre para relaxar"),
    "jardim": dict(sobre="01 — ÁREA EXTERNA", titulo="Jardim iluminado", sub="Paisagismo tropical com iluminação em LED"),
    "sala": dict(sobre="02 — SALA", titulo="Ambiente integrado", sub="Porta de vidro com acesso direto ao deck"),
    "cozinha": dict(sobre="03 — COZINHA", titulo="Cozinha equipada",
                    itens=["Geladeira", "Fogão cooktop", "Micro-ondas", "Mesa de refeições"]),
    "quarto": dict(sobre="04 — QUARTO", titulo="Quarto aconchegante", sub="Cama de casal e cortinas para um sono tranquilo"),
    "banheiro": dict(sobre="05 — BANHEIRO", titulo="Cabine com hidromassagem", sub="Acabamento moderno e muito conforto"),
    "mosaico": dict(sobre="TUDO EM UM SÓ LUGAR", frase="Moderna. Aconchegante. Completa."),
    "final": dict(sobre=MARCA, titulo="Venha conhecer", sub="Um refúgio moderno esperando por você"),
}

FPS = 30
XF = 0.9  # duração das transições (s)
GRAO = 1.2  # intensidade do grão de filme (0 = desliga)
CRF = 21  # qualidade do H.264 (menor = maior qualidade e arquivo)
DOURADO = (233, 192, 138)
BRANCO = (255, 255, 255)
FUNDO = (18, 16, 15)


# ------------------------------------------------------------------ utilidades
def clamp01(x):
    return 0.0 if x < 0 else 1.0 if x > 1 else x


def ease_io(x):
    x = clamp01(x)
    return x * x * (3 - 2 * x)


def ease_out(x):
    x = clamp01(x)
    return 1 - (1 - x) ** 3


def ease_kb(x):
    x = clamp01(x)
    return 0.6 * x + 0.4 * ease_io(x)


def ffmpeg_exe():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return "ffmpeg"


@functools.lru_cache(maxsize=None)
def fonte(nome, tamanho, peso=400):
    caminhos = {
        "serif": "PlayfairDisplay[wght].ttf",
        "serif-it": "PlayfairDisplay-Italic[wght].ttf",
        "sans": "Montserrat[wght].ttf",
    }
    try:
        f = ImageFont.truetype(os.path.join(FONTES, caminhos[nome]), tamanho)
        f.set_variation_by_axes([peso])
        return f
    except OSError:
        reserva = "DejaVuSerif.ttf" if nome.startswith("serif") else "DejaVuSans.ttf"
        return ImageFont.truetype(reserva, tamanho)


# ------------------------------------------------------------------ fotos
class Foto:
    """Foto original com versões ampliadas em cache (para zoom sem serrilhado)."""

    NIVEIS = (1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8)

    def __init__(self, arquivo):
        im = Image.open(os.path.join(FOTOS, arquivo)).convert("RGB")
        im = ImageEnhance.Contrast(im).enhance(1.05)
        self.base = ImageEnhance.Color(im).enhance(1.08)
        self.cache = {}

    def nivel(self, fator):
        f = next((n for n in self.NIVEIS if n >= fator * 0.95), self.NIVEIS[-1])
        if f not in self.cache:
            w, h = self.base.size
            im = self.base
            if f > 1:
                im = im.resize((round(w * f), round(h * f)), Image.Resampling.LANCZOS)
                im = im.filter(ImageFilter.UnsharpMask(radius=0.9 * f, percent=55, threshold=2))
            self.cache[f] = im
        return self.cache[f]

    def para(self, tamanho, zmax):
        ow, oh = tamanho
        w, h = self.base.size
        bw = min(w, h * ow / oh)
        return self.nivel(ow / (bw / zmax))


def janela_kb(src, a, b, p, tamanho):
    """Recorte Ken Burns: a e b são (cx, cy, zoom) normalizados."""
    sw, sh = src.size
    ow, oh = tamanho
    ar = ow / oh
    bw, bh = (sh * ar, sh) if sw / sh > ar else (sw, sw / ar)
    e = ease_kb(p)
    cx = a[0] + (b[0] - a[0]) * e
    cy = a[1] + (b[1] - a[1]) * e
    z = math.exp(math.log(a[2]) + (math.log(b[2]) - math.log(a[2])) * e)
    ww, wh = bw / z, bh / z
    x0 = min(max(cx * sw - ww / 2, 0), sw - ww)
    y0 = min(max(cy * sh - wh / 2, 0), sh - wh)
    return src.transform(tamanho, Image.Transform.AFFINE, (ww / ow, 0, x0, 0, wh / oh, y0),
                         resample=Image.Resampling.BICUBIC)


def cobrir(im, tamanho):
    ow, oh = tamanho
    w, h = im.size
    s = max(ow / w, oh / h)
    im = im.resize((math.ceil(w * s), math.ceil(h * s)), Image.Resampling.LANCZOS)
    x, y = (im.width - ow) // 2, (im.height - oh) // 2
    return im.crop((x, y, x + ow, y + oh))


def fundo_desfocado(foto, tamanho, escurecer=0.42):
    pequeno = cobrir(foto.base, (tamanho[0] // 8, tamanho[1] // 8))
    pequeno = pequeno.filter(ImageFilter.GaussianBlur(6))
    im = pequeno.resize(tamanho, Image.Resampling.BICUBIC)
    return ImageEnhance.Brightness(im).enhance(escurecer)


def mascara_arredondada(tamanho, raio):
    m = Image.new("L", tamanho, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, tamanho[0] - 1, tamanho[1] - 1), raio, fill=255)
    return m


def sombra(fundo, ret, raio, forca=0.6, desfoque=40):
    x, y, w, h = ret
    m = Image.new("L", fundo.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((x, y + 18, x + w, y + h + 18), raio, fill=int(255 * forca))
    m = m.filter(ImageFilter.GaussianBlur(desfoque))
    fundo.paste(Image.new("RGB", fundo.size, (0, 0, 0)), (0, 0), m)


# ------------------------------------------------------------------ texto
def camada_texto(texto, fnt, cor=BRANCO, tracking=0, sombra_forca=0.55, opacidade=1.0):
    pad = 40
    if tracking:
        larg = sum(fnt.getlength(c) for c in texto) + tracking * (len(texto) - 1)
    else:
        larg = fnt.getlength(texto)
    asc, desc = fnt.getmetrics()
    tam = (int(math.ceil(larg)) + 2 * pad, asc + desc + 2 * pad)
    alfa = Image.new("L", tam, 0)
    d = ImageDraw.Draw(alfa)
    if tracking:
        x = pad
        for c in texto:
            d.text((x, pad), c, font=fnt, fill=255)
            x += fnt.getlength(c) + tracking
    else:
        d.text((pad, pad), texto, font=fnt, fill=255)
    camada = Image.new("RGBA", tam, (0, 0, 0, 0))
    if sombra_forca:
        s = alfa.filter(ImageFilter.GaussianBlur(12)).point(lambda v: int(v * sombra_forca))
        camada.putalpha(s)
    cor_im = Image.new("RGBA", tam, cor + (255,))
    cor_im.putalpha(alfa.point(lambda v: int(v * opacidade)))
    camada = Image.alpha_composite(camada, cor_im)
    return dict(camada=camada, pad=pad, w=larg, h=asc + desc)


def quebrar(texto, fnt, largura):
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        if atual and fnt.getlength(teste) > largura:
            linhas.append(atual)
            atual = palavra
        else:
            atual = teste
    return linhas + [atual]


class Bloco:
    """Pilha de elementos de texto animados (entrada escalonada)."""

    def __init__(self, x, y, alinhar="left", ancora="top", inicio=0.5, intervalo=0.14, saida=None):
        self.x, self.y, self.alinhar, self.ancora = x, y, alinhar, ancora
        self.inicio, self.intervalo, self.saida = inicio, intervalo, saida
        self.elementos = []

    def texto(self, texto, fnt, espaco=0, **kw):
        el = camada_texto(texto, fnt, **kw)
        el["espaco"] = espaco
        self.elementos.append(el)
        return self

    def linha(self, largura, espaco=0, altura=2):
        camada = Image.new("RGBA", (largura, altura), DOURADO + (255,))
        self.elementos.append(dict(camada=camada, pad=0, w=largura, h=altura, espaco=espaco, linha=True))
        return self

    def item(self, texto, fnt, espaco=0):
        traco = camada_texto("—", fnt, cor=DOURADO)
        txt = camada_texto(texto, fnt)
        gap = 18
        w = traco["w"] + gap + txt["w"]
        camada = Image.new("RGBA", (int(w) + 80, txt["camada"].height), (0, 0, 0, 0))
        camada.alpha_composite(traco["camada"], (0, 0))
        camada.alpha_composite(txt["camada"], (int(traco["w"] + gap), 0))
        self.elementos.append(dict(camada=camada, pad=40, w=w, h=txt["h"], espaco=espaco))
        return self

    def espaco(self, px):
        self.elementos[-1]["espaco"] += px
        return self

    def altura(self):
        return sum(e["h"] + e["espaco"] for e in self.elementos) - self.elementos[-1]["espaco"]

    def desenhar(self, quadro, t):
        y = self.y
        if self.ancora == "bottom":
            y -= self.altura()
        elif self.ancora == "middle":
            y -= self.altura() / 2
        for i, el in enumerate(self.elementos):
            a = ease_out((t - self.inicio - i * self.intervalo) / 0.8)
            if self.saida is not None:
                a *= 1 - ease_io((t - self.saida) / 0.5)
            if a > 0.003:
                x = self.x - {"center": el["w"] / 2, "right": el["w"]}.get(self.alinhar, 0)
                dy = (1 - a) * 26
                camada = el["camada"]
                if el.get("linha"):
                    w = max(1, int(el["w"] * a))
                    camada = camada.crop((0, 0, w, camada.height))
                    x = self.x - {"center": w / 2, "right": w}.get(self.alinhar, 0)
                    dy = 0
                alfa = np.asarray(camada.getchannel("A"), dtype=np.float32) * a
                mask = Image.fromarray(alfa.astype(np.uint8))
                quadro.paste(camada.convert("RGB"), (int(round(x - el["pad"])), int(round(y + dy - el["pad"]))), mask)
            y += el["h"] + el["espaco"]


# ------------------------------------------------------------------ cenas
class Cena:
    dur = 5.0

    def render(self, t):
        raise NotImplementedError


class CenaCheia(Cena):
    """Foto em tela cheia com movimento Ken Burns e gradiente para o texto."""

    def __init__(self, tamanho, foto, a, b, bloco, dur, estilo="inferior"):
        self.tamanho, self.a, self.b, self.bloco, self.dur = tamanho, a, b, bloco, dur
        self.src = foto.para(tamanho, max(a[2], b[2]))
        W, H = tamanho
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        if estilo.startswith("inferior"):
            lx = xx / W if estilo == "inferior" else 1 - xx / W
            g = np.clip((yy / H - 0.38) / 0.62, 0, 1) ** 1.4 * 0.82 * (1 - 0.45 * lx)
            g = np.maximum(g, np.clip((0.2 - yy / H) / 0.2, 0, 1) * 0.5 * (1 - 0.6 * xx / W))
        else:
            r = np.hypot((xx - W / 2) / (W / 2), (yy - H / 2) / (H / 2))
            brilho = np.exp(-((xx - W / 2) / (0.36 * W)) ** 2 - ((yy - H / 2) / (0.2 * H)) ** 2)
            g = 0.30 + 0.22 * np.clip(r, 0, 1.4) + 0.28 * brilho
        self.escuro = Image.fromarray((np.clip(g, 0, 1) * 255).astype(np.uint8))
        self.preto = Image.new("RGB", tamanho, (0, 0, 0))

    def render(self, t):
        q = janela_kb(self.src, self.a, self.b, t / self.dur, self.tamanho)
        q.paste(self.preto, (0, 0), self.escuro)
        self.bloco.desenhar(q, t)
        return q


class CenaPainel(Cena):
    """Foto em um painel arredondado sobre um fundo desfocado da própria foto."""

    def __init__(self, tamanho, foto, ret, a, b, bloco, dur, raio=22):
        self.tamanho, self.ret, self.a, self.b, self.bloco, self.dur = tamanho, ret, a, b, bloco, dur
        x, y, w, h = ret
        self.src = foto.para((w, h), max(a[2], b[2]))
        self.fundo = fundo_desfocado(foto, tamanho)
        sombra(self.fundo, ret, raio)
        self.mask = mascara_arredondada((w, h), raio)

    def render(self, t):
        q = self.fundo.copy()
        x, y, w, h = self.ret
        q.paste(janela_kb(self.src, self.a, self.b, t / self.dur, (w, h)), (x, y), self.mask)
        self.bloco.desenhar(q, t)
        return q


class CenaMosaico(Cena):
    """Várias fotos em ladrilhos que sobem em sequência."""

    def __init__(self, tamanho, ladrilhos, blocos, dur, raio=16):
        self.tamanho, self.blocos, self.dur = tamanho, blocos, dur
        W, H = tamanho
        yy = np.mgrid[0:H, 0:W][0].astype(np.float32) / H
        grad = (np.array(FUNDO) * (1.15 - 0.3 * yy[..., None])).clip(0, 255).astype(np.uint8)
        self.fundo = Image.fromarray(grad)
        self.ladrilhos = []
        for foto, ret, foco in ladrilhos:
            w, h = ret[2], ret[3]
            self.ladrilhos.append((foto.para((w, h), 1.1), ret, foco, mascara_arredondada((w, h), raio)))

    def render(self, t):
        q = self.fundo.copy()
        for i, (src, (x, y, w, h), foco, mask) in enumerate(self.ladrilhos):
            a = ease_out((t - 0.25 - i * 0.12) / 0.9)
            if a <= 0.003:
                continue
            im = janela_kb(src, (foco, 0.5, 1.1), (foco, 0.5, 1.0), t / self.dur, (w, h))
            m = Image.fromarray((np.asarray(mask, dtype=np.float32) * a).astype(np.uint8))
            q.paste(im, (x, int(y + (1 - a) * 60)), m)
        for b in self.blocos:
            b.desenhar(q, t)
        return q


# ------------------------------------------------------------------ roteiro
def roteiro(formato, fotos):
    fachada, sala, cozinha, quarto, banheiro = (fotos[k] for k in ("fachada", "sala", "cozinha", "quarto", "banheiro"))
    horizontal = formato == "h"
    W, H = (1920, 1080) if horizontal else (1080, 1920)
    tam = (W, H)
    k = 1.0 if horizontal else 0.95  # escala da tipografia

    def f_sobre():
        return fonte("sans", int(24 * k), 600)

    def f_titulo(s=82):
        return fonte("serif", int(s * k), 400)

    def f_sub():
        return fonte("sans", int(34 * k), 300)

    def bloco_legenda(chave, dur, lado="left"):
        tx = TEXTOS[chave]
        saida = dur - XF - 0.35
        if horizontal:
            b = Bloco(120 if lado == "left" else W - 120, H - 120, alinhar=lado, ancora="bottom", saida=saida)
            b.linha(64, espaco=22)
            b.texto(tx["sobre"], f_sobre(), tracking=7, cor=DOURADO, espaco=6)
            b.texto(tx["titulo"], f_titulo(), espaco=4)
            b.texto(tx["sub"], f_sub(), cor=(236, 232, 226))
            return b
        b = Bloco(80, 1210, saida=saida)
        b.linha(64, espaco=26)
        b.texto(tx["sobre"], f_sobre(), tracking=6, cor=DOURADO, espaco=8)
        for ln in quebrar(tx["titulo"], f_titulo(84), 900):
            b.texto(ln, f_titulo(84), espaco=0)
        b.espaco(10)
        for ln in quebrar(tx["sub"], f_sub(), 900):
            b.texto(ln, f_sub(), cor=(236, 232, 226), espaco=4)
        return b

    def bloco_central(chave, y, tam_titulo, saida=None):
        tx = TEXTOS[chave]
        b = Bloco(W // 2, y, alinhar="center", ancora="middle", inicio=0.7, intervalo=0.2, saida=saida)
        b.texto(tx["sobre"], fonte("sans", int(26 * k), 500), tracking=10, cor=DOURADO, espaco=4)
        b.texto(tx["titulo"], f_titulo(tam_titulo), espaco=22)
        b.linha(90, espaco=30)
        for ln in quebrar(tx["sub"], fonte("sans", int(36 * k), 300), W - 160):
            b.texto(ln, fonte("sans", int(36 * k), 300), tracking=1, cor=(236, 232, 226), espaco=4)
        return b

    cenas = []
    if horizontal:
        d = 7.0
        cenas.append(CenaCheia(tam, fachada, (0.5, 0.5, 1.14), (0.48, 0.52, 1.0),
                               bloco_central("abertura", H // 2, 132, saida=d - XF - 0.4), d, "central"))
        d = 5.4
        cenas.append(CenaCheia(tam, fachada, (0.30, 0.42, 1.2), (0.36, 0.44, 1.32), bloco_legenda("deck", d), d))
        cenas.append(CenaCheia(tam, fachada, (0.78, 0.58, 1.28), (0.66, 0.55, 1.16), bloco_legenda("jardim", d), d))
        d = 5.8
        cenas.append(CenaCheia(tam, sala, (0.42, 0.5, 1.04), (0.56, 0.52, 1.16), bloco_legenda("sala", d), d))

        tx = TEXTOS["cozinha"]
        b = Bloco(1200, H // 2, ancora="middle", saida=d - XF - 0.35)
        b.linha(64, espaco=24)
        b.texto(tx["sobre"], f_sobre(), tracking=7, cor=DOURADO, espaco=8)
        for ln in ("Cozinha", "equipada"):
            b.texto(ln, f_titulo(88))
        b.espaco(26)
        for it in tx["itens"]:
            b.item(it, fonte("sans", 34, 300), espaco=14)
        cenas.append(CenaPainel(tam, cozinha, (130, 190, 960, 700), (0.4, 0.5, 1.0), (0.56, 0.52, 1.06), b, d))

        cenas.append(CenaCheia(tam, quarto, (0.5, 0.5, 1.14), (0.46, 0.5, 1.02), bloco_legenda("quarto", d), d))
        cenas.append(CenaCheia(tam, banheiro, (0.36, 0.52, 1.02), (0.42, 0.5, 1.14),
                               bloco_legenda("banheiro", d, "right"), d, "inferior-dir"))

        d = 6.2
        tx = TEXTOS["mosaico"]
        lw, lh, gap = 320, 540, 22
        x0 = (W - (5 * lw + 4 * gap)) // 2
        fotos_m = [(fachada, 0.32), (sala, 0.5), (cozinha, 0.45), (quarto, 0.45), (banheiro, 0.42)]
        ladr = [(f, (x0 + i * (lw + gap), 250, lw, lh), fc) for i, (f, fc) in enumerate(fotos_m)]
        topo = Bloco(W // 2, 150, alinhar="center", ancora="middle", inicio=0.1, saida=d - XF - 0.35)
        topo.texto(tx["sobre"], fonte("sans", 24, 600), tracking=10, cor=DOURADO)
        base = Bloco(W // 2, 895, alinhar="center", ancora="middle", inicio=1.0, saida=d - XF - 0.35)
        base.texto(tx["frase"], fonte("serif-it", 64, 400))
        cenas.append(CenaMosaico(tam, ladr, [topo, base], d))

        d = 7.5
        cenas.append(CenaCheia(tam, fachada, (0.47, 0.48, 1.0), (0.44, 0.46, 1.12),
                               bloco_central("final", H // 2, 120), d, "central"))
        return tam, cenas

    # ---- vertical 9:16 (Reels / Stories / Status)
    painel = (60, 290, 960, 860)

    def cena_v(foto, a, b, chave, d):
        return CenaPainel(tam, foto, painel, a, b, bloco_legenda(chave, d), d, raio=26)

    d = 7.0
    ab = bloco_central("abertura", 1420, 118, saida=d - XF - 0.4)
    cenas.append(CenaPainel(tam, fachada, painel, (0.45, 0.5, 1.12), (0.42, 0.5, 1.0), ab, d, raio=26))
    d = 5.4
    cenas.append(cena_v(fachada, (0.28, 0.42, 1.12), (0.33, 0.44, 1.24), "deck", d))
    cenas.append(cena_v(fachada, (0.76, 0.58, 1.2), (0.66, 0.55, 1.1), "jardim", d))
    d = 5.8
    cenas.append(cena_v(sala, (0.4, 0.5, 1.0), (0.55, 0.52, 1.1), "sala", d))

    tx = TEXTOS["cozinha"]
    b = Bloco(80, 1210, saida=d - XF - 0.35)
    b.linha(64, espaco=26)
    b.texto(tx["sobre"], f_sobre(), tracking=6, cor=DOURADO, espaco=8)
    b.texto(tx["titulo"], f_titulo(84), espaco=24)
    for it in tx["itens"]:
        b.item(it, fonte("sans", 33, 300), espaco=10)
    cenas.append(CenaPainel(tam, cozinha, painel, (0.3, 0.5, 1.0), (0.7, 0.52, 1.0), b, d, raio=26))

    cenas.append(cena_v(quarto, (0.5, 0.5, 1.12), (0.45, 0.5, 1.0), "quarto", d))
    cenas.append(cena_v(banheiro, (0.36, 0.52, 1.0), (0.44, 0.5, 1.12), "banheiro", d))

    d = 6.2
    tx = TEXTOS["mosaico"]
    lw, lh, gap = 465, 560, 30
    x0 = (W - (2 * lw + gap)) // 2
    grade = [(fachada, 0.32), (sala, 0.5), (quarto, 0.45), (banheiro, 0.42)]
    ladr = [(f, (x0 + (i % 2) * (lw + gap), 330 + (i // 2) * (lh + gap), lw, lh), fc) for i, (f, fc) in enumerate(grade)]
    topo = Bloco(W // 2, 250, alinhar="center", ancora="middle", inicio=0.1, saida=d - XF - 0.35)
    topo.texto(tx["sobre"], fonte("sans", 24, 600), tracking=9, cor=DOURADO)
    base = Bloco(W // 2, 1650, alinhar="center", ancora="middle", inicio=1.0, intervalo=0.2, saida=d - XF - 0.35)
    for frase in tx["frase"].split(" "):
        base.texto(frase, fonte("serif-it", 62, 400), espaco=4)
    cenas.append(CenaMosaico(tam, ladr, [topo, base], d))

    d = 7.5
    cenas.append(CenaPainel(tam, fachada, painel, (0.45, 0.48, 1.0), (0.42, 0.46, 1.12),
                            bloco_central("final", 1420, 112), d, raio=26))
    return tam, cenas


# ------------------------------------------------------------------ montagem
class Filme:
    def __init__(self, formato, fotos):
        self.formato = formato
        self.tam, self.cenas = roteiro(formato, fotos)
        self.inicios, t = [], 0.0
        for c in self.cenas:
            self.inicios.append(t)
            t += c.dur - XF
        self.dur = t + XF
        W, H = self.tam
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        r = np.hypot((xx - W / 2) / (W / 2), (yy - H / 2) / (H / 2))
        self.vinheta = Image.fromarray((np.clip(0.38 * (r / 1.414) ** 2.2, 0, 1) * 255).astype(np.uint8))
        self.preto = Image.new("RGB", self.tam, (0, 0, 0))
        rng = np.random.default_rng(3)
        self.grao = [rng.normal(0, GRAO, (H, W)).astype(np.int16) for _ in range(6)] if GRAO else None
        self.marca = camada_texto(MARCA, fonte("sans", 20, 600), tracking=8, opacidade=0.85, sombra_forca=0.4)
        self.marca_ini = self.inicios[1] + 0.6
        self.marca_fim = self.inicios[-1]

    def quadro(self, t, n=0):
        ativos = [i for i, s in enumerate(self.inicios) if s <= t < s + self.cenas[i].dur]
        if not ativos:
            ativos = [len(self.cenas) - 1]
        i = ativos[0]
        q = self.cenas[i].render(t - self.inicios[i])
        if len(ativos) > 1:
            j = ativos[1]
            q2 = self.cenas[j].render(t - self.inicios[j])
            q = Image.blend(q, q2, ease_io((t - self.inicios[j]) / XF))

        a = ease_io((t - self.marca_ini) / 0.8) * (1 - ease_io((t - self.marca_fim) / XF))
        if a > 0.003 and not self._mosaico_ativo(t):
            el = self.marca
            if self.formato == "h":
                pos = (120 - el["pad"], 80 - el["pad"])
            else:
                pos = (int(self.tam[0] / 2 - el["w"] / 2 - el["pad"]), 120 - el["pad"])
            alfa = np.asarray(el["camada"].getchannel("A"), dtype=np.float32) * a
            q.paste(el["camada"].convert("RGB"), pos, Image.fromarray(alfa.astype(np.uint8)))

        q.paste(self.preto, (0, 0), self.vinheta)
        escuro = 1 - ease_io(t / 1.0) if t < 1.0 else ease_io((t - (self.dur - 1.6)) / 1.6)
        if escuro > 0:
            q = Image.blend(q, self.preto, escuro)
        if self.grao is None:
            return np.asarray(q)
        arr = np.asarray(q, dtype=np.int16) + self.grao[n % len(self.grao)][..., None]
        return np.clip(arr, 0, 255).astype(np.uint8)

    def _mosaico_ativo(self, t):
        for i, c in enumerate(self.cenas):
            if isinstance(c, CenaMosaico):
                s = self.inicios[i]
                return s + XF * 0.5 <= t < s + c.dur - XF * 0.5
        return False

    def renderizar(self, destino, audio):
        W, H = self.tam
        total = int(round(self.dur * FPS))
        cmd = [ffmpeg_exe(), "-y", "-loglevel", "error",
               "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
               "-i", audio,
               "-c:v", "libx264", "-preset", "slow", "-crf", str(CRF), "-pix_fmt", "yuv420p",
               "-profile:v", "high", "-maxrate", "12M", "-bufsize", "24M",
               "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", destino]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for n in range(total):
            proc.stdin.write(self.quadro(n / FPS, n).tobytes())
            if n % (FPS * 5) == 0:
                print(f"  {os.path.basename(destino)}: {n / FPS:5.1f}s / {self.dur:.1f}s", flush=True)
        proc.stdin.close()
        if proc.wait() != 0:
            sys.exit("ffmpeg falhou")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--formato", choices=["h", "v", "ambos"], default="ambos")
    ap.add_argument("--previa", help="instantes (s) separados por vírgula para salvar como PNG")
    args = ap.parse_args()

    os.makedirs(SAIDA, exist_ok=True)
    fotos = {
        "fachada": Foto("fachada.webp"),
        "sala": Foto("sala.png"),
        "cozinha": Foto("cozinha.png"),
        "quarto": Foto("quarto.png"),
        "banheiro": Foto("banheiro.webp"),
    }
    formatos = ["h", "v"] if args.formato == "ambos" else [args.formato]
    for fmt in formatos:
        filme = Filme(fmt, fotos)
        nome = "apresentacao-horizontal" if fmt == "h" else "apresentacao-vertical"
        if args.previa:
            for s in args.previa.split(","):
                t = float(s)
                Image.fromarray(filme.quadro(t)).save(os.path.join(SAIDA, f"previa-{fmt}-{t:05.1f}.png"))
            continue
        audio = os.path.join(SAIDA, "trilha.wav")
        gerar_trilha(filme.dur, audio)
        print(f"Renderizando {nome} ({filme.dur:.1f}s)...")
        filme.renderizar(os.path.join(SAIDA, nome + ".mp4"), audio)
        # capa (quadro de abertura com o título já visível)
        Image.fromarray(filme.quadro(2.6)).save(os.path.join(SAIDA, nome + "-capa.jpg"), quality=92)


if __name__ == "__main__":
    main()
