"""Filtro de autenticação por sessão vs. por JWT, lado a lado: a mesma estrutura, só muda a verificação
(Cap08 / Aula 08 da ASW).

Uso: python gen_cap08_filtros.py <ficheiro_saida.png>
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon

DARK = "#0a1420"
MID = "#0e6e8c"
LIGHT = "#eaf6f8"
ORANGE = "#d4651a"
RED = "#c0392b"
GREEN = "#218c4a"
GREY = "#5f6b70"
FS = 18

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "filtros.png"


def box(ax, xc, yc, w, h, txt, fc, ec, cor=DARK, mono=False, bold=False):
    ax.add_patch(FancyBboxPatch((xc - w / 2, yc - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=2.2, zorder=2))
    ax.text(xc, yc, txt, ha="center", va="center", fontsize=FS - 3, color=cor, linespacing=1.2,
            family="monospace" if mono else None, fontweight="bold" if bold else "normal", zorder=3)


def losango(ax, xc, yc, w, h, txt, cor):
    ax.add_patch(Polygon([(xc, yc + h / 2), (xc + w / 2, yc), (xc, yc - h / 2), (xc - w / 2, yc)], closed=True,
                         fc="white", ec=cor, lw=2.2, zorder=2))
    ax.text(xc, yc, txt, ha="center", va="center", fontsize=FS - 4, color=DARK, linespacing=1.2, zorder=3)


def seta(ax, p, q, cor=DARK, txt=None, lado="right"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=20, color=cor, lw=2.3, zorder=1,
                                 shrinkA=0, shrinkB=0))
    if txt:
        xm, ym = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        if lado == "center":
            ax.text(xm, ym + 0.1, txt, ha="center", va="bottom", fontsize=FS - 4, color=cor, fontweight="bold")
        else:
            ax.text(xm + 0.18, ym + 0.12, txt, ha="left", va="bottom", fontsize=FS - 4, color=cor, fontweight="bold")


def coluna(ax, x, titulo, passos, cor):
    ax.text(x, 10.55, titulo, ha="center", va="center", fontsize=FS + 1, color=cor, fontweight="bold")
    box(ax, x, 9.6, 3.6, 0.8, "pedido HTTP", "white", DARK, bold=True)
    y = 9.2
    for k, (pergunta, falha) in enumerate(passos):
        yc = y - 1.55
        seta(ax, (x, y), (x, yc + 0.85), txt="sim" if k else None)
        losango(ax, x, yc, 5.0, 1.7, pergunta, cor)
        seta(ax, (x + 2.5, yc), (x + 3.7, yc), RED, "não", lado="center")
        box(ax, x + 4.45, yc, 1.4, 0.75, "401", "#fbe9e7", RED, cor=RED, bold=True)
        if falha:
            ax.text(x + 4.45, yc - 0.6, falha, ha="center", va="top", fontsize=FS - 7, color=RED, style="italic")
        y = yc - 0.85
    seta(ax, (x, y), (x, y - 0.75), GREEN, "sim")
    box(ax, x, y - 1.15, 4.4, 0.8, "chain.doFilter()", LIGHT, GREEN, cor=GREEN, mono=True, bold=True)
    seta(ax, (x, y - 1.55), (x, y - 2.05), GREEN)
    box(ax, x, y - 2.45, 3.6, 0.8, "Servlet", "white", GREEN, cor=GREEN, bold=True)


fig, ax = plt.subplots(figsize=(19, 11.4), dpi=200)
ax.set_xlim(0, 19)
ax.set_ylim(-0.7, 11.0)
ax.axis("off")

coluna(ax, 3.4, "Filtro por sessão", [
    ("existe sessão com\n\"utilizador\"?", ""),
], MID)
coluna(ax, 12.6, "Filtro por JWT", [
    ("Authorization começa\npor \"Bearer \"?", ""),
    ("assinatura e exp\nválidas? (JJWT)", "token forjado\nou expirado"),
], ORANGE)
ax.plot([8.9, 8.9], [0.3, 10.9], color="#c9d3d6", lw=1.5, ls=(0, (2, 3)))
ax.text(9.5, -0.2, "a mesma estrutura: verificar → 401 ou chain.doFilter(); só muda a verificação", ha="center",
        va="center", fontsize=FS - 4, color=GREY, style="italic")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
