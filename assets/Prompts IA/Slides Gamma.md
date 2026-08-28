🎓 CONTEXTO — UC Aplicações e Serviços Web (ASW)

Estou a criar decks de slides para a UC de Aplicações e Serviços Web (MEEC, UTAD). Cada deck corresponde a uma aula. Usa sempre as seguintes convenções de estilo e layout. Cada aula deve ter entre 20, no mínimo, a 25 slides (número máximo preferencial), nunca deverão exceder os 30.

Vou-te passar as instruções de construção dos slides aqui neste texto, depois deves perguntar-me pelo texto da aula e eu copio e colo (ou passo-te um ficheiro). Antes de começares deves perguntar se há figuras a inserir. Se houver eu insiro e tu deves conservar o mais possível as que forem diagramas e não as substituir por imagens generativas. No entanto podes e deves melhorá-las esteticamente e usar a paleta de cores do resto do esquema dos slides. Deverás inserir essas figuras nos locais indicados nos ficheiros de texto.

Todos os termos em inglês nos slides de língua portuguesa devem ser italicizados. Excetuam-se código Java/HTML/CSS/JavaScript e nomes próprios de tecnologias (Servlet, Tomcat, Bootstrap, JSON, etc.), que não se italicizam.

🎨 TEMAS POR BLOCO

Aula 1 e Aulas 13–14 (Apresentação / Encerramento — Apresentação de Trabalhos e Teste Teórico): tema Pearl ou Howlite
Aulas 2–3 (Bloco 1 — Fundamentos da Web): tema Cornflower ou Breeze
Aulas 4–5 (Bloco 2 — Java EE Clássico): tema Sage ou Pistachio
Aulas 6–8 (Bloco 3 — Web Services): tema Vanilla ou Bee Happy
Aulas 9–12 (Bloco 4 — LABs Práticos): tema Lavender ou Iris

🖼️ IMAGENS ILUSTRATIVAS

Estilo: isometric illustration, clean geometric shapes, flat colors, technical diagram aesthetic, [cor do bloco] and white palette, no shadows, crisp lines
Modelo: ideogram-v4-turbo
Formato preferido: quadrado (square) para imagens em colunas; portrait para accent images laterais
artStylePreset: custom

📐 DIAGRAMAS E ESQUEMAS TÉCNICOS

Fundo branco, tipografia limpa, sem gradientes
Cor de destaque: azul-petróleo (#0e6e8c, ou #4dd0e1 para variantes mais claras) para o Bloco 1, alinhado com a paleta da Sebenta-ASW; adaptar à cor do bloco nos outros decks
Melhorar diagramas existentes com gpt-image-2-mini (imageEditContent), mantendo estrutura e substituindo apenas as cores
Exemplos de diagramas deste bloco: Arquitetura em Camadas da Jakarta EE (Client/Web/Business/EIS Tier), Apresentação vs. Serviço (front-end/back-end), o Padrão MVC (clássico e distribuído)

📄 LAYOUT DOS SLIDES

O primeiro slide terá que ter obrigatoriamente uma imagem que "resuma" o tema do deck. Essa imagem será inserida no slide 1; para além disso deve ser feita uma segunda cópia dessa imagem no formato 16:9 e colocada na pasta de média.
Título (h1) e label fora e acima das colunas
Imagem numa coluna (40–45%), texto na outra (55–60%)
Imagens com dimensions="fill" para preencher a coluna
Accent image lateral (image-layout="left" ou "right") para slides mais simples com uma única imagem
Label variant="solid" para slides de conteúdo; variant="outline" para slides de capa/abertura

💾 COMPATIBILIDADE POWERPOINT

Evitar smart layouts complexos (arrows, processSteps) — substituir por listas numeradas em <p> com bold
Smart layouts simples (outlineBoxesWithSideLine, bigBullets, solidBoxes) são aceitáveis
Imagens em colunas exportam bem; accent images também

🌍 LÍNGUA

Todo o conteúdo em Português europeu (pt-PT)
Responde-me sempre em português

📚 ESTRUTURA DA UC (para referência)

Aula 1 — Apresentação da UC e Arquitetura de Aplicações Web (tema de abertura, sem prática)
Bloco 1 — Fundamentos da Web: Aula 2 (HTML, CSS e Bootstrap), Aula 3 (O Protocolo HTTP)
Bloco 2 — Java EE Clássico: Aula 4 (Java EE e Fundamentos de Servlets), Aula 5 (Modelo Stateful: Sessões e JSP)
Bloco 3 — Web Services: Aula 6 (Segurança e Filters), Aula 7 (Web Services REST e Arquitetura Stateless — Parte 1), Aula 8 (Web Services REST — Parte 2 — e o Cliente em JavaScript)
Bloco 4 — LABs Práticos: Aula 9 (LAB1: Primeiro Endpoint e DAO Simulado), Aula 10 (LAB2: Login e Sessão), Aula 11 (LAB3: AuthenticationFilter e Logout), Aula 12 (LAB4: JDBC e CRUD Completo)
Aula 13 — Apresentação dos Trabalhos Práticos (tema de encerramento)
Aula 14 — Teste Teórico (tema de encerramento)
