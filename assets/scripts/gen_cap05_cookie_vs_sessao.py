"""Cookie (no cliente) e sessão (no servidor): onde fica cada coisa (Cap05 / Aula 05 da ASW).

Uso: python gen_cap05_cookie_vs_sessao.py <ficheiro_saida.png>
"""
import os
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "cookie-vs-sessao.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2, z=1):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=z))


fig, ax = plt.subplots(figsize=(13, 5.6), dpi=200)
ax.set_xlim(0, 13)
ax.set_ylim(0, 5.6)
ax.set_aspect("equal")
ax.axis("off")

# Cliente: browser com os cookies
box(ax, 0.3, 0.9, 4.6, 4.2, "white", DARK)
ax.add_patch(Rectangle((0.32, 4.55), 4.56, 0.53, fc=LIGHT, ec="none", zorder=2))
for k, c in enumerate(("#e06c5f", "#e8b54a", "#6cbf6c")):
    ax.add_patch(plt.Circle((0.62 + 0.28 * k, 4.81), 0.08, color=c, zorder=3))
ax.text(2.6, 4.1, "Cookies guardados", ha="center", va="center", fontsize=FS - 1, color=DARK, fontweight="bold")
box(ax, 0.7, 2.95, 3.8, 0.75, LIGHT, ORANGE, lw=2.2, z=2)
ax.text(2.6, 3.33, "JSESSIONID = A3F9", ha="center", va="center", fontsize=FS - 1, color=ORANGE,
        family="monospace", fontweight="bold", zorder=4)
box(ax, 0.7, 1.95, 3.8, 0.75, LIGHT, "#9aa7ad", lw=1.6, z=2)
ax.text(2.6, 2.33, "tema = escuro", ha="center", va="center", fontsize=FS - 2, color="#5f6b70",
        family="monospace", zorder=4)
ax.text(2.6, 1.3, "só o identificador", ha="center", va="center", fontsize=FS - 2, color=DARK, style="italic")
ax.text(2.6, 0.45, "Cliente", ha="center", va="center", fontsize=FS + 1, color=DARK, fontweight="bold")

# Servidor: a HttpSession com os dados
box(ax, 7.6, 0.9, 5.1, 4.2, LIGHT, MID, lw=2.0, z=0)
ax.text(10.15, 4.65, "HttpSession A3F9", ha="center", va="center", fontsize=FS, color=MID, fontweight="bold")
rows = (("utilizador", "\"ana\""), ("perfil", "\"aluno\""), ("carrinho", "[3 artigos]"))
for i, (k, v) in enumerate(rows):
    y = 3.75 - 0.78 * i
    box(ax, 7.95, y - 0.3, 4.4, 0.6, "white", MID, lw=1.6, z=2)
    ax.text(8.2, y, k, ha="left", va="center", fontsize=FS - 2, color=DARK, family="monospace", zorder=4)
    ax.text(12.1, y, v, ha="right", va="center", fontsize=FS - 2, color=ORANGE, family="monospace", zorder=4)
ax.text(10.15, 1.3, "os dados ficam aqui", ha="center", va="center", fontsize=FS - 2, color=DARK, style="italic")
ax.text(10.15, 0.45, "Servidor", ha="center", va="center", fontsize=FS + 1, color=MID, fontweight="bold")

# Ligação: o identificador aponta para a sessão
ax.add_patch(FancyArrowPatch((4.6, 3.33), (7.85, 4.65), arrowstyle="-|>", mutation_scale=22,
                             color=ORANGE, lw=2.6, zorder=3, connectionstyle="arc3,rad=-0.15"))
ax.text(6.2, 4.55, "a chave", ha="center", va="center", fontsize=FS - 2, color=ORANGE, style="italic")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
