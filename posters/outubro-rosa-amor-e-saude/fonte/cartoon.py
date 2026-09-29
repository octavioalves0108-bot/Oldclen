"""Cartoon estilo ilustração: base estilizada, sombreamento suave em faixas e traço fino."""
import sys
import cv2
import numpy as np

src_path, mask_path, out_path = sys.argv[1:4]
LEVELS = int(sys.argv[4]); SHADE_MIX = float(sys.argv[5]); MIN_AREA = int(sys.argv[6])

img = cv2.imread(src_path)
alpha = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)[:, :, 3]
h, w = img.shape[:2]; S = 2
img = cv2.resize(img, (w * S, h * S), interpolation=cv2.INTER_LANCZOS4)
alpha = cv2.resize(alpha, (w * S, h * S), interpolation=cv2.INTER_LINEAR)

base = cv2.stylization(img, sigma_s=90, sigma_r=0.3)
for _ in range(3):
    base = cv2.bilateralFilter(base, 9, 25, 9)

lab = cv2.cvtColor(base, cv2.COLOR_BGR2LAB).astype(np.float32)
L, A, B = cv2.split(lab)
# tira o brilho estourado só na pele (cor saturada); preserva os fios grisalhos
chroma = np.sqrt((A - 128) ** 2 + (B - 128) ** 2)
wsk = np.clip((cv2.GaussianBlur(chroma, (0, 0), 3) - 8) / 12, 0, 1)
L = np.where(L > 178, L - wsk * (L - 178) * 0.6, L)
Ls = cv2.GaussianBlur(L, (0, 0), 3.0)
step = 255.0 / LEVELS
Lq = (np.floor(Ls / step) + 0.5) * step
Lq = cv2.GaussianBlur(Lq, (0, 0), 2.0)
Lout = SHADE_MIX * Lq + (1 - SHADE_MIX) * L
# pele: sombras largas e lisas (3 tons), como em desenho
wsk_s = cv2.GaussianBlur(wsk, (0, 0), 6)
Lsk = cv2.GaussianBlur(np.minimum(L, 170), (0, 0), 6.0)
stp = 255.0 / 4
Lskq = cv2.GaussianBlur((np.floor(Lsk / stp) + 0.5) * stp, (0, 0), 4.0)
Lsk_out = 0.65 * Lskq + 0.35 * Lsk
Lout = wsk_s * Lsk_out + (1 - wsk_s) * Lout
A = 128 + (cv2.GaussianBlur(A, (0, 0), 2) - 128) * 1.22
B = 128 + (cv2.GaussianBlur(B, (0, 0), 2) - 128) * 1.22
A = wsk_s * cv2.GaussianBlur(A, (0, 0), 8) + (1 - wsk_s) * A
B = wsk_s * cv2.GaussianBlur(B, (0, 0), 8) + (1 - wsk_s) * B
col = cv2.cvtColor(np.clip(cv2.merge([Lout, A, B]), 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)

# traço: XDoG numa versão levemente suavizada (preserva olhos, nariz, boca)
soft = img.copy()
for _ in range(3):
    soft = cv2.bilateralFilter(soft, 7, 30, 7)
g = cv2.cvtColor(soft, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
dog = cv2.GaussianBlur(g, (0, 0), 1.3) - 0.99 * cv2.GaussianBlur(g, (0, 0), 2.1)
line = (dog < -0.010).astype(np.uint8)
n, lbl, st, _ = cv2.connectedComponentsWithStats(line, connectivity=8)
keep = np.zeros(n, bool); keep[1:] = st[1:, cv2.CC_STAT_AREA] >= MIN_AREA
line = cv2.GaussianBlur(keep[lbl].astype(np.float32), (0, 0), 0.9)
# traço mais leve no cabelo (pouca cor) e mais firme no rosto
strong = (dog < -0.022).astype(np.float32)
strong = cv2.GaussianBlur(strong, (0, 0), 0.9)
line = wsk_s * np.maximum(strong, line * 0.7) + (1 - wsk_s) * line * 0.6
edge = cv2.morphologyEx((alpha > 128).astype(np.uint8), cv2.MORPH_GRADIENT, np.ones((5, 5), np.uint8)).astype(np.float32)
line = np.maximum(line, cv2.GaussianBlur(edge, (0, 0), 1.0))

ink = np.array([55, 32, 75], np.float32)
k = line[..., None] * 0.75
res = np.clip(col.astype(np.float32) * (1 - k) + ink * k, 0, 255).astype(np.uint8)
rgba = cv2.cvtColor(res, cv2.COLOR_BGR2BGRA); rgba[:, :, 3] = alpha
cv2.imwrite(out_path, rgba); print("ok")
