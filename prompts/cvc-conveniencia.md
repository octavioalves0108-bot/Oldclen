# Prompt — site da CVC Conveniência

**Como usar:** junte os arquivos da seção 5 e responda os itens da seção 3 com
o dono (pelo Direct do Instagram ou pessoalmente). Depois, copie tudo que
está abaixo da linha e cole numa IA de código, como o Claude.

> Já existe uma demo feita com este mesmo roteiro em
> [`../demos/cvc-conveniencia/`](../demos/cvc-conveniencia/). Use este prompt
> para refazer o site com os dados reais quando o dono confirmar, ou para
> gerar em outra ferramenta.

---

Você é um designer e desenvolvedor front-end sênior, especialista em sites de
marca com acabamento premium. Crie o site de apresentação da **CVC
Conveniência**, uma loja de conveniência — bebidas, gelo, carvão e snacks —
cuja marca é uma coruja laranja em forma de pino de mapa.

## 1. Objetivo

Uma página única, que abre com uma animação de carregamento de marca, e que
converte visita em **pedido** — pelo Direct do Instagram ou pelo WhatsApp
(seção 3). O público é quem está no meio do rolê, do churrasco ou da
resenha e precisa de algo gelado agora. Tom: noturno, descontraído, confiante
— "a coruja tá de olho" —, sem apelo ao exagero de bebida.

## 2. Dados reais do negócio — use exatamente estes

