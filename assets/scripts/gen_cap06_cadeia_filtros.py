"""Esquema da cadeia de Filtros antes da Servlet (Cap06 / Aula 06 da ASW).

Uso: python gen_cap06_cadeia_filtros.py <ficheiro_saida.png>
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
RED = "#c0392b"
YELLOW = "#e0a800"
GREEN = "#218c4b"
FS = 17

out = sys.argv[1] if len(sys.argv) > 1 else "Filter_Chain.png"


def box(ax, x, y, w, h, text, fc, tc=DARK, ec=DARK, lw=2.6, fs=FS, z=2):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.18",
                                fc=fc, ec=ec, lw=lw, zorder=z))
    if text:
        ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=tc,
                fontweight="bold", zorder=3, linespacing=1.25)


def arrow(ax, x0, y0, x1, y1, color):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=22,
                                 color=color, lw=3, zorder=2))


fig, ax = plt.subplots(figsize=(14, 7.2), dpi=200)
ax.set_xlim(0, 14)
ax.set_ylim(0, 7.2)
ax.set_aspect("equal")
ax.axis("off")

# Contentor
ax.add_patch(FancyBboxPatch((4.0, 2.35), 9.8, 3.9, boxstyle="round,pad=0.02,rounding_size=0.25",
                            fc=LIGHT, ec=MID, lw=2.2, ls="--", zorder=0))
ax.text(8.9, 5.9, "Servlet Container (Tomcat)", ha="center", va="center", fontsize=FS,
        color=MID, fontweight="bold", style="italic")

yc = 4.2
xs = {"cliente": 1.3, "f1": 5.45, "dots": 7.35, "fn": 9.25, "servlet": 12.15}
box(ax, xs["cliente"], yc, 2.3, 1.6, "Cliente", "white")
box(ax, xs["f1"], yc, 2.1, 1.6, "Filtro 1", "white", ec=MID)
ax.text(xs["dots"], yc, "…", ha="center", va="center", fontsize=FS + 10, color=MID, fontweight="bold")
box(ax, xs["fn"], yc, 2.1, 1.6, "Filtro N", "white", ec=MID)
box(ax, xs["servlet"], yc, 2.6, 1.6, "Servlet\n(lógica de\nnegócio)", ACCENT, fs=FS - 1)

# Pedido (em cima) e resposta (em baixo)
yp, yr = yc + 0.4, yc - 0.4
for a, b in [("cliente", "f1"), ("f1", "dots"), ("dots", "fn"), ("fn", "servlet")]:
    wa = {"cliente": 1.15, "f1": 1.05, "dots": 0.35, "fn": 1.05, "servlet": 1.3}
    arrow(ax, xs[a] + wa[a] + 0.05, yp, xs[b] - wa[b] - 0.05, yp, MID)
    arrow(ax, xs[b] - wa[b] - 0.05, yr, xs[a] + wa[a] + 0.05, yr, DARK)
ax.text(3.2, yp + 0.15, "pedido", ha="center", va="bottom", fontsize=FS - 3, color=MID, fontweight="bold")
ax.text(3.2, yr - 0.15, "resposta", ha="center", va="top", fontsize=FS - 3, color=DARK, fontweight="bold")
ax.text(xs["dots"], yc + 1.15, "chain.doFilter()", ha="center", va="center", fontsize=FS - 3,
        color=MID, family="monospace")

# Legenda: os três comportamentos de um Filtro
legenda = [
    (RED, "Bloquear o pedido (400 / 401 / 403)"),
    (YELLOW, "Modificar o pedido (validação, logging, …)"),
    (GREEN, "Deixar prosseguir: chain.doFilter()"),
]
for k, (cor, texto) in enumerate(legenda):
    yk = 1.65 - 0.62 * k
    ax.add_patch(plt.Circle((1.0, yk), 0.2, color=cor, zorder=3))
    ax.text(1.45, yk, texto, ha="left", va="center", fontsize=FS - 1, color=DARK)

fig.savefig(out, bbox_inches="tight", pad_inches=0.15, facecolor="white")
print("gravado:", out)
