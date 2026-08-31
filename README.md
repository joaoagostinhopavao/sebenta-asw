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
│   ├── apendiceA.qmd     # Código completo "World Capitals" (4 .html prontos a copiar)
│   ├── apendiceB.qmd     # Assinatura de Tokens JWT (HMAC vs. RSA/ECDSA, ataque alg:none)
│   ├── apendiceC.qmd     # Configuração do Ambiente de Desenvolvimento
│   ├── apendiceD1.qmd    # LAB1: Primeiro Endpoint e DAO Simulado
│   ├── apendiceD2.qmd    # LAB2: Login e Sessão
│   ├── apendiceD3.qmd    # LAB3: AuthenticationFilter e Logout
│   ├── apendiceD4.qmd    # LAB4: JDBC e CRUD Completo
│   ├── apendiceD5.qmd    # LAB5 (Opcional): Autenticação Sem Estado com JWT
│   └── apendiceD6.qmd    # LAB6: O Front-Office em JavaScript
├── assets/
│   ├── css/custom.css    # Estilos personalizados (paleta azul-petróleo)
│   ├── images/           # Imagens e figuras (heroes/, capa/Web/, capa/PDF/ — por preencher)
│   └── cover.tex          # Capa PDF (TikZ, sem foto ainda)
├── en/                    # Versão em inglês (projecto Quarto próprio, só HTML)
│   ├── _quarto.yml
│   ├── index.qmd
│   ├── references.qmd
│   ├── capitulos/         # cap01.qmd … cap08.qmd + apendiceA.qmd … apendiceD6.qmd, em inglês (completo)
│   └── assets/
│       ├── css/custom.css     # cópia do CSS principal (ver nota abaixo)
│       └── images/capitulos/  # cópia das imagens dos capítulos/apêndices (ver nota abaixo)
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

**Nota sobre as imagens da versão inglesa:** pelo mesmo motivo, os
caminhos relativos `../assets/images/...` usados nos capítulos/apêndices
de `en/` resolvem-se a `en/assets/images/`, não à pasta principal. Por
isso existe uma cópia própria em `en/assets/images/capitulos/` — sempre
que uma imagem for acrescentada ou alterada na pasta principal
(`assets/images/capitulos/`), replicar também aqui. **Exceção:** os
diagramas gerados por nós (não *screenshots* do *browser* nem extraídos
de slides) têm, em `en/`, uma versão própria com o texto traduzido para
inglês, em vez de uma cópia idêntica da versão portuguesa — atualmente
`Modelo_TCP_IP.png` e `HTTP_message_request_format.png` (Cap03),
`Modelo_MVC_Geral.png` e `Comparacao_Scopes.png` (Cap05), `Filter_Chain.png`,
`Filter_Lifecycle.png` e `Servlet_vs_Filter.png` (Cap06), e `JWT_HMAC.png`
e `JWT_Assimetrico.png` (Apêndice B). Os scripts de geração (`matplotlib`,
paleta azul-petróleo da sebenta) não fazem parte do repositório, tal como
já acontecia com os originais em português — se for preciso voltar a
ajustar um destes diagramas, terá de se recriar o script do zero a partir
da imagem existente.

## Estado

Projecto criado em 2026-08-26. Estrutura de 8 capítulos + 9 apêndices
definida a partir do planeamento em
`Planeamento de UUCC/ASW/Planeamento ASW.canvas`. A estrutura de capítulos
passou por duas revisões: primeiro o Cap03 "O Protocolo HTTP" foi absorvido
pelo Cap01 (8→7 capítulos); depois, ao rever a sequência pedagógica, voltou
a sair como capítulo próprio, mas agora posicionado depois do Cap02
(HTML/CSS), não antes (7→8 capítulos de novo). A razão: o Cap01 passou a
terminar numa síntese explícita — "três peças: Frontend, Middleware,
Backend" — que serve de mapa ao resto do livro; o HTML só faz sentido como
a primeira peça concretizada, e o HTTP só é motivado depois de existir um
formulário HTML concreto a que se possa recorrer como exemplo (os mesmos
`capital.html`/`login.html` do Cap02). **Todos os 8 capítulos têm agora
conteúdo real.**

Os apêndices seguem, por ordem, o mesmo critério: A e B acompanham a ordem
dos capítulos a que se referem (Código Completo → Cap02; Assinatura de
Tokens JWT → Cap08), e C+D1-D6 formam a parte prática do livro
(Configuração do Ambiente, seguida dos seis LABs). Os LABs, antes um único
Apêndice B, foram desdobrados em D1-D6 (um por LAB) por causa do
comprimento que um único apêndice atingiria com todos completos. Os LABs
1-5 constroem só o *backend* (LAB5 é opcional, autenticação sem estado com
JWT); o LAB6, escrito por último, liga esse *backend* a um *front-office*
em JavaScript, em vez de o "twist" de JavaScript ir espalhado por cada LAB
individual. **Todos os LABs (Apêndices D1-D6) estão escritos** — o LAB6 foi
o último, ligando o *backend* dos LABs 1-4 (e, para quem o tiver feito,
também a variante do LAB5) às páginas do Apêndice A através de `fetch()`.

**Versão inglesa (`en/`) completa** — tradução de todo o livro (8
capítulos + 9 apêndices), feita numa única ronda dedicada depois de o PT
ter ficado todo fechado, em vez de espelhar capítulo a capítulo à medida
que iam sendo escritos. Regra seguida para o texto visível das páginas
estáticas da aplicação "World Capitals" (barra de navegação, `login.html`,
`capital.html`, `paises-editar.html`, e as suas cópias/variantes nos
Apêndices A e D1-D6): mantido em português em ambas as versões, porque
essas páginas e os *screenshots* que as acompanham são partilhados
verbatim entre PT e EN (nunca refeitos em inglês) — só a prosa envolvente
foi traduzida. Identificadores internos (nomes de variáveis/funções
JavaScript, `id`s de HTML não usados em nenhum *screenshot*) foram
traduzidos livremente para inglês natural.

A matéria e os trabalhos práticos seguem de perto uma UC homóloga já
lecionada no ESIGELEC (parceiro internacional) — ver `Team Inbox/Team-ASW/`
para os materiais de partida (programa oficial, Labs e slides do ESIGELEC,
slides da UTAD).

## Autor

João Pavão — UTAD, 2026 (componente teórica, autor dos capítulos)
