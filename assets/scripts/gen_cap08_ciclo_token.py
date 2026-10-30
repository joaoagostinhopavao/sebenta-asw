"""Ciclo de vida de um JWT entre cliente e servidor: login, pedidos com o token, expiração e novo login
(Cap08 / Aula 08 da ASW).

Uso: python gen_cap08_ciclo_token.py <ficheiro_saida.png>
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

DARK = "#0a1420"
MID = "#0e6e8c"
LIGHT = "#eaf6f8"
ORANGE = "#d4651a"
RED = "#c0392b"
GREEN = "#218c4a"
GREY = "#9aa7ad"
FS = 18

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "ciclo_token.png"

XC, XS = 2.6, 13.4          # linhas de vida do cliente e do servidor
W, H = 18.0, 12.4


def box(ax, x0, y0, w, h, fc, ec, lw=2.2):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=2))


def badge(ax, x, y, n, color):
    ax.add_patch(plt.Circle((x, y), 0.24, color=color, zorder=5))
    ax.text(x, y, str(n), ha="center", va="center", fontsize=FS - 3, color="white", fontweight="bold", zorder=6)


def msg(ax, y, n, texto, color, para_servidor=True, sub=None):
    a, b = (XC, XS) if para_servidor else (XS, XC)
    ax.add_patch(FancyArrowPatch((a, y), (b, y), arrowstyle="-|>", mutation_scale=22, color=color, lw=2.6,
                                 zorder=3, shrinkA=0, shrinkB=0))
    xm = (XC + XS) / 2
    badge(ax, XC + 0.55 if para_servidor else XS - 0.55, y + 0.38, n, color)
    ax.text(xm, y + 0.38, texto, ha="center", va="center", fontsize=FS - 2, family="monospace", color=color,
            fontweight="bold")
    if sub:
        ax.text(xm, y - 0.36, sub, ha="center", va="center", fontsize=FS - 4, color=DARK, style="italic")


def nota(ax, y, texto, color=MID):
    ax.text(XS + 0.45, y, texto, ha="left", va="center", fontsize=FS - 3, color=color, style="italic",
            linespacing=1.25)


fig, ax = plt.subplots(figsize=(W, H), dpi=200)
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

for x, nome, sub in ((XC, "Cliente", "browser"), (XS, "Servidor", "API REST")):
    box(ax, x - 1.5, H - 1.35, 3.0, 1.15, LIGHT, MID)
    ax.text(x, H - 0.62, nome, ha="center", va="center", fontsize=FS + 1, color=DARK, fontweight="bold")
    ax.text(x, H - 1.02, sub, ha="center", va="center", fontsize=FS - 4, color=MID, style="italic")
    ax.plot([x, x], [0.3, H - 1.4], color=GREY, lw=2, ls=(0, (5, 4)), zorder=1)

msg(ax, 9.9, 1, "POST /login", MID, sub="utilizador e palavra-passe no corpo")
nota(ax, 9.9, "valida as credenciais (DAO)\ne gera o JWT, assinado")
msg(ax, 8.55, 2, "200 OK + JWT", GREEN, para_servidor=False, sub="o cliente guarda o token")
msg(ax, 7.0, 3, "GET /livros", MID, sub="Authorization: Bearer <JWT>")
nota(ax, 7.0, "verifica a assinatura e o exp,\nsem consultar sessão nenhuma")
msg(ax, 5.65, 4, "200 OK + JSON", GREEN, para_servidor=False)

ax.plot([0.4, W - 0.4], [4.75, 4.75], color=ORANGE, lw=1.8, ls=(0, (3, 3)), zorder=1)
ax.text((XC + XS) / 2, 4.95, "o tempo passa e o token expira (claim exp)", ha="center", va="bottom",
        fontsize=FS - 3, color=ORANGE, style="italic", fontweight="bold",
        bbox=dict(fc="white", ec="none", pad=2))

msg(ax, 3.75, 5, "GET /livros", MID, sub="Authorization: Bearer <JWT expirado>")
nota(ax, 3.75, "assinatura correta,\nmas o exp já passou", RED)
msg(ax, 2.4, 6, "401 Unauthorized", RED, para_servidor=False)
msg(ax, 1.05, 7, "POST /login", MID, sub="novo login, novo token")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
