"""Uma Servlet do ponto de vista do cliente: um destino de pedidos HTTP (Cap04 / Aula 04 da ASW).

Uso: python gen_cap04_servlet_http.py <ficheiro_saida.png>
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
ORANGE = "#d4651a"
FS = 15

out = sys.argv[1] if len(sys.argv) > 1 else "servlet-cliente.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2, z=1, ls="-"):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=z, ls=ls))


def arrow(ax, x0, y0, x1, y1, color):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=22,
                                 color=color, lw=2.8, zorder=3))


fig, ax = plt.subplots(figsize=(12, 5), dpi=200)
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.set_aspect("equal")
ax.axis("off")

# Browser (janela desenhada)
box(ax, 0.3, 0.9, 3.2, 2.9, "white", DARK)
ax.add_patch(Rectangle((0.32, 3.3), 3.16, 0.48, fc=LIGHT, ec="none", zorder=2))
for k, c in enumerate(("#e06c5f", "#e8b54a", "#6cbf6c")):
    ax.add_patch(plt.Circle((0.6 + 0.28 * k, 3.54), 0.08, color=c, zorder=3))
for y, w in ((2.75, 2.4), (2.35, 2.6), (1.95, 2.0), (1.55, 2.4)):
    ax.add_patch(Rectangle((0.6, y), w, 0.18, fc="#d7dde0", ec="none", zorder=2))
ax.text(1.9, 0.45, "Browser (cliente)", ha="center", va="center", fontsize=FS, color=DARK, fontweight="bold")

# Servidor com a Servlet
box(ax, 7.4, 0.3, 4.3, 4.3, LIGHT, MID, lw=2.0, z=0)
ax.text(9.55, 4.25, "Servidor (Tomcat)", ha="center", va="center", fontsize=FS - 1, color=MID, fontweight="bold")
box(ax, 8.0, 1.55, 3.1, 1.8, DARK, DARK, z=1)
ax.text(9.55, 2.7, "Servlet", ha="center", va="center", fontsize=FS + 1, color="white", fontweight="bold", zorder=4)
ax.text(9.55, 2.1, "uma classe Java", ha="center", va="center", fontsize=FS - 2, color=ACCENT, zorder=4)

# Pedido e resposta
arrow(ax, 3.7, 3.0, 7.9, 3.0, DARK)
ax.text(5.8, 3.35, "pedido HTTP", ha="center", va="center", fontsize=FS, color=DARK, style="italic")
arrow(ax, 7.9, 1.8, 3.7, 1.8, ORANGE)
ax.text(5.8, 1.45, "resposta HTTP", ha="center", va="center", fontsize=FS, color=ORANGE, style="italic")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
