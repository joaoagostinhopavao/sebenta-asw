# Sebenta ASW — Aplicações e Serviços Web

Projecto Quarto para a sebenta da UC de Aplicações e Serviços Web,
Mestrado em Engenharia Eletrotécnica e de Computadores (MEEC), UTAD.

## Estrutura

```
Sebenta-ASW/
├── _quarto.yml          # Configuração do projecto
├── index.qmd             # Prefácio
├── capitulos/
│   ├── cap01.qmd         # Apresentação da UC e Arquitetura de Aplicações Web
│   ├── cap02.qmd         # HTML, CSS e Bootstrap
│   ├── cap03.qmd         # O Protocolo HTTP
│   ├── cap04.qmd         # Java EE e Fundamentos de Servlets
│   ├── cap05.qmd         # Modelo Stateful: Sessões e JSP
│   ├── cap06.qmd         # Segurança e Filters
│   ├── cap07.qmd         # Web Services REST e Arquitetura Stateless (Parte 1)
│   ├── cap08.qmd         # Web Services REST (Parte 2) e o Cliente em JavaScript
│   ├── apendiceA.qmd     # Configuração do Ambiente de Desenvolvimento
│   └── apendiceB.qmd     # LABs Práticos (mesmos do ESIGELEC, com twist de JS)
├── assets/
│   ├── css/custom.css    # Estilos personalizados (paleta azul-petróleo)
│   ├── images/           # Imagens e figuras (heroes/, capa/Web/, capa/PDF/ — por preencher)
│   └── cover.tex          # Capa PDF (TikZ, sem foto ainda)
└── referencias.bib        # Bibliografia (a partir da ficha oficial da UC)
```

## Renderização

```bash
# Livro completo (HTML + PDF)
quarto render

# Preview com hot reload
quarto preview
```

## Estado

Projecto criado em 2026-08-26. Estrutura dos 8 capítulos + 2 apêndices
definida a partir do planeamento em
`Planeamento de UUCC/ASW/Planeamento ASW.canvas`. Capítulos ainda por
escrever (esqueleto com tópicos-chave por secção).

A matéria e os trabalhos práticos seguem de perto uma UC homóloga já
lecionada no ESIGELEC (parceiro internacional) — ver `Team Inbox/Team-ASW/`
para os materiais de partida (programa oficial, Labs e slides do ESIGELEC,
slides da UTAD).

## Autor

João Pavão — UTAD, 2026 (componente teórica, autor dos capítulos)
