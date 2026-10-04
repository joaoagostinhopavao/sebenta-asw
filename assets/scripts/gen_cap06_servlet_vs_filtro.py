"""Esquema "só Servlets" vs. "Servlet + Filtro" (Cap06 / Aula 06 da ASW).

Uso: python gen_cap06_servlet_vs_filtro.py <ficheiro_saida.png>
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

DARK = "#0a1420"
MID = "#0e6e8c"
ACCENT = "#4dd0e1"
ORANGE = "#e08a2e"
FS = 19

out = sys.argv[1] if len(sys.argv) > 1 else "Servlet_vs_Filter.png"


def rbox(ax, x, y, w, h, fc, z=1):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=fc, ec=fc, zorder=z))


def coluna(ax, x0, titulo, blocos):
    w = 6.2
    rbox(ax, x0, 6.2, w, 0.95, MID)
    ax.text(x0 + w / 2, 6.675, titulo, ha="center", va="center", fontsize=FS + 4,
            color="white", fontweight="bold")
    rbox(ax, x0, 0.9, w, 5.1, DARK)
    y = 5.45
    for cabecalho, itens in blocos:
        ax.text(x0 + w / 2, y, cabecalho, ha="center", va="center", fontsize=FS,
                color="white", fontweight="bold")
        y -= 0.62
        for item in itens:
            ax.text(x0 + w / 2, y, item, ha="center", va="center", fontsize=FS - 1, color=ACCENT)
            y -= 0.5
        y -= 0.35


fig, ax = plt.subplots(figsize=(14, 7.6), dpi=200)
ax.set_xlim(0, 14)
ax.set_ylim(0, 7.6)
ax.set_aspect("equal")
ax.axis("off")

coluna(ax, 0.5, "Só Servlets", [
    ("Em cada Servlet:", ["autenticação", "logging", "validação", "lógica de negócio"]),
])
coluna(ax, 7.3, "Servlet + Filtro", [
    ("Num só Filtro:", ["autenticação", "logging", "validação"]),
    ("Em cada Servlet:", ["lógica de negócio"]),
])

# Selo DRY
rbox(ax, 12.35, 6.75, 1.45, 0.7, ORANGE, z=3)
ax.text(13.075, 7.1, "DRY", ha="center", va="center", fontsize=FS, color="white",
        fontweight="bold", zorder=4)

ax.text(7.0, 0.35, "E se for preciso mudar a lógica de autenticação em 15 Servlets?",
        ha="center", va="center", fontsize=FS - 1, color=DARK, style="italic")

fig.savefig(out, bbox_inches="tight", pad_inches=0.15, facecolor="white")
print("gravado:", out)