| Campo | Valor |
|---|---|
| Nome | CVC Conveniência |
| Instagram | [@cvcconveniencia](https://www.instagram.com/cvcconveniencia/) |
| Canal de pedido (enquanto não houver WhatsApp) | Direct do Instagram — `https://ig.me/m/cvcconveniencia` |
| Marca | Coruja laranja dentro de um pino de mapa: cabeça arredondada, rosto escuro, dois olhos laranja, bico em V, uma barra horizontal e a ponta do pino embaixo. Na logo original, ela fica sobre uma foto escura de garrafas e gelo |
| Cor da marca | Laranja `#FF8638`, amostrado da logo |
| Cor de fundo da marca | Grafite quase preto, `#16181A` na logo (use `#0C0D0E` como fundo do site) |

**É só isso que é público.** O perfil não tem ficha no Google, site nem
cadastro em guia comercial que tenha aparecido nas buscas. Todo o resto
precisa vir do dono (seção 3).

## 3. Dados a confirmar antes de publicar

Peça ao dono. Até ele responder, use o texto reserva ou omita a seção
indicada.

- **WhatsApp.** Com o número, todos os botões passam a abrir o WhatsApp com
  mensagem pronta. Sem ele, os botões abrem o Direct
- **Endereço e bairro.** Sem eles, **não crie a seção "Como chegar"**, nem
  mapa, nem JSON-LD com endereço
- **Horário.** A coruja sugere "noite", mas não afirme "aberto até tarde" nem
  "24h" sem confirmação. Sem horário, omita
- **O que vende de fato.** Marque com ele o que existe, e só isso entra no
  carrossel: cervejas · destilados (whisky, gin, vodka) · vinhos e
  espumantes · energéticos e refrigerantes · água · gelo · carvão · snacks e
  petiscos · doces · tabacaria. Reserva, se ele não responder: cervejas,
  gelo, carvão e snacks
- **Entrega.** Se faz delivery, a área e se cobra taxa. Sem confirmação, não
  mencione entrega — fale em "pedido" e "combine com a loja"
- **Formas de pagamento** (Pix, cartão, dinheiro). Sem confirmação, omita
- **Se vende bebida alcoólica.** Se sim, a pergunta de idade da abertura é
  obrigatória (seção 7) e os avisos legais do rodapé também

## 4. O que nunca inventar

- **Preço, promoção, combo ou "o mais barato"**
- **Horário, entrega, tempo de entrega, raio de entrega, "24h"**
- **Depoimento, nota de avaliação ou número de seguidores**
- **Marcas de terceiros.** Nada de logo, rótulo ou nome de cerveja, whisky,
  energético etc. As ilustrações de produto são genéricas, sem marca
- **Foto de produto como se fosse da loja.** Não gere foto por IA fingindo
  ser a prateleira ou a geladeira dele. Sem foto real, use ilustração
  vetorial (seção 6)
- **Chamada que incentive consumo excessivo** ("bebe até cair", "open bar"
  etc.)

## 5. Arquivos que eu anexo

- `logo.png` — a logo do Instagram (151×148 px — pequena; ver abaixo)
- `coruja.svg` — a coruja da logo **vetorizada**, sem o fundo, para usar
  nítida em tamanho grande. Está em
  [`../demos/cvc-conveniencia/fonte/img/coruja.svg`](../demos/cvc-conveniencia/fonte/img/coruja.svg).
  Tem três camadas: rosto e sobrancelha escuros (`#131415`), corpo laranja
  com os vazados (`fill-rule="evenodd"`) e os olhos por cima — separe os
  olhos num grupo próprio para animar
- Fotos do Instagram dele, se houver: fachada, geladeira, balcão, produtos
  (opcional)

**Regra da logo:** a imagem `logo.png` aparece só em tamanho pequeno (até
~90 px): menu, rodapé, ícone da aba, avatar do perfil. Em tamanho grande
(abertura, destaques, chamada final), use sempre o `coruja.svg`.

## 6. Direção de arte

- **Conceito:** "a coruja da madrugada". Noite, fumaça quente, vidro gelado,
  condensação. O laranja da coruja é a única luz forte da página
- **Paleta:** fundo `#0C0D0E`, superfícies `#131516` e `#1B1D1F`, laranja
  `#FF8638` (marca), laranja escuro `#FF6A13`, âmbar `#FFB45E`, creme
  `#F4EFE9` (texto), cinza `#8F9295` (texto secundário), azul-gelo
  `#BFE6FF` (detalhes de gelo)
- **Tipografia:** Bricolage Grotesque em peso 800 e largura 78–80% para os
  títulos (grossa e condensada, com cara de letreiro), Instrument Serif
  itálico em laranja para a palavra de destaque de cada título, Manrope para
  o texto. Google Fonts
- **Textura:** grão de filme leve e **estático**; fumaça laranja em
  gradiente radial, sem desfoque
- **Ilustração dos produtos:** vetorial, com gradientes que imitam vidro,
  metal e líquido — garrafa âmbar de cerveja com gotas de condensação, copo
  com espuma e bolhas subindo, garrafa de whisky com copo e gelo, garrafa de
  vinho com taça, latas metálicas, cubos de gelo translúcidos, carvão com
  brasa, pacote de salgadinho. Cada ilustração em cena escura com um foco de
  luz na cor da categoria. **Sem marca nenhuma nos rótulos**

## 7. Estrutura da página, seção por seção

1. **Abertura (loader, ~3 s):** a coruja (`coruja.svg`) se desenha em traço
   laranja, se preenche e **pisca duas vezes**, flutuando sobre anéis de
   "localização" que se expandem num piso em perspectiva 3D. Abaixo,
   "CVC" com as letras subindo uma a uma e "Conveniência" em espaçamento
   largo. Contador de 000 a 100 com frases que trocam ("Gelando as
   bebidas", "Quebrando o gelo", "Acendendo o carvão", "Acordando a
   coruja", "Abrindo a porta"). Nos cantos: "Conveniência" e
   "@cvcconveniencia"
2. **Pergunta de idade** (se vender bebida alcoólica — seção 3): ao chegar em
   100%, a coruja sobe e aparece o cartão "Você tem *18 anos* ou mais?" com
   "Sim, pode entrar" e "Ainda não". O foco vai para "Sim", e Enter
   confirma. O "Ainda não" mostra: "Então a gente se vê daqui a pouco. A
   coruja espera você fazer 18." e não libera o site. A resposta "sim" fica
   salva no navegador (`localStorage`, com `try/catch`), e a pergunta não
   se repete. Ao entrar, um círculo laranja se abre a partir da coruja,
   cobre a tela e sobe como uma cortina, revelando o topo
3. **Menu fixo:** logo pequena + "CVC / Conveniência", links (Seleção, A CVC,
   Como pedir, Instagram) e botão "Pedir agora". Fica sólido depois de
   rolar, some ao rolar para baixo, volta ao rolar para cima
4. **Topo (o efeito 3D principal):** à esquerda, "A noite pede. / A CVC
   *tem.*" com as letras entrando uma a uma; subtítulo "Bebidas geladas,
   gelo, carvão e aquele petisco que faltava. A conveniência que sabe o que
   o seu rolê precisa." (ajuste à seção 3); botões "Pedir pelo Direct" (ou
   WhatsApp) e "Ver a seleção". À direita, uma **lata 3D girando**: cilindro
   de faces CSS com rótulo desenhado em `<canvas>` — fundo metálico escuro,
   faixa laranja diagonal com "GELADA • CVC •" repetido, a coruja de um lado
   e "CVC / CONVENIÊNCIA" do outro, gotas de condensação —, tampa metálica
   com anel, sombreamento cilíndrico fixo e borda laranja. Em volta: 4 cubos
   de gelo 3D translúcidos girando em profundidades diferentes, a logo em
   selo de app flutuando, dois selos ("Seleção da casa", "Chama no Direct")
   e bolhas subindo. A cena inclina com o mouse; a lata gira mais rápido
   quando a página rola. Ao fundo, "CVC" gigante só em contorno, com
   parallax
5. **Faixas cruzadas:** duas faixas inclinadas correndo em sentidos opostos —
   uma laranja ("Cerveja gelada ✦ Destilados ✦ Gelo ✦ Carvão ✦ Snacks",
   com as categorias confirmadas) e uma escura em contorno ("Chama a coruja
   ✦ @cvcconveniencia"). Elas entortam com a velocidade da rolagem
6. **Seleção da casa:** carrossel 3D (coverflow) com um card por categoria
   confirmada. Cada card tem número, etiqueta ("Sempre no ponto", "Pra
   caprichar", "Fogo e gelo"...), a ilustração animada (bolhas, gotas
   escorrendo, brasa pulsando, fumaça), o título, uma frase curta, chips de
   exemplos e "Pedir agora" com mensagem pronta citando a categoria. Card da
   frente com brilho laranja e inclinação que segue o mouse. Arrastar,
   clicar, setas do teclado e troca automática com barra de progresso. Abaixo
   do carrossel: "Beba com moderação · Venda de bebidas alcoólicas proibida
   para menores de 18 anos". **Se o dono mandar fotos**, cada card aceita
   foto no lugar da ilustração
7. **A CVC (manifesto):** à esquerda, a coruja grande que **pisca e segue o
   cursor com os olhos**; à direita, um texto que acende palavra por palavra
   com a rolagem — "Nem sempre dá pra planejar. A cerveja acaba, o gelo
   derrete, a visita chega sem avisar. Pra essas horas existe a *CVC:* o
   que falta, *gelado* e *perto* de você — com uma coruja de olho em tudo."
8. **Como pedir:** três cartões com número grande vazado e inclinação 3D —
   "Escolha", "Chame a coruja" (pelo Direct/WhatsApp, @cvcconveniencia) e
   "Aproveite gelado"
9. **Instagram:** título "Tudo o que chega na loja aparece *primeiro* lá.",
   botão "Seguir @cvcconveniencia" e um **celular 3D** inclinado, que segue
   o mouse, com o perfil estilizado: avatar da logo com anel laranja
   girando, nome, @, "Seguir" e "Mensagem", destaques e uma grade de 9
   blocos gráficos que aparecem em sequência. Só nome, @ e logo são reais —
   **sem número de seguidores, sem bio inventada, sem posts falsos**
10. **Como chegar** — só se o endereço for confirmado (seção 3)
11. **Chamada final:** a coruja piscando, "Bateu a vontade? / Chama a
    *coruja.*", raios laranja girando devagar e um brilho que cresce com a
    rolagem, botão de pedido e o @
12. **Rodapé:** logo, Instagram, links e, em linha própria: "Beba com
    moderação · Venda de bebidas alcoólicas proibida para menores de 18
    anos · Se beber, não dirija"
13. **Botão flutuante** de pedido (Direct ou WhatsApp) que aparece depois do
    topo

## 8. Motion e 3D

- Letras dos títulos entrando uma a uma, com a palavra mascarada (a letra
  sobe de trás de uma linha invisível)
- Elementos entrando ao rolar: subir com fade, desfoque que clareia,
  inclinação 3D que se endireita
- Lata 3D girando + cubos de gelo 3D + cena que inclina com o mouse; no
  celular, balanço lento automático
- Coruja que pisca de tempos em tempos e segue o cursor com os olhos
- Carrossel coverflow 3D; cartões e celular com inclinação 3D
- Bolhas e faíscas subindo no topo
- Faixas que entortam com a velocidade da rolagem
- Botões magnéticos no computador; brilho que atravessa o botão principal;
  cursor em anel que vira "Arraste" sobre o carrossel
- Rolagem suave com inércia na roda do mouse (toque e teclado nativos)
- Barra de progresso da rolagem
- Respeite "reduzir movimento": abertura curta, sem autoplay, sem bolhas, sem
  giro contínuo

## 9. Regras de desempenho (a página tem que ser fluida no celular)

Estas regras vieram da otimização da demo: sem elas, a página rodava a 12–20
quadros por segundo num celular médio; com elas, a ~60.

- Anime apenas `transform` e `opacity`. Nunca anime `top`, `left`, `width`,
  `height` ou `box-shadow` em loop
- Nada de `filter: blur()` ou `backdrop-filter` em camada grande ou dentro da
  cena 3D. A fumaça é uma única camada com gradientes radiais
- **Lata:** no máximo 20 faces (18 no celular) — um cilindro de 20 faces não
  se distingue de um círculo nesse tamanho. Esconda as faces de costas. O
  giro é uma animação do navegador (Web Animations API), e a rolagem só muda
  o `playbackRate`. Não gire a lata em `requestAnimationFrame`
- Bolhas e faíscas em animação CSS, não em `<canvas>` redesenhado a cada
  quadro
- Ilustrações do carrossel só animam no card da frente e com o carrossel na
  tela
- No laço em JavaScript: leia todas as medidas primeiro, escreva depois, e
  só escreva quando o valor mudar. Com a página parada, o laço não mexe em
  nada
- Não troque variável CSS num elemento que tem muitos filhos a cada quadro
  (a cena 3D, a lata, os cards); escreva o `transform` direto no elemento
- Seções abaixo do topo com `content-visibility: auto` e
  `contain-intrinsic-size`; os links internos recalculam o destino durante
  a rolagem
- Sem `will-change` permanente em dezenas de elementos (por exemplo, em cada
  letra)
- Grão de filme estático; animações do topo pausadas quando ele sai da tela

## 10. Técnico

- **Entrega:** um único `index.html`, sem instalar nada, pronto para arrastar
  no Netlify Drop. Logo embutida em WebP (base64) — cada imagem entra uma vez
  só no arquivo. A coruja vai inline como SVG. Sem frameworks; JavaScript
  puro. Só Google Fonts como recurso externo
- **Dados editáveis num bloco só**, no topo do script:
  ```js
  var LOJA = {
    instagram: 'cvcconveniencia',
    whatsapp: '',       // só números, com DDI e DDD: '5561999990000'
    pedirIdade: true    // false desliga a pergunta de idade
  };
  ```
  Com `whatsapp` vazio, os botões abrem `ig.me/m/cvcconveniencia` e dizem
  "Direct". Preenchido, abrem `wa.me/<número>?text=<mensagem>` com mensagem
  citando o item, e os textos viram "WhatsApp" sozinhos
- **Celular primeiro:** confira em 390 px; nenhuma rolagem lateral (atenção
  aos elementos 3D, que ficam mais largos que a caixa antes de aparecer);
  botões com pelo menos 44 px
- **SEO:** `<title>` "CVC Conveniência — a noite pede, a CVC tem", meta
  description, Open Graph, favicon da logo. JSON-LD `ConvenienceStore` com
  `name`, `logo` e `sameAs` (Instagram) — `telephone`, `address` e
  `openingHours` só quando confirmados
- **Acessibilidade:** a pergunta de idade é um diálogo (`role="dialog"`,
  `aria-modal`) com foco no botão "Sim"; títulos quebrados em letras levam
  `aria-label` com o texto inteiro; foco visível; contraste AA; carrossel
  navegável por teclado
- **Funciona sem JavaScript:** o conteúdo aparece mesmo se o script falhar;
  a abertura e a pergunta de idade só existem quando o JavaScript roda

## 11. Checklist de aceite

- [ ] Todo botão de pedido abre o Direct (ou o WhatsApp configurado), com a
      palavra certa no texto do botão
- [ ] Só as categorias confirmadas aparecem; nenhum preço, horário, entrega,
      nota ou marca de terceiro
- [ ] Pergunta de idade funciona com mouse e teclado, e não se repete
      depois do "sim"
- [ ] Avisos "Beba com moderação", "proibida para menores de 18 anos" e "Se
      beber, não dirija" presentes
- [ ] Coruja grande sempre em vetor; `logo.png` só em tamanho pequeno
- [ ] Sem rolagem lateral em 390 px; sem erro no console
- [ ] Fluido no celular: ~60 quadros por segundo no topo e rolando
- [ ] "Reduzir movimento" desliga as animações longas
