"""Esquema "da mensagem HTTP aos objetos Java e de volta" (Cap04 / Aula 04 da ASW).

Uso: python gen_cap04_http_objetos.py <ficheiro_saida.png>
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
GREEN = "#2e8b57"
PAPER = "#f7f7f5"
FS = 14

out = sys.argv[1] if len(sys.argv) > 1 else "servlet-http-objetos.png"


def panel(ax, x0, y0, w, h, fc, ec, lw=2.0, z=1, dashed=False):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=fc, ec=ec, lw=lw, zorder=z, ls="--" if dashed else "-"))


def lines(ax, x0, ytop, items, fs=FS - 1, step=0.42, bold_first=False):
    for k, (txt, col) in enumerate(items):
        ax.text(x0, ytop - k * step, txt, fontsize=fs, color=col, family="monospace",
                va="center", ha="left", zorder=3,
                fontweight="bold" if (bold_first and k == 0) else "normal")


def arrow(ax, x0, y0, x1, y1, color=DARK, lw=2.6, rad=0.0):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=22,
                                 color=color, lw=lw, connectionstyle=f"arc3,rad={rad}", zorder=4))


def title(ax, x, y, txt, color=DARK, fs=FS, ha="left"):
    ax.text(x, y, txt, fontsize=fs, color=color, fontweight="bold", va="center", ha=ha, zorder=3)


fig, ax = plt.subplots(figsize=(15.6, 7.4), dpi=200)
ax.set_xlim(0, 15.6)
ax.set_ylim(0, 7.4)
ax.set_aspect("equal")
ax.axis("off")

# Contentor
panel(ax, 5.75, 0.15, 9.7, 6.85, LIGHT, MID, lw=2.0, z=0)
title(ax, 6.0, 6.7, "Servlet Container (Tomcat)", color=MID)

# --- Pedido HTTP (texto) ---
title(ax, 0.2, 6.7, "Pedido HTTP (texto)")
panel(ax, 0.15, 4.15, 5.25, 2.3, PAPER, DARK)
lines(ax, 0.35, 6.0, [
    ("GET /recurso?nome=valor HTTP/1.1", MID),
    ("Host: servidor:8080", DARK),
    ("Accept: application/json", ORANGE),
], fs=FS - 2)

# --- HttpServletRequest ---
panel(ax, 6.1, 4.15, 4.9, 2.3, "white", DARK, lw=2.4, z=1)
lines(ax, 6.3, 6.0, [
    ("HttpServletRequest request", DARK),
    ('getParameter("nome")', MID),
    ('   → "valor"', MID),
    ('getHeader("Accept")', ORANGE),
    ('   → "application/json"', ORANGE),
], fs=FS - 2, bold_first=True, step=0.38)

# --- Servlet ---
panel(ax, 11.75, 2.55, 3.4, 2.2, DARK, DARK, z=1)
ax.text(13.45, 4.25, "Servlet", fontsize=FS, color="white", fontweight="bold",
        ha="center", va="center", zorder=3)
ax.text(13.45, 3.35, "doGet(request,\nresponse)", fontsize=FS - 1, color=ACCENT,
        family="monospace", ha="center", va="center", zorder=3, linespacing=1.4)

# --- HttpServletResponse ---
panel(ax, 6.1, 0.45, 4.9, 2.05, "white", DARK, lw=2.4, z=1)
lines(ax, 6.3, 2.1, [
    ("HttpServletResponse response", DARK),
    ("setStatus(200)", GREEN),
    ('setContentType("application/json")', ORANGE),
    ("getWriter().print(corpo)", MID),
], fs=FS - 2, bold_first=True)

# --- Resposta HTTP (texto) ---
title(ax, 0.2, 2.85, "Resposta HTTP (texto)")
panel(ax, 0.15, 0.45, 5.25, 2.05, PAPER, DARK)
lines(ax, 0.35, 2.1, [
    ("HTTP/1.1 200 OK", GREEN),
    ("Content-Type: application/json", ORANGE),
    ("", DARK),
    ('{ … corpo da resposta … }', MID),
], fs=FS - 2)

# Setas
arrow(ax, 5.45, 5.4, 6.05, 5.4)
arrow(ax, 11.05, 5.35, 12.3, 4.8, rad=-0.15)
arrow(ax, 12.3, 2.5, 11.05, 1.6, rad=-0.15)
arrow(ax, 6.05, 1.45, 5.45, 1.45)

ax.text(8.55, 3.42, "o contentor converte\ntexto ⇄ objetos Java", fontsize=FS - 1, color=MID,
        style="italic", ha="center", va="center", linespacing=1.3)

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
