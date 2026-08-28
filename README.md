# Sebenta ASW — Aplicações e Serviços Web

Projecto Quarto para a sebenta da UC de Aplicações e Serviços Web,
Mestrado em Engenharia Eletrotécnica e de Computadores (MEEC), UTAD.

## Estrutura

```
Sebenta-ASW/
├── _quarto.yml          # Configuração do projecto
├── index.qmd             # Prefácio
├── capitulos/
│   ├── cap01.qmd         # Arquitetura de Aplicações Web (as 3 peças: Frontend/Middleware/Backend)
│   ├── cap02.qmd         # HTML, CSS e Bootstrap (Frontend)
│   ├── cap03.qmd         # O Protocolo HTTP (Middleware)
│   ├── cap04.qmd         # Java EE e Fundamentos de Servlets (Backend)
│   ├── cap05.qmd         # Modelo Stateful: Sessões e JSP
│   ├── cap06.qmd         # Segurança e Filtros
│   ├── cap07.qmd         # Web Services REST e Arquitetura Stateless (Parte 1)
│   ├── cap08.qmd         # Web Services REST (Parte 2) e o Cliente em JavaScript
│   ├── apendiceA.qmd     # Configuração do Ambiente de Desenvolvimento
│   ├── apendiceB.qmd     # LABs Práticos (mesmos do ESIGELEC, com twist de JS)
│   └── apendiceC.qmd     # Código completo "World Capitals" (4 .html prontos a copiar)
├── assets/
│   ├── css/custom.css    # Estilos personalizados (paleta azul-petróleo)
│   ├── images/           # Imagens e figuras (heroes/, capa/Web/, capa/PDF/ — por preencher)
│   └── cover.tex          # Capa PDF (TikZ, sem foto ainda)
├── en/                    # Versão em inglês (projecto Quarto próprio, só HTML)
│   ├── _quarto.yml
│   ├── index.qmd
│   ├── references.qmd
│   ├── capitulos/         # cap01.qmd … cap07.qmd, em inglês (ainda 7 capítulos, desatualizado — ver Estado)
│   └── assets/css/custom.css  # cópia do CSS principal (ver nota abaixo)
└── referencias.bib        # Bibliografia (a partir da ficha oficial da UC)
```

## Renderização

```bash
# Versão portuguesa — livro completo (HTML + PDF)
quarto render

# Versão inglesa — só HTML (sem secção pdf: no en/_quarto.yml)
quarto render en/

# Preview com hot reload (cada versão tem de ser aberta em separado)
quarto preview
quarto preview en/
```

A versão em inglês (`en/`) segue o mesmo padrão já usado no Sebenta-IM:
projecto Quarto irmão, com `output-dir: ../docs/en`, gerando o site em
`docs/en/`. O rodapé de cada versão tem uma ligação para a outra
(`🇬🇧 English` / `🇵🇹 Português`), usando caminhos relativos à raiz do
site (`/en/` e `/`) — assume que o site é publicado na raiz do domínio;
ajustar se um dia for publicado num subdiretório (ex. GitHub Pages de
projecto).

**Nota sobre o CSS da versão inglesa:** o caminho `/assets/css/custom.css`
no `en/_quarto.yml` resolve-se à raiz do *site* do próprio subprojecto
`en/` (`docs/en/`), não à pasta principal (`docs/`). Por isso existe uma
cópia própria em `en/assets/css/custom.css` — sempre que o `custom.css`
principal for alterado, replicar a alteração também aqui.

## Estado

Projecto criado em 2026-08-26. Estrutura de 8 capítulos + 2 apêndices
definida a partir do planeamento em
`Planeamento de UUCC/ASW/Planeamento ASW.canvas`. A estrutura passou por
duas revisões: primeiro o Cap03 "O Protocolo HTTP" foi absorvido pelo
Cap01 (8→7 capítulos); depois, ao rever a sequência pedagógica, voltou a
sair como capítulo próprio, mas agora posicionado depois do Cap02
(HTML/CSS), não antes (7→8 capítulos de novo). A razão: o Cap01 passou a
terminar numa síntese explícita — "três peças: Frontend, Middleware,
Backend" — que serve de mapa ao resto do livro; o HTML só faz sentido como
a primeira peça concretizada, e o HTTP só é motivado depois de existir um
formulário HTML concreto a que se possa recorrer como exemplo (os mesmos
`capital.html`/`login.html` do Cap02). Cap01 a Cap06 já têm conteúdo real;
Cap07 e Cap08 ainda são esqueleto (tópicos-chave por secção).

A matéria e os trabalhos práticos seguem de perto uma UC homóloga já
lecionada no ESIGELEC (parceiro internacional) — ver `Team Inbox/Team-ASW/`
para os materiais de partida (programa oficial, Labs e slides do ESIGELEC,
slides da UTAD).

## Autor

João Pavão — UTAD, 2026 (componente teórica, autor dos capítulos)
