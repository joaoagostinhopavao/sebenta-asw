"""JWT numa aplicação repartida por microsserviços: um login no serviço de autenticação e o mesmo token
aceite pelos outros serviços, cada um a validá-lo sozinho (Cap08 / Aula 08 da ASW).

Uso: python gen_cap08_microsservicos.py <ficheiro_saida.png>
"""
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

DARK = "#0a1420"
MID = "#0e6e8c"
LIGHT = "#eaf6f8"
ORANGE = "#d4651a"
GREEN = "#218c4a"
GREY = "#9aa7ad"
FS = 18

out = sys.argv[1] if len(sys.argv) > 1 else "microsservicos.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2, ls="-"):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=2, linestyle=ls))


def arrow(ax, p, q, color, lw=2.6):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=22, color=color, lw=lw, zorder=3,
                                 shrinkA=0, shrinkB=0))


def servico(ax, y, nome, endpoint, nota, cor):
    box(ax, 9.6, y, 5.6, 1.7, "white", cor)
    ax.text(9.85, y + 1.25, nome, ha="left", va="center", fontsize=FS - 1, color=cor, fontweight="bold")
    ax.text(9.85, y + 0.45, nota, ha="left", va="center", fontsize=FS - 4, color=DARK, style="italic")
    return endpoint


fig, ax = plt.subplots(figsize=(19, 9.4), dpi=200)
ax.set_xlim(0, 19)
ax.set_ylim(-0.6, 8.8)
ax.axis("off")

# cliente
box(ax, 0.2, 3.3, 2.6, 1.6, "white", DARK)
ax.text(1.5, 4.25, "Cliente", ha="center", va="center", fontsize=FS, color=DARK, fontweight="bold")
ax.text(1.5, 3.75, "guarda o token", ha="center", va="center", fontsize=FS - 5, color=GREY, style="italic")

# os três serviços
box(ax, 9.2, -0.45, 6.4, 8.55, "none", GREY, lw=1.6, ls=(0, (4, 3)))
ax.text(12.4, 8.4, "no mesmo servidor (portas diferentes) ou em servidores diferentes", ha="center",
        va="center", fontsize=FS - 5, color=GREY, style="italic")
servico(ax, 6.0, "Serviço de autenticação", "", "valida as credenciais e emite o JWT", ORANGE)
servico(ax, 3.05, "Serviço de livros", "", "valida o token sozinho", GREEN)
servico(ax, 0.1, "Serviço de encomendas", "", "valida o token sozinho", GREEN)

# pedidos
arrow(ax, (2.9, 4.75), (9.5, 7.0), ORANGE)
ax.text(5.6, 6.35, "1  POST /login", ha="center", va="center", fontsize=FS - 3, color=ORANGE, family="monospace",
        fontweight="bold", rotation=17)
arrow(ax, (9.5, 6.55), (2.9, 4.45), ORANGE)
ax.text(6.9, 5.15, "2  JWT", ha="center", va="center", fontsize=FS - 3, color=ORANGE, family="monospace",
        fontweight="bold", rotation=17)
arrow(ax, (2.9, 4.0), (9.5, 3.9), GREEN)
ax.text(6.2, 4.3, "3  GET /livros + o mesmo JWT", ha="center", va="center", fontsize=FS - 4, color=GREEN,
        family="monospace", fontweight="bold")
arrow(ax, (2.9, 3.6), (9.5, 0.95), GREEN)
ax.text(5.9, 1.75, "4  POST /encomendas + o mesmo JWT", ha="center", va="center", fontsize=FS - 4, color=GREEN,
        family="monospace", fontweight="bold", rotation=-21)

ax.text(15.9, 3.9, "nenhum serviço\npergunta ao de\nautenticação: basta\nverificar a assinatura", ha="left",
        va="center", fontsize=FS - 4, color=GREEN, style="italic", linespacing=1.25)

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
