import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

TEAL="#106E8C"; LIGHT="#DFF2F6"; DARK="#0D1B24"; ORANGE="#E07A1F"; FADE="#EEF6F8"; GREY="#5B6B73"

fig, ax = plt.subplots(figsize=(19, 10))
ax.set_xlim(-3.6, 16.8); ax.set_ylim(-0.6, 10.6); ax.axis("off")

def box(x0, x1, y, h, fc, text, tc=DARK, fs=15, bold=False, ec=DARK, lw=2.2, alpha=1):
    ax.add_patch(FancyBboxPatch((x0+0.03, y), x1-x0-0.06, h, boxstyle="round,pad=0,rounding_size=0.12",
                                fc=fc, ec=ec, lw=lw, alpha=alpha))
    ax.text((x0+x1)/2, y+h/2, text, ha="center", va="center", fontsize=fs, color=tc,
            fontweight="bold" if bold else "normal", linespacing=1.3)

H = 1.5
rows = [9.0, 6.5, 4.0, 1.5]       # y de cada linha (base)
X = dict(eth=0.2, ip=3.3, tcp=6.1, app=8.9, end=14.4, fcs=15.4)

layers = [("Aplicação", "HTTP"), ("Transporte", "TCP"), ("Internet", "IP"), ("Acesso à Rede", "Ethernet")]
pdus = ["mensagem HTTP", "segmento TCP", "pacote IP", "trama Ethernet"]
for (name, proto), y in zip(layers, rows):
    ax.text(-3.4, y+H/2+0.22, name, ha="left", va="center", fontsize=21, fontweight="bold", color=DARK)
    ax.text(-3.4, y+H/2-0.33, proto, ha="left", va="center", fontsize=16, color=GREY)

http_txt = "GET /capital?countrycode=PT\nHost: www.example.com"
# linha 1: aplicação
y = rows[0]
box(X["app"], X["end"], y, H, TEAL, http_txt, tc="white", fs=15.5, bold=True)
# linha 2: transporte
y = rows[1]
box(X["tcp"], X["app"], y, H, ORANGE, "Cabeçalho TCP\nportas\n51734 → 80", tc="white", fs=15, bold=True)
box(X["app"], X["end"], y, H, LIGHT, "dados\n(mensagem HTTP)", fs=15)
# linha 3: internet
y = rows[2]
box(X["ip"], X["tcp"], y, H, ORANGE, "Cabeçalho IP\n192.168.1.20 →\n203.0.113.10", tc="white", fs=15, bold=True)
box(X["tcp"], X["end"], y, H, LIGHT, "dados\n(segmento TCP)", fs=15)
# linha 4: acesso à rede
y = rows[3]
box(X["eth"], X["ip"], y, H, ORANGE, "Cabeçalho\nEthernet\nMAC orig. → dest.", tc="white", fs=15, bold=True)
box(X["ip"], X["end"], y, H, LIGHT, "dados\n(pacote IP)", fs=15)
box(X["end"], X["fcs"], y, H, ORANGE, "FCS", tc="white", fs=14, bold=True)

# linhas guia tracejadas: a PDU inteira de cima passa a "dados" da linha de baixo
guides = [(X["app"], X["end"]), (X["tcp"], X["end"]), (X["ip"], X["end"])]
for (x0, x1), ytop, ybot in zip(guides, rows[:-1], rows[1:]):
    for xx in (x0, x1):
        ax.plot([xx, xx], [ytop-0.05, ybot+H+0.05], ls=(0, (4, 3)), color=GREY, lw=1.6)

# nomes das PDU por baixo de cada linha
spans = [(X["app"], X["end"]), (X["tcp"], X["end"]), (X["ip"], X["end"]), (X["eth"], X["fcs"])]
for (x0, x1), y, n in zip(spans, rows, pdus):
    ax.text((x0+x1)/2, y-0.28, n, ha="center", va="center", fontsize=15, style="italic", color=TEAL, fontweight="bold")

# seta de envio
ax.add_patch(FancyArrowPatch((16.25, rows[0]+H), (16.25, rows[3]), arrowstyle="-|>", mutation_scale=28, lw=3, color=DARK))
ax.text(16.6, (rows[0]+H+rows[3])/2, "envio (encapsulamento)", rotation=90, ha="center", va="center", fontsize=17, color=DARK)

# legenda
ax.add_patch(FancyBboxPatch((-3.4, -0.45), 0.45, 0.35, boxstyle="round,pad=0,rounding_size=0.06", fc=ORANGE, ec=DARK, lw=1.5))
ax.text(-2.8, -0.27, "acrescentado por esta camada", va="center", fontsize=15, color=DARK)
ax.add_patch(FancyBboxPatch((4.6, -0.45), 0.45, 0.35, boxstyle="round,pad=0,rounding_size=0.06", fc=LIGHT, ec=DARK, lw=1.5))
ax.text(5.2, -0.27, "recebido da camada de cima, transportado sem ser lido", va="center", fontsize=15, color=DARK)

plt.savefig("assets/images/capitulos/cap03/Encapsulamento.png", dpi=110, bbox_inches="tight", facecolor="white")
