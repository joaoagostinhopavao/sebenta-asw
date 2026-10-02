"""Arquitetura em camadas da Jakarta EE, com o que o Tomcat cobre (Cap04 / Aula 04 da ASW).

Uso: python gen_cap04_camadas.py <ficheiro_saida.png>
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
GREY = "#6b7a82"
FS = 15

out = sys.argv[1] if len(sys.argv) > 1 else "jakarta-camadas.png"


def box(ax, x0, y0, w, h, text, fc, tc, ec=None, fs=FS, bold=True, lw=2.0, ls="-", z=2, ha="center"):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=fc, ec=ec or fc, lw=lw, ls=ls, zorder=z))
    if text:
        tx = x0 + w / 2 if ha == "center" else x0 + 0.3
        ax.text(tx, y0 + h / 2, text, ha=ha, va="center", fontsize=fs, color=tc,
                fontweight="bold" if bold else "normal", zorder=z + 1, linespacing=1.3)


def arrow(ax, x, y0, y1):
    ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle="<|-|>", mutation_scale=18,
                                 color=DARK, lw=2.2, zorder=1))


fig, ax = plt.subplots(figsize=(13, 8.2), dpi=200)
ax.set_xlim(0, 13)
ax.set_ylim(0, 8.2)
ax.set_aspect("equal")
ax.axis("off")

rows = [  # (y0, camada, componentes, componentes_cinzentos)
    (6.5, "Cliente\n(Client Tier)", "Browser · aplicações cliente", False),
    (4.55, "Web\n(Web Tier)", "Servlets · JSP · serviços Web", False),
    (2.6, "Negócio\n(Business Tier)", "Enterprise Beans", True),
    (0.65, "Dados\n(EIS Tier)", "Bases de dados · sistemas de\ninformação empresarial (EIS)", False),
]
H = 1.3
for y0, nome, comp, cinz in rows:
    box(ax, 0.3, y0, 2.9, H, nome, DARK, "white", fs=FS - 1)
    box(ax, 3.5, y0, 5.6, H, None if cinz else comp, LIGHT, DARK, ec=MID, fs=FS - 1, bold=False)
    if cinz:
        ax.text(6.3, y0 + H * 0.66, comp, ha="center", va="center", fontsize=FS - 1, color=GREY, zorder=4)

for k in range(3):
    arrow(ax, 6.3, rows[k + 1][0] + H + 0.05, rows[k][0] - 0.05)

# Onde reside
ax.text(10.95, rows[0][0] + H / 2, "máquina do cliente", ha="center", va="center", fontsize=FS - 2,
        color=DARK, style="italic")
ax.text(10.95, (rows[1][0] + rows[2][0] + H) / 2, "servidor Jakarta EE", ha="center", va="center",
        fontsize=FS - 2, color=DARK, style="italic")
ax.plot([9.5, 9.5], [rows[2][0] + 0.1, rows[1][0] + H - 0.1], color=DARK, lw=1.6)
ax.text(10.95, rows[3][0] + H / 2, "servidor de base de dados", ha="center", va="center",
        fontsize=FS - 2, color=DARK, style="italic")

# Tomcat cobre só a Web Tier
box(ax, 0.1, rows[1][0] - 0.15, 9.2, H + 0.3, None, "none", ORANGE, ec=ORANGE, lw=2.6, ls="--", z=3)
ax.text(9.65, rows[1][0] + H + 0.32, "Tomcat (esta UC)", ha="left", va="center", fontsize=FS,
        color=ORANGE, fontweight="bold")
ax.text(6.3, rows[2][0] + H * 0.3, "no Tomcat: classes Java comuns (ex.: o DAO)", ha="center",
        va="center", fontsize=FS - 3, color=ORANGE, style="italic", zorder=5)

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
