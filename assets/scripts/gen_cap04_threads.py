"""Esquema "uma instância, vários threads" de uma Servlet (Cap04 / Aula 04 da ASW).

Uso: python gen_cap04_threads.py <ficheiro_saida.png>
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

out = sys.argv[1] if len(sys.argv) > 1 else "servlet-threads.png"


def box(ax, x, y, w, h, text, fc=DARK, tc="white", ec=None, fs=FS, bold=True, mono=False, lw=2.2, z=2):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec or fc, lw=lw, zorder=z))
    if text:
        ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=tc,
                fontweight="bold" if bold else "normal", zorder=3, linespacing=1.3,
                family="monospace" if mono else None)


def arrow(ax, x0, y0, x1, y1, color=DARK, rad=0.0, lw=2.4):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=20,
                                 color=color, lw=lw, connectionstyle=f"arc3,rad={rad}", zorder=1.5))


fig, ax = plt.subplots(figsize=(13, 6.4), dpi=200)
ax.set_xlim(0, 13)
ax.set_ylim(0, 6.4)
ax.set_aspect("equal")
ax.axis("off")

# Contentor
box(ax, 8.0, 3.1, 9.4, 5.6, None, fc=LIGHT, ec=MID, lw=2.0, z=0)
ax.text(3.55, 5.6, "Servlet Container (Tomcat)", fontsize=FS, color=MID, fontweight="bold", va="center")

# Instância única
ix, iy = 10.4, 3.1
box(ax, ix, iy, 3.6, 3.4, None, fc="white", ec=DARK, lw=2.6, z=1)
ax.text(ix, iy + 1.25, "uma só instância\nda Servlet", ha="center", va="center",
        fontsize=FS - 1, color=DARK, fontweight="bold", linespacing=1.3)
box(ax, ix, iy - 0.35, 2.8, 0.9, "service()", mono=True)
ax.text(ix, iy - 1.25, "→ doGet() / doPost()", ha="center", va="center", fontsize=FS - 3,
        color=MID, family="monospace")

# Pedidos e threads
ys = [4.7, 3.1, 1.5]
for k, yk in enumerate(ys, start=1):
    box(ax, 1.2, yk, 1.9, 0.85, f"Pedido {k}", fc=MID, fs=FS - 1)
    arrow(ax, 2.2, yk, 4.05, yk, color=DARK)
    box(ax, 5.1, yk, 2.0, 0.85, f"thread {k}", fc=DARK, fs=FS - 1)
    arrow(ax, 6.15, yk, ix - 1.85, iy + (yk - iy) * 0.35, color=ACCENT, lw=2.6)

ax.text(1.2, 0.45, "pedidos em simultâneo", ha="center", va="center", fontsize=FS - 2,
        color=DARK, style="italic")
ax.text(5.1, 0.45, "um thread por pedido", ha="center", va="center", fontsize=FS - 2,
        color=DARK, style="italic")
ax.text(ix, 0.45, "todos usam a mesma instância", ha="center", va="center", fontsize=FS - 2,
        color=DARK, style="italic")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
