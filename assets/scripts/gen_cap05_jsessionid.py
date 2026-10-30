"""Como o cookie JSESSIONID liga pedidos sucessivos à mesma sessão (Cap05 / Aula 05 da ASW).

Uso: python gen_cap05_jsessionid.py <ficheiro_saida.png>
"""
import os
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from traduzir_figura import ativar  # noqa: E402
ativar(__file__)                     # --en: textos em inglês (assets/scripts/en/)
out = sys.argv[1] if len(sys.argv) > 1 else "sessao-jsessionid.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2, z=1):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=z))


def arrow(ax, x0, y0, x1, y1, color):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=22,
                                 color=color, lw=2.8, zorder=3))


def step(ax, x, y, n, color):
    ax.add_patch(plt.Circle((x, y), 0.27, color=color, zorder=4))
    ax.text(x, y, str(n), ha="center", va="center", fontsize=FS, color="white", fontweight="bold", zorder=5)


fig, ax = plt.subplots(figsize=(13, 8.6), dpi=200)
ax.set_xlim(0, 13)
ax.set_ylim(0, 8.6)
ax.set_aspect("equal")
ax.axis("off")

XB, XS = 1.6, 8.0  # linhas de vida do browser e do servidor

# Cabeçalhos
box(ax, 0.3, 7.5, 2.6, 0.85, DARK, DARK)
ax.text(XB, 7.92, "Browser", ha="center", va="center", fontsize=FS + 1, color="white", fontweight="bold", zorder=4)
box(ax, 6.7, 7.5, 2.6, 0.85, DARK, DARK)
ax.text(XS, 7.92, "Servidor", ha="center", va="center", fontsize=FS + 1, color="white", fontweight="bold", zorder=4)
for x in (XB, XS):
    ax.plot([x, x], [0.3, 7.45], color="#9aa7ad", lw=1.6, ls=(0, (5, 4)), zorder=0)

# Memória do servidor: as sessões
box(ax, 9.7, 3.2, 3.0, 3.9, LIGHT, MID, lw=2.0, z=0)
ax.text(11.2, 6.75, "Sessões guardadas", ha="center", va="center", fontsize=FS - 1, color=MID, fontweight="bold")
box(ax, 9.95, 4.75, 2.5, 1.55, "white", ORANGE, lw=2.2)
ax.text(11.2, 5.95, "id A3F9", ha="center", va="center", fontsize=FS - 1, color=ORANGE, fontweight="bold", zorder=4)
ax.text(11.2, 5.3, "utilizador = \"ana\"", ha="center", va="center", fontsize=FS - 3, color=DARK,
        family="monospace", zorder=4)
box(ax, 9.95, 3.45, 2.5, 1.0, "white", "#9aa7ad", lw=1.6)
ax.text(11.2, 3.95, "id 7C21 (outro)", ha="center", va="center", fontsize=FS - 3, color="#5f6b70", zorder=4)

# 1: primeiro pedido, sem cookie
y = 6.85
arrow(ax, XB + 0.1, y, XS - 0.1, y, DARK)
step(ax, 0.55, y, 1, DARK)
ax.text((XB + XS) / 2, y + 0.3, "POST /login", ha="center", va="bottom",
        fontsize=FS - 2, color=DARK, family="monospace")
ax.text((XB + XS) / 2, y - 0.3, "utilizador=ana&palavra-passe=…", ha="center", va="top", fontsize=FS - 2, color=DARK, family="monospace")
ax.text((XB + XS) / 2, y - 0.8, "ainda sem cookie", ha="center", va="top", fontsize=FS - 3, color="#5f6b70",
        style="italic")
ax.annotate("", xy=(9.9, 5.6), xytext=(XS + 0.1, y - 0.15),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.0, ls="--", mutation_scale=18))
ax.text(8.25, 5.75, "getSession()\ncria a sessão", ha="left", va="top", fontsize=FS - 3, color=ORANGE)

# 2: resposta com Set-Cookie
y = 5.0
arrow(ax, XS - 0.1, y, XB + 0.1, y, ORANGE)
step(ax, 0.55, y, 2, ORANGE)
ax.text((XB + XS) / 2, y + 0.3, "200 OK", ha="center", va="bottom", fontsize=FS - 2, color=ORANGE,
        family="monospace")
ax.text((XB + XS) / 2, y - 0.3, "Set-Cookie: JSESSIONID=A3F9", ha="center", va="top", fontsize=FS - 1,
        color=ORANGE, family="monospace", fontweight="bold")

# 3: pedido seguinte, já com o cookie
y = 3.15
arrow(ax, XB + 0.1, y, XS - 0.1, y, DARK)
step(ax, 0.55, y, 3, DARK)
ax.text((XB + XS) / 2, y + 0.3, "GET /perfil", ha="center", va="bottom", fontsize=FS - 2, color=DARK,
        family="monospace")
ax.text((XB + XS) / 2, y - 0.3, "Cookie: JSESSIONID=A3F9", ha="center", va="top", fontsize=FS - 1,
        color=MID, family="monospace", fontweight="bold")
ax.annotate("", xy=(9.9, 5.0), xytext=(XS + 0.1, y + 0.1),
            arrowprops=dict(arrowstyle="-|>", color=MID, lw=2.0, ls="--", mutation_scale=18))
ax.text(8.25, 2.55, "procura a sessão A3F9:\nencontra \"ana\"", ha="left", va="center", fontsize=FS - 3, color=MID)

# 4: resposta personalizada
y = 1.2
arrow(ax, XS - 0.1, y, XB + 0.1, y, ORANGE)
step(ax, 0.55, y, 4, ORANGE)
ax.text((XB + XS) / 2, y + 0.3, "200 OK", ha="center", va="bottom", fontsize=FS - 2, color=ORANGE,
        family="monospace")
ax.text((XB + XS) / 2, y - 0.3, "página com os dados de \"ana\"", ha="center", va="top", fontsize=FS - 2,
        color=ORANGE, style="italic")

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
