"""Esquema do modelo cliente-servidor (Cap01 e Cap03 / Aula 03 da ASW).

Uso: python gen_cap01_cliente_servidor.py <ficheiro_saida.png>
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

DARK = "#0a1420"
MID = "#0e6e8c"
ACCENT = "#4dd0e1"
LIGHT = "#eaf6f8"
ORANGE = "#e08a2e"
FS = 17

out = sys.argv[1] if len(sys.argv) > 1 else "Modelo_cliente_servidor.png"


def box(ax, x, y, w, h, fc, ec, lw=2.4, z=1):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.2",
                                fc=fc, ec=ec, lw=lw, zorder=z))


def arrow(ax, x0, y0, x1, y1, color):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=26,
                                 color=color, lw=3.2, zorder=2))


fig, ax = plt.subplots(figsize=(14, 5.6), dpi=200)
ax.set_xlim(0, 14)
ax.set_ylim(0, 5.6)
ax.set_aspect("equal")
ax.axis("off")

# Cliente: um browser desenhado (janela com barra de endereço)
cx, cy = 2.4, 2.6
box(ax, cx, cy, 3.6, 3.4, "white", DARK, lw=2.6)
ax.add_patch(Rectangle((cx - 1.4, cy - 0.9), 2.8, 2.0, fc=LIGHT, ec=MID, lw=2, zorder=2))
ax.add_patch(Rectangle((cx - 1.4, cy + 0.75), 2.8, 0.35, fc=MID, ec=MID, lw=2, zorder=3))
for k in range(3):
    ax.add_patch(plt.Circle((cx - 1.2 + 0.22 * k, cy + 0.925), 0.07, color="white", zorder=4))
for k, w in enumerate([2.2, 1.6, 1.9]):
    ax.add_patch(Rectangle((cx - 1.15, cy + 0.35 - 0.4 * k), w, 0.16, fc=ACCENT, ec="none", zorder=3))
ax.text(cx, cy + 2.15, "Cliente", ha="center", va="center", fontsize=FS + 3, color=DARK, fontweight="bold")
ax.text(cx, cy - 1.35, "por exemplo, um browser", ha="center", va="center", fontsize=FS - 3,
        color=MID, style="italic")

# Servidor: um rack simples
sx, sy = 11.6, 2.6
box(ax, sx, sy, 3.6, 3.4, "white", DARK, lw=2.6)
for k in range(3):
    yk = sy + 0.75 - 0.75 * k
    ax.add_patch(FancyBboxPatch((sx - 1.3, yk - 0.25), 2.6, 0.5,
                                boxstyle="round,pad=0.01,rounding_size=0.08",
                                fc=DARK, ec=DARK, zorder=2))
    ax.add_patch(plt.Circle((sx + 0.95, yk), 0.08, color=ACCENT, zorder=3))
    ax.add_patch(Rectangle((sx - 1.1, yk - 0.05), 1.3, 0.1, fc=MID, ec="none", zorder=3))
ax.text(sx, sy + 2.15, "Servidor", ha="center", va="center", fontsize=FS + 3, color=DARK, fontweight="bold")
ax.text(sx, sy - 1.35, "por exemplo, o Tomcat", ha="center", va="center", fontsize=FS - 3,
        color=MID, style="italic")

# Pedido e resposta
arrow(ax, 4.5, 3.25, 9.5, 3.25, MID)
ax.text(7.0, 3.6, "pedido HTTP (request)", ha="center", va="center", fontsize=FS, color=MID,
        fontweight="bold")
arrow(ax, 9.5, 1.95, 4.5, 1.95, ORANGE)
ax.text(7.0, 1.6, "resposta HTTP (response)", ha="center", va="center", fontsize=FS, color=ORANGE,
        fontweight="bold")

fig.savefig(out, bbox_inches="tight", pad_inches=0.15, facecolor="white")
print("gravado:", out)
