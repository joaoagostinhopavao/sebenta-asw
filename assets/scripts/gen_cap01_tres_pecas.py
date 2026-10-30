"""As três peças de uma aplicação Web (Frontend, Middleware, Backend), a correspondência com o MVC e as aulas
onde cada uma é estudada (Cap01 / Aula 01 da ASW).

Uso: python gen_cap01_tres_pecas.py <ficheiro_saida.png> [--en]
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)

DARK = "#0a1420"
MID = "#0e6e8c"
ACCENT = "#4dd0e1"
LIGHT = "#eaf6f8"
ORANGE = "#d4651a"
GREY = "#5f6b70"
FS = 18

out = sys.argv[1] if len(sys.argv) > 1 else "tres-pecas.png"

fig, ax = plt.subplots(figsize=(18, 7.2), dpi=200)
ax.set_xlim(0, 18)
ax.set_ylim(0, 7.2)
ax.axis("off")


def box(x0, y0, w, h, fc, ec, lw=2.4):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.18",
                                fc=fc, ec=ec, lw=lw, zorder=2))


pecas = [
    (0.3, "Frontend", "corre no cliente\n(browser)", "View", "Aula 02\nHTML, CSS e Bootstrap", DARK),
    (6.4, "Middleware", "liga o cliente ao servidor:\nnesta UC, sempre o HTTP", "", "Aula 03\nDa rede ao HTTP", ORANGE),
    (12.5, "Backend", "corre no servidor:\nlógica de negócio e dados", "Controller + Model", "Aulas 04 a 08\nServlets, sessões, REST, JWT", MID),
]
for x, nome, desc, mvc, aula, cor in pecas:
    box(x, 3.4, 5.2, 3.6, LIGHT, cor)
    ax.text(x + 2.6, 6.3, nome, ha="center", va="center", fontsize=FS + 6, color=cor, fontweight="bold", zorder=3)
    ax.text(x + 2.6, 5.15, desc, ha="center", va="center", fontsize=FS - 1, color=DARK, linespacing=1.25, zorder=3)
    if mvc:
        ax.text(x + 2.6, 3.95, "MVC: " + mvc, ha="center", va="center", fontsize=FS - 2, color=cor, style="italic",
                fontweight="bold", zorder=3)
    box(x + 0.4, 0.4, 4.4, 1.9, "white", cor, lw=2.0)
    ax.text(x + 2.6, 1.35, aula, ha="center", va="center", fontsize=FS - 2, color=DARK, linespacing=1.3, zorder=3)
    ax.add_patch(FancyArrowPatch((x + 2.6, 3.35), (x + 2.6, 2.35), arrowstyle="-|>", mutation_scale=20, color=GREY,
                                 lw=2, zorder=1))

for x0, x1 in ((5.55, 6.35), (11.65, 12.45)):
    ax.add_patch(FancyArrowPatch((x0, 5.4), (x1, 5.4), arrowstyle="<|-|>", mutation_scale=24, color=ORANGE, lw=3,
                                 zorder=3))

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
