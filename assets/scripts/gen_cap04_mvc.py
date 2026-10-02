"""Esquema MVC com Servlets: a View no cliente (JSON) ou no browser (HTML gerado por JSP).
Cap04 / Aula 04 da ASW.

Uso: python gen_cap04_mvc.py <ficheiro_saida.png>
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
ORANGE = "#d4651a"
FS = 15

out = sys.argv[1] if len(sys.argv) > 1 else "servlet-mvc.png"


def box(ax, x, y, w, h, text, fc=DARK, tc="white", ec=None, fs=FS, bold=True, lw=2.2, z=2):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec or fc, lw=lw, zorder=z))
    if text:
        ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=tc,
                fontweight="bold" if bold else "normal", zorder=z + 1, linespacing=1.3)


def arrow(ax, x0, y0, x1, y1, color=DARK, rad=0.0, lw=2.4, both=False):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="<|-|>" if both else "-|>",
                                 mutation_scale=20, color=color, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}", zorder=1.5))


def label(ax, x, y, text, color=MID, fs=FS - 2, style="italic", ha="center", bold=False):
    ax.text(x, y, text, ha=ha, va="center", fontsize=fs, color=color, style=style,
            fontweight="bold" if bold else "normal", linespacing=1.3, zorder=4)


fig, ax = plt.subplots(figsize=(15, 8), dpi=200)
ax.set_xlim(0, 15)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")

# Servidor
box(ax, 9.35, 3.95, 10.9, 7.5, None, fc=LIGHT, ec=MID, lw=2.0, z=0)
label(ax, 4.15, 7.35, "Servidor (Tomcat)", color=MID, style="normal", ha="left", bold=True, fs=FS)

# Clientes (as duas Views)
box(ax, 1.65, 6.0, 3.0, 1.6, "Cliente\n(página HTML + JS,\napp móvel, …)", fc="white", tc=DARK, ec=DARK, fs=FS - 2)
label(ax, 1.65, 7.25, "View no cliente:\nrecebe dados (JSON)", color=ORANGE, bold=True, style="normal")
box(ax, 1.65, 1.9, 3.0, 1.3, "Browser", fc="white", tc=DARK, ec=DARK, fs=FS - 1)
label(ax, 1.65, 0.75, "View no browser:\nrecebe a página (HTML)", color=ORANGE, bold=True, style="normal")

# Controller, JSP, Model, dados
sx, sy = 6.9, 4.4
box(ax, sx, sy, 2.8, 1.3, "Servlet\n(Controller)")
box(ax, sx, 1.9, 2.8, 1.2, "JSP\n(gera o HTML)", fc=MID)
box(ax, 10.3, sy, 2.4, 1.3, "Model\n(DAO)", fc="white", tc=DARK, ec=DARK)
box(ax, 13.45, sy, 1.9, 1.3, "Dados\n(lista, BD, …)", fc="white", tc=DARK, ec=MID, fs=FS - 2, bold=False)

# Caminho 1: cliente <-> Servlet, com JSON
arrow(ax, 3.2, 6.25, 5.45, 4.95, rad=-0.12)
label(ax, 4.55, 6.15, "pedido HTTP")
arrow(ax, 5.45, 4.65, 3.2, 5.75, color=ORANGE, rad=-0.12)
label(ax, 4.05, 4.85, "JSON", color=ORANGE, style="normal", bold=True)

# Caminho 2: browser -> Servlet -> JSP -> browser, com HTML
arrow(ax, 3.2, 2.2, 5.45, 3.85, rad=0.1)
label(ax, 4.05, 3.35, "pedido HTTP")
arrow(ax, sx, sy - 0.68, sx, 2.53)
label(ax, sx + 0.2, 3.15, "encaminha,\ncom os dados", ha="left")
arrow(ax, 5.47, 1.75, 3.2, 1.75, color=ORANGE)
label(ax, 4.3, 1.35, "HTML", color=ORANGE, style="normal", bold=True)

# Controller <-> Model <-> dados
arrow(ax, sx + 1.42, sy, 9.07, sy, both=True)
arrow(ax, 11.53, sy, 12.48, sy, both=True)

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
