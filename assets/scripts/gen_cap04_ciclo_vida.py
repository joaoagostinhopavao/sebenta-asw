"""Esquema do ciclo de vida de uma Servlet (Cap04 / Aula 04 da ASW).

Uso: python gen_cap04_ciclo_vida.py <ficheiro_saida.png>
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

DARK = "#0a1420"
MID = "#0e6e8c"
ACCENT = "#4dd0e1"
LIGHT = "#eaf6f8"
FS = 15

out = sys.argv[1] if len(sys.argv) > 1 else "servlet-ciclo-vida.png"


def box(ax, x, y, w, h, text, fc=DARK, tc="white", ec=None, fs=FS, bold=True, mono=False):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec or fc, lw=2.2, zorder=2))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=tc,
            fontweight="bold" if bold else "normal", zorder=3, linespacing=1.3,
            family="monospace" if mono else None)


def arrow(ax, x0, y0, x1, y1, color=DARK, rad=0.0, lw=2.4):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=20,
                                 color=color, lw=lw, connectionstyle=f"arc3,rad={rad}", zorder=1))


def note(ax, x, y, text, color=MID, fs=FS - 2, style="italic", ha="center"):
    ax.text(x, y, text, ha=ha, va="center", fontsize=fs, color=color, style=style, linespacing=1.3)


fig, ax = plt.subplots(figsize=(13, 6.2), dpi=200)
ax.set_xlim(0, 13)
ax.set_ylim(0, 6.2)
ax.set_aspect("equal")
ax.axis("off")

y = 3.6
xs = [1.5, 4.7, 8.0, 11.4]

# 1. Carregar
box(ax, xs[0], y, 2.9, 1.4, "Carregar a classe\ne criar a instância", fc=LIGHT, tc=DARK, ec=MID, fs=FS - 1)
note(ax, xs[0], y + 1.25, "1.º pedido\n(ou arranque do servidor)")

# 2. init
box(ax, xs[1], y, 2.2, 1.1, "init()", mono=True)
note(ax, xs[1], y + 1.15, "uma vez")
note(ax, xs[1], y - 1.15, "preparar recursos\n(ex.: ligação à BD)", color=DARK, style="normal")

# 3. service
box(ax, xs[2], y, 2.6, 1.1, "service()", mono=True)
note(ax, xs[2], y + 1.75, "uma vez por pedido HTTP,\nnum thread próprio")
arrow(ax, xs[2] + 0.75, y + 0.58, xs[2] - 0.75, y + 0.58, color=ACCENT, rad=1.1, lw=2.6)

# despacho por verbo
dy = y - 2.25
for dx, verbo, metodo in ((-1.25, "GET", "doGet()"), (1.25, "POST", "doPost()")):
    box(ax, xs[2] + dx, dy, 2.1, 0.8, metodo, fc=MID, mono=True, fs=FS - 1)
    arrow(ax, xs[2] + dx * 0.35, y - 0.55, xs[2] + dx, dy + 0.42, color=MID, lw=2.0)
    note(ax, xs[2] + dx * 0.72 + (0.35 if dx > 0 else -0.35), y - 1.05, verbo, color=MID, fs=FS - 3, style="normal")
note(ax, xs[2], dy - 0.75, "… consoante o verbo HTTP", color=DARK, style="normal", fs=FS - 3)

# 4. destroy
box(ax, xs[3], y, 2.2, 1.1, "destroy()", mono=True)
note(ax, xs[3], y + 1.25, "uma vez, ao desligar o servidor\nou retirar a aplicação")
note(ax, xs[3], y - 1.15, "libertar recursos", color=DARK, style="normal")

# setas principais
arrow(ax, xs[0] + 1.47, y, xs[1] - 1.12, y)
arrow(ax, xs[1] + 1.12, y, xs[2] - 1.32, y)
arrow(ax, xs[2] + 1.32, y, xs[3] - 1.12, y)

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
