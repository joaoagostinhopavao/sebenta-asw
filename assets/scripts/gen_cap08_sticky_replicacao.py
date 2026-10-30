"""Os dois paliativos para usar sessões com vários servidores: sticky sessions e replicação de sessões
(Cap08 / Aula 08 da ASW).

Uso: python gen_cap08_sticky_replicacao.py <ficheiro_saida.png>
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

DARK = "#0a1420"
MID = "#0e6e8c"
LIGHT = "#eaf6f8"
ORANGE = "#d4651a"
RED = "#c0392b"
GREY = "#9aa7ad"
FS = 18

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "sticky_replicacao.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=2))


def arrow(ax, p, q, color, estilo="-|>", ls="-", lw=2.6):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=estilo, mutation_scale=22, color=color, lw=lw, zorder=3,
                                 linestyle=ls, shrinkA=0, shrinkB=0))


def painel(ax, x0, titulo, replicacao):
    ax.text(x0, 6.55, titulo, ha="left", va="center", fontsize=FS + 1, color=DARK, fontweight="bold",
            style="normal" if replicacao else "italic")
    box(ax, x0, 2.55, 2.2, 1.3, "white", DARK)
    ax.text(x0 + 1.1, 3.2, "Cliente\n(ana)", ha="center", va="center", fontsize=FS - 2, color=DARK,
            fontweight="bold", linespacing=1.2)
    box(ax, x0 + 3.0, 2.55, 2.4, 1.3, LIGHT, MID)
    ax.text(x0 + 4.2, 3.2, "Balanceador", ha="center", va="center", fontsize=FS - 3, color=MID, fontweight="bold")
    arrow(ax, (x0 + 2.25, 3.2), (x0 + 2.95, 3.2), MID)
    ya, yb = 4.35, 0.55
    for yy, nome in ((ya, "Servidor A"), (yb, "Servidor B")):
        box(ax, x0 + 6.3, yy, 3.0, 1.55, "white", MID, lw=2.0)
        ax.text(x0 + 6.5, yy + 1.15, nome, ha="left", va="center", fontsize=FS - 3, color=MID, fontweight="bold")
    ax.text(x0 + 6.5, ya + 0.5, "sessão de ana", ha="left", va="center", fontsize=FS - 4, color=ORANGE,
            family="monospace")
    if replicacao:
        ax.text(x0 + 6.5, yb + 0.5, "cópia da sessão", ha="left", va="center", fontsize=FS - 4, color=ORANGE,
                family="monospace")
        arrow(ax, (x0 + 5.45, 3.5), (x0 + 6.25, ya + 0.6), MID)
        arrow(ax, (x0 + 5.45, 2.9), (x0 + 6.25, yb + 0.9), MID)
        arrow(ax, (x0 + 8.6, ya - 0.05), (x0 + 8.6, yb + 1.6), ORANGE, estilo="<|-|>", ls=(0, (4, 3)))
        ax.text(x0 + 8.8, 3.2, "sincroniza", ha="left", va="center", fontsize=FS - 4, color=ORANGE, style="italic")
        nota = "qualquer servidor responde,\nmas é preciso copiar todas as sessões"
    else:
        ax.text(x0 + 6.5, yb + 0.5, "(não conhece ana)", ha="left", va="center", fontsize=FS - 4, color=GREY,
                family="monospace")
        arrow(ax, (x0 + 5.45, 3.5), (x0 + 6.25, ya + 0.6), MID)
        ax.text(x0 + 5.0, 4.75, "sempre\npara A", ha="center", va="center", fontsize=FS - 4, color=MID,
                style="italic", linespacing=1.15)
        nota = "simples, mas se A falhar a sessão perde-se\ne a carga não se reparte por igual"
    ax.text(x0, -0.35, nota, ha="left", va="center", fontsize=FS - 3, color=RED if not replicacao else ORANGE,
            style="italic", linespacing=1.25)


fig, ax = plt.subplots(figsize=(21, 7.8), dpi=200)
ax.set_xlim(0, 21)
ax.set_ylim(-1.0, 6.9)
ax.axis("off")
painel(ax, 0.2, "Sticky sessions", False)
painel(ax, 10.9, "Replicação de sessões", True)
ax.plot([10.4, 10.4], [-0.9, 6.8], color=GREY, lw=1.5, ls=(0, (2, 3)))

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
