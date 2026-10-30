"""Anatomia de um JWT: as três partes codificadas e o que cada uma contém (Cap08 / Aula 08 da ASW).

O token do esquema é verdadeiro (HS256), o mesmo do exemplo do capítulo.
Uso: python gen_cap08_jwt_anatomia.py <ficheiro_saida.png>
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
GREY = "#5f6b70"
FS = 18

HEADER = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
PAYLOAD = "eyJzdWIiOiJhbmEiLCJyb2xlIjoidXNlciIsImV4cCI6MTg5MzQ1NjAwMH0"
SIGNATURE = "O1M0ymsf-ceCK3OxAewCVLReDaVliYUirWclbBC4-LE"

out = sys.argv[1] if len(sys.argv) > 1 else "jwt_anatomia.png"


def box(ax, x0, y0, w, h, fc, ec, lw=2.2):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fc, ec=ec, lw=lw, zorder=1))


fig, ax = plt.subplots(figsize=(17.6, 8.4), dpi=200)
ax.set_xlim(0, 17.6)
ax.set_ylim(0, 8.4)
ax.axis("off")

# o token inteiro, em três cores, em duas linhas
ax.text(0.2, 7.95, "O token, tal como viaja no cabeçalho Authorization (as três partes em Base64URL):", ha="left", va="center",
        fontsize=FS, color=DARK, fontweight="bold")
linha1 = [(HEADER, MID), (".", DARK), (PAYLOAD, ORANGE), (".", DARK)]
linha2 = [(SIGNATURE, GREEN)]
for y, partes in ((7.3, linha1), (6.8, linha2)):
    t = ax.text(0.2, y, "", fontsize=FS - 2, family="monospace")
    x = 0.2
    for txt, cor in partes:
        t = ax.text(x, y, txt, ha="left", va="center", fontsize=FS - 2, family="monospace", color=cor,
                    fontweight="bold")
        fig.canvas.draw()
        bb = t.get_window_extent().transformed(ax.transData.inverted())
        x = bb.x1

# as três partes, uma por linha: nome, conteúdo descodificado, nota
linhas = [
    ("Header", MID, '{"alg":"HS256","typ":"JWT"}', "o algoritmo da assinatura", "só codificado: qualquer um lê"),
    ("Payload", ORANGE, '{"sub":"ana","role":"user",\n "exp":1893456000}',
     "as claims: quem é, que perfil tem, até quando vale", "só codificado: qualquer um lê"),
    ("Assinatura", GREEN, "3b 53 34 ca 6b 1f f9 c7 ... f8 b1\n(32 bytes, ilegível: não é texto)",
     "= HMAC-SHA256(header.payload, chave secreta)", "ninguém a consegue forjar sem a chave"),
]
y = 4.95
for nome, cor, conteudo, desc, nota in linhas:
    box(ax, 0.2, y - 0.75, 2.4, 1.5, cor, cor)
    ax.text(1.4, y, nome, ha="center", va="center", fontsize=FS + 1, color="white", fontweight="bold")
    ax.add_patch(FancyArrowPatch((2.75, y), (4.15, y), arrowstyle="-|>", mutation_scale=20, color=cor,
                                 lw=2.4, zorder=3))
    ax.text(3.45, y + 0.15, "descodifica", ha="center", va="bottom", fontsize=FS - 7, color=cor, style="italic")
    box(ax, 4.3, y - 0.75, 6.6, 1.5, LIGHT, cor, lw=2.0)
    ax.text(4.55, y, conteudo, ha="left", va="center", fontsize=FS - 2, family="monospace", color=DARK,
            linespacing=1.3)
    ax.text(11.2, y + 0.28, desc, ha="left", va="center", fontsize=FS - 2, color=DARK)
    ax.text(11.2, y - 0.28, nota, ha="left", va="center", fontsize=FS - 2, color=cor, style="italic",
            fontweight="bold")
    y -= 1.85

fig.savefig(out, bbox_inches="tight", pad_inches=0.12, facecolor="white")
print("ok", out)
