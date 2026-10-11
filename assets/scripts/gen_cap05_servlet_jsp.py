"""MVC com Servlet e JSP: o percurso de um pedido até ao HTML gerado (Cap05 / Aula 05 da ASW).

Uso: python gen_cap05_servlet_jsp.py <ficheiro_saida.png>
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

out = sys.argv[1] if len(sys.argv) > 1 else "servlet-jsp.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2, z=1):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=z))


def arrow(ax, x0, y0, x1, y1, color):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=22,
                                 color=color, lw=2.8, zorder=3))


def step(ax, x, y, n, color):
    ax.add_patch(plt.Circle((x, y), 0.25, color=color, zorder=4))
    ax.text(x, y, str(n), ha="center", va="center", fontsize=FS - 1, color="white", fontweight="bold", zorder=5)


def comp(ax, x0, y0, w, h, title, role):
    box(ax, x0, y0, w, h, DARK, DARK, z=1)
    ax.text(x0 + w / 2, y0 + h * 0.62, title, ha="center", va="center", fontsize=FS + 1, color="white",
            fontweight="bold", zorder=4)
    ax.text(x0 + w / 2, y0 + h * 0.27, role, ha="center", va="center", fontsize=FS - 2, color=ACCENT, zorder=4)


fig, ax = plt.subplots(figsize=(14, 6.4), dpi=200)
ax.set_xlim(0, 14)
ax.set_ylim(0, 6.4)
ax.set_aspect("equal")
ax.axis("off")

# Browser
box(ax, 0.2, 1.7, 2.6, 2.6, "white", DARK)
ax.add_patch(Rectangle((0.22, 3.85), 2.56, 0.43, fc=LIGHT, ec="none", zorder=2))
for k, c in enumerate(("#e06c5f", "#e8b54a", "#6cbf6c")):
    ax.add_patch(plt.Circle((0.48 + 0.26 * k, 4.06), 0.07, color=c, zorder=3))
for yy, w in ((3.3, 2.0), (2.9, 1.6), (2.5, 1.9)):
    ax.add_patch(Rectangle((0.45, yy), w, 0.16, fc="#d7dde0", ec="none", zorder=2))
ax.text(1.5, 1.25, "Browser", ha="center", va="center", fontsize=FS, color=DARK, fontweight="bold")

# Servidor
box(ax, 5.0, 0.25, 8.8, 5.9, LIGHT, MID, lw=2.0, z=0)
ax.text(9.4, 5.8, "Servidor (Tomcat)", ha="center", va="center", fontsize=FS - 1, color=MID, fontweight="bold")
comp(ax, 5.6, 3.6, 3.0, 1.6, "Servlet", "Controller")
comp(ax, 10.4, 3.6, 3.0, 1.6, "DAO", "Model")
comp(ax, 5.6, 0.7, 3.0, 1.6, "perfil.jsp", "View")

# 1: pedido
arrow(ax, 2.9, 3.9, 5.5, 4.4, DARK)
step(ax, 4.1, 4.6, 1, DARK)
ax.text(3.2, 5.2, "GET /perfil", ha="left", va="center", fontsize=FS - 2, color=DARK, family="monospace")

# 2: consulta o Model
arrow(ax, 8.7, 4.65, 10.3, 4.65, DARK)
arrow(ax, 10.3, 4.15, 8.7, 4.15, MID)
step(ax, 9.5, 5.1, 2, DARK)
ax.text(9.5, 3.75, "dados", ha="center", va="center", fontsize=FS - 2, color=MID, style="italic")

# 3: forward para a JSP com o atributo no pedido
arrow(ax, 7.1, 3.5, 7.1, 2.4, ORANGE)
step(ax, 6.6, 2.95, 3, ORANGE)
ax.text(7.35, 3.12, "request.setAttribute(…)", ha="left", va="center", fontsize=FS - 3, color=ORANGE,
        family="monospace")
ax.text(7.35, 2.72, "forward(request, response)", ha="left", va="center", fontsize=FS - 3, color=ORANGE,
        family="monospace")

# 4: HTML gerado volta ao browser
arrow(ax, 5.5, 1.5, 2.9, 2.2, ORANGE)
step(ax, 4.1, 1.45, 4, ORANGE)
ax.text(3.2, 0.75, "HTML gerado", ha="left", va="center", fontsize=FS - 2, color=ORANGE, style="italic")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
