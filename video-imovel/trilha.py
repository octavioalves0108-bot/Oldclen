"""Trilha sonora ambiente sintetizada (piano suave + pad + baixo), sem direitos autorais."""
import math
import wave

import numpy as np

SR = 44100

# Progressão em Ré maior: Dmaj9 - Bm9 - Gmaj9 - A7sus4
ACORDES = [
    [50, 57, 61, 64, 66],
    [47, 54, 57, 61, 62],
    [43, 50, 54, 57, 59],
    [45, 52, 55, 59, 62],
]
ARPEJOS = [
    [62, 66, 69, 73, 76],
    [59, 62, 66, 69, 73],
    [55, 59, 62, 66, 69],
    [57, 62, 64, 67, 71],
]
RAIZES = [38, 35, 43, 45]
PADRAO = [0, 2, 4, 3, 1, 2, 4, 2]


def _hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def _piano(freq, dur=3.2):
    tt = np.arange(int(dur * SR)) / SR
    s = np.zeros_like(tt)
    for k in range(1, 9):
        fk = k * freq * math.sqrt(1 + 0.0003 * k * k)
        if fk > SR / 2 - 2000:
            break
        tau = 1.7 / (1 + 0.7 * (k - 1))
        s += (1 / k ** 1.4) * np.exp(-tt / tau) * np.sin(2 * math.pi * fk * tt)
    return s * np.minimum(1, tt / 0.004)


def _somar(buf, ini, sinal):
    if ini >= len(buf):
        return
    fim = min(len(buf), ini + len(sinal))
    buf[ini:fim] += sinal[: fim - ini]


def _reverb(x, rng, dur=3.4):
    m = int(dur * SR)
    tt = np.arange(m) / SR
    ir = rng.normal(size=m) * np.exp(-tt / 0.85)
    ir = np.convolve(ir, np.ones(12) / 12, mode="same")
    ir[: int(0.02 * SR)] = 0
    ir /= np.sqrt(np.sum(ir ** 2))
    n = len(x) + m
    tam = 1 << (n - 1).bit_length()
    y = np.fft.irfft(np.fft.rfft(x, tam) * np.fft.rfft(ir, tam), tam)
    return y[: len(x)]


def gerar_trilha(duracao, caminho, bpm=70, semente=7):
    rng = np.random.default_rng(semente)
    n = int((duracao + 0.2) * SR)
    t = np.arange(n) / SR
    esq, dir_ = np.zeros(n), np.zeros(n)
    batida = 60 / bpm
    compasso = 4 * batida
    ncomp = int(math.ceil(duracao / compasso)) + 1
    ultimo = int(duracao // compasso)

    # Pad: vozes levemente desafinadas, entrada e saída lentas
    for k in range(ncomp):
        t0 = k * compasso
        i0 = int(t0 * SR)
        if i0 >= n:
            break
        i1 = min(n, int((t0 + compasso + 2.2) * SR))
        tt = t[i0:i1] - t0
        env = np.clip(tt / 1.8, 0, 1) * np.clip(1 - (tt - compasso) / 2.2, 0, 1)
        env = env ** 1.6 * (1 + 0.08 * np.sin(2 * math.pi * 0.23 * tt))
        for m in ACORDES[k % 4]:
            f = _hz(m)
            for det, pan in ((-0.0035, 0.8), (0.0, 0.5), (0.0035, 0.2)):
                fase = rng.uniform(0, 2 * math.pi)
                w = 2 * math.pi * f * (1 + det) * tt + fase
                s = (np.sin(w) + 0.22 * np.sin(2 * w) + 0.07 * np.sin(3 * w)) * env * 0.022
                esq[i0:i1] += s * pan
                dir_[i0:i1] += s * (1 - pan)

    # Piano em arpejo (a partir do 2º compasso)
    cache = {}
    for k in range(1, ncomp):
        if k * compasso >= duracao - 1:
            break
        notas = ARPEJOS[k % 4]
        if k >= ultimo:
            for j, m in enumerate(notas[:4]):
                cache.setdefault(m, _piano(_hz(m), 5.0))
                s = cache[m] * 0.16
                ini = int((k * compasso + j * 0.09) * SR)
                _somar(esq, ini, s * 0.55)
                _somar(dir_, ini, s * 0.45)
            break
        for j, idx in enumerate(PADRAO):
            if j % 2 and rng.random() < 0.22:
                continue
            m = notas[idx]
            if m not in cache:
                cache[m] = _piano(_hz(m))
            vel = (0.2 if j % 4 == 0 else 0.13) * rng.uniform(0.85, 1.1)
            ini = int((k * compasso + j * batida / 2 + rng.uniform(0, 0.012)) * SR)
            pan = 0.35 + 0.3 * idx / 4
            _somar(esq, ini, cache[m] * vel * pan)
            _somar(dir_, ini, cache[m] * vel * (1 - pan))

    # Baixo (a partir do 3º compasso)
    for k in range(2, ultimo + 1):
        f = _hz(RAIZES[k % 4])
        tt = np.arange(int((compasso + 1.5) * SR)) / SR
        env = np.minimum(1, tt / 0.08) * np.exp(-tt / 2.8) * np.clip(1 - (tt - compasso) / 1.5, 0, 1)
        s = (np.sin(2 * math.pi * f * tt) + 0.3 * np.sin(4 * math.pi * f * tt)) * env * 0.11
        ini = int(k * compasso * SR)
        _somar(esq, ini, s)
        _somar(dir_, ini, s)

    esq = esq + 0.5 * _reverb(esq, rng)
    dir_ = dir_ + 0.5 * _reverb(dir_, rng)
    mix = np.stack([esq, dir_], axis=1)
    mix -= mix.mean(axis=0)
    mix /= np.abs(mix).max()
    mix = np.tanh(1.8 * mix) / math.tanh(1.8)

    fade_in = np.minimum(1, t / 1.2)
    fade_out = np.clip((duracao - t) / 3.0, 0, 1) ** 1.5
    mix *= (fade_in * fade_out)[:, None] * 0.72

    pcm = (mix * 32767).astype("<i2")
    with wave.open(caminho, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
