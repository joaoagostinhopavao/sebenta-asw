"""Dois servidores atrás de um balanceador: com sessão vs. sem estado (Cap07 / Aula 07 da ASW).

Uso: python gen_cap07_instancias.py <ficheiro_saida.png> [--sem-estado]
     --sem-estado: só a metade de baixo (usada na Aula 08)
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
RED = "#c0392b"
GREEN = "#218c4a"
GREY = "#9aa7ad"
FS = 15

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "instancias.png"
SO_SEM_ESTADO = "--sem-estado" in sys.argv


def box(ax, x0, y0, w, h, fc, ec, lw=2.2, z=1):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=z))


def arrow(ax, p, q, color, rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=20, color=color, lw=2.4, zorder=3,
                                 connectionstyle=f"arc3,rad={rad}"))


def badge(ax, x, y, n, color):
    ax.add_patch(plt.Circle((x, y), 0.22, color=color, zorder=5))
    ax.text(x, y, str(n), ha="center", va="center", fontsize=FS - 3, color="white", fontweight="bold", zorder=6)


def row(ax, y0, title, stateful):
    ax.text(0.2, y0 + 4.05, title, ha="left", va="center", fontsize=FS + 1, color=DARK, fontweight="bold")
    # cliente
    box(ax, 0.2, y0 + 1.1, 2.4, 1.6, "white", DARK)
    ax.text(1.4, y0 + 1.9, "Cliente", ha="center", va="center", fontsize=FS, color=DARK, fontweight="bold")
    # balanceador
    box(ax, 4.0, y0 + 1.1, 2.6, 1.6, LIGHT, MID)
    ax.text(5.3, y0 + 2.1, "Balanceador", ha="center", va="center", fontsize=FS - 1, color=MID, fontweight="bold")
    ax.text(5.3, y0 + 1.6, "distribui os pedidos", ha="center", va="center", fontsize=FS - 4, color=DARK,
            style="italic")
    # instâncias
    for k, (yy, name) in enumerate(((y0 + 2.35, "Servidor A"), (y0 + 0.05, "Servidor B"))):
        box(ax, 9.6, yy, 4.4, 1.4, "white", MID, lw=2.0)
        ax.text(9.85, yy + 1.05, name, ha="left", va="center", fontsize=FS - 1, color=MID, fontweight="bold")
        if stateful and k == 0:
            txt, col = "sessão: utilizador = \"ana\"", ORANGE
        elif k == 0:
            txt, col = "sem sessão (emite o token)", GREY
        else:
            txt, col = "sem sessão", GREY
        ax.text(9.85, yy + 0.45, txt, ha="left", va="center", fontsize=FS - 3, color=col, family="monospace")
    # pedidos
    arrow(ax, (2.7, y0 + 2.3), (3.9, y0 + 2.3), MID)
    arrow(ax, (6.7, y0 + 2.3), (9.5, y0 + 3.05), MID)
    badge(ax, 7.1, y0 + 3.0, 1, MID)
    ax.text(7.45, y0 + 3.0, "login", ha="left", va="center", fontsize=FS - 3, color=MID,
            family="monospace")
    arrow(ax, (6.7, y0 + 1.5), (9.5, y0 + 0.75), MID)
    badge(ax, 7.1, y0 - 0.12, 2, MID)
    if stateful:
        ax.text(7.45, y0 - 0.12, "GET /livros", ha="left", va="center", fontsize=FS - 3, color=MID,
                family="monospace")
        res, col, note = "401", RED, "B não conhece a sessão criada em A"
    else:
        ax.text(7.45, y0 - 0.12, "GET /livros + token", ha="left", va="center", fontsize=FS - 3, color=MID,
                family="monospace")
        res, col, note = "200", GREEN, "o próprio pedido traz o token"
    ax.text(14.25, y0 + 0.95, res, ha="left", va="center", fontsize=FS + 3, color=col, fontweight="bold")
    ax.text(14.25, y0 + 0.4, note, ha="left", va="center", fontsize=FS - 4, color=col, style="italic")


if SO_SEM_ESTADO:
    fig, ax = plt.subplots(figsize=(18.6, 5.0), dpi=200)
    ax.set_ylim(-0.4, 4.6)
else:
    fig, ax = plt.subplots(figsize=(18.6, 9.8), dpi=200)
    ax.set_ylim(-0.4, 9.4)
ax.set_xlim(0, 18.6)
ax.set_aspect("equal")
ax.axis("off")

if not SO_SEM_ESTADO:
    row(ax, 4.9, "Com sessão no servidor (stateful)", True)
row(ax, 0.2, "Sem estado no servidor (stateless)", False)

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
