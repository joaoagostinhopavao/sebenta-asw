"""Base64 passo a passo: o texto "Ana" (3 bytes, 24 bits) reagrupado em 4 grupos de 6 bits = "QW5h"
(Cap08 / Aula 08 da ASW).

Uso: python gen_cap08_base64.py <ficheiro_saida.png>
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

DARK = "#0a1420"
MID = "#0e6e8c"
LIGHT = "#eaf6f8"
GREY = "#5f6b70"
CORES = ["#0e6e8c", "#d4651a", "#218c4a"]       # uma cor por byte de origem
FS = 18
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "base64.png"

texto = "Ana"
bits = "".join(f"{ord(c):08b}" for c in texto)
grupos = [bits[i:i + 6] for i in range(0, 24, 6)]
assert "".join(ALFABETO[int(g, 2)] for g in grupos) == "QW5h"

CW = 0.62                      # largura de cada bit
X0 = 3.4
fig, ax = plt.subplots(figsize=(19.5, 8.6), dpi=200)
ax.set_xlim(0, 19.5)
ax.set_ylim(0, 8.6)
ax.axis("off")


def rotulo(y, txt):
    ax.text(0.2, y, txt, ha="left", va="center", fontsize=FS - 2, color=GREY, style="italic")


def bit(x, y, b, cor):
    ax.add_patch(Rectangle((x, y - 0.32), CW, 0.64, fc="white", ec=cor, lw=1.6, zorder=2))
    ax.text(x + CW / 2, y, b, ha="center", va="center", fontsize=FS - 1, family="monospace", color=cor,
            fontweight="bold", zorder=3)


# 1. os 3 caracteres, os seus códigos e os 8 bits de cada um
rotulo(7.9, "texto")
rotulo(7.0, "código (byte)")
rotulo(5.9, "8 bits por byte")
for k, c in enumerate(texto):
    x = X0 + k * (8 * CW + 0.35)
    cor = CORES[k]
    xm = x + 4 * CW
    ax.text(xm, 7.9, c, ha="center", va="center", fontsize=FS + 6, family="monospace", color=cor,
            fontweight="bold")
    ax.text(xm, 7.0, str(ord(c)), ha="center", va="center", fontsize=FS + 1, color=cor, fontweight="bold")
    for j in range(8):
        bit(x + j * CW, 5.9, bits[8 * k + j], cor)

ax.text(X0 + 12.5 * CW + 0.35, 4.8, "os mesmos 24 bits, agora em grupos de 6", ha="center", va="center",
        fontsize=FS - 2, color=DARK, style="italic")

# 2. os mesmos 24 bits em 4 grupos de 6, cada bit com a cor do byte de onde veio
rotulo(3.7, "6 bits por grupo")
rotulo(2.6, "valor (0 a 63)")
rotulo(1.5, "carácter Base64")
for g in range(4):
    x = X0 + g * (6 * CW + 0.35)
    for j in range(6):
        i = 6 * g + j
        bit(x + j * CW, 3.7, bits[i], CORES[i // 8])
    xm = x + 3 * CW
    v = int(grupos[g], 2)
    ax.text(xm, 2.6, str(v), ha="center", va="center", fontsize=FS + 1, color=DARK, fontweight="bold")
    ax.add_patch(FancyBboxPatch((xm - 0.45, 1.05), 0.9, 0.9, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=LIGHT, ec=MID, lw=2, zorder=2))
    ax.text(xm, 1.5, ALFABETO[v], ha="center", va="center", fontsize=FS + 6, family="monospace", color=MID,
            fontweight="bold", zorder=3)

ax.text(X0, 0.35, "tabela: 0-25 → A-Z,  26-51 → a-z,  52-61 → 0-9,  62 → -,  63 → _", ha="left", va="center",
        fontsize=FS - 3, color=GREY, family="monospace")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out, grupos)
