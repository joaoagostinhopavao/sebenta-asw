"""Aplicação Web (MVC) vs. API REST: onde fica a View (Cap07 / Aula 07 da ASW).

Uso: python gen_cap07_mvc_vs_rest.py <ficheiro_saida.png>
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

DARK = "#0a1420"
MID = "#0e6e8c"
ACCENT = "#4dd0e1"
LIGHT = "#eaf6f8"
ORANGE = "#d4651a"
GREY = "#9aa7ad"
FS = 15

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "mvc-vs-rest.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2, z=1, ls="-"):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=z, linestyle=ls))


def arrow(ax, p, q, color, label, side):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=22, color=color, lw=2.6, zorder=3))
    xm = (p[0] + q[0]) / 2
    ym = (p[1] + q[1]) / 2
    ax.text(xm + side, ym, label, ha="left" if side > 0 else "right", va="center",
            fontsize=FS - 1, color=color, fontweight="bold")


def piece(ax, x, y, w, text, fc, ec, tc, ls="-"):
    box(ax, x, y, w, 0.62, fc, ec, lw=1.8, z=2, ls=ls)
    ax.text(x + w / 2, y + 0.31, text, ha="center", va="center", fontsize=FS - 2, color=tc, zorder=4)


fig, ax = plt.subplots(figsize=(13, 7.4), dpi=200)
ax.set_xlim(0, 13)
ax.set_ylim(0, 7.4)
ax.set_aspect("equal")
ax.axis("off")

for x0, title in ((0.2, "Aplicação Web (MVC)"), (6.8, "API REST")):
    ax.text(x0 + 3.0, 7.05, title, ha="center", va="center", fontsize=FS + 2, color=DARK, fontweight="bold")
    # servidor
    box(ax, x0, 3.9, 6.0, 2.75, LIGHT, MID, lw=2.0, z=0)
    ax.text(x0 + 0.25, 6.3, "Servidor", ha="left", va="center", fontsize=FS, color=MID, fontweight="bold")
    piece(ax, x0 + 0.3, 5.2, 2.6, "Controller (Servlet)", "white", MID, DARK)
    piece(ax, x0 + 3.1, 5.2, 2.6, "Model (DAO)", "white", MID, DARK)
    # cliente
    box(ax, x0, 0.35, 6.0, 1.9, "white", DARK, lw=2.2, z=0)
    ax.text(x0 + 0.25, 1.95, "Cliente", ha="left", va="center", fontsize=FS, color=DARK, fontweight="bold")

# MVC: a View vive no servidor e gera HTML
piece(ax, 0.5, 4.25, 5.4, "View (JSP): gera a página HTML", ACCENT, DARK, DARK)
ax.text(3.2, 1.05, "o browser mostra o HTML recebido", ha="center", va="center",
        fontsize=FS - 1, color=DARK, style="italic")
arrow(ax, (2.0, 2.35), (2.0, 3.8), MID, "pedido", -0.15)
arrow(ax, (4.4, 3.8), (4.4, 2.35), ORANGE, "HTML", 0.15)

# REST: não há View no servidor; o cliente desenha a página
piece(ax, 7.1, 4.25, 5.4, "sem View no servidor", "white", GREY, GREY, ls="--")
piece(ax, 7.1, 0.85, 5.4, "View (JavaScript): desenha a página", ACCENT, DARK, DARK)
arrow(ax, (8.6, 2.35), (8.6, 3.8), MID, "pedido", -0.15)
arrow(ax, (11.0, 3.8), (11.0, 2.35), ORANGE, "JSON", 0.15)

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
