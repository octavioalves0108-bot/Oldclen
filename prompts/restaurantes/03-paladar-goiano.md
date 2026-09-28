# Prompt — site do Restaurante Paladar Goiano (Taguatinga Norte)

**Como usar:** junte os arquivos da seção 5 (logo e fotos do Instagram dele),
confirme os itens da seção 3 pelo WhatsApp ou pelo Google Maps, e então copie
tudo que está abaixo da linha e cole numa IA de código, como o Claude.

---

Você é um designer e desenvolvedor front-end sênior, especialista em sites
de restaurante com acabamento premium. Crie o site de apresentação do
**Restaurante Paladar Goiano**, restaurante de comida goiana com churrasco
servido na mesa, na Comercial Norte de Taguatinga (Brasília-DF).

## 1. Objetivo

Uma página única, que abre com uma animação de carregamento de marca, e que
leva o visitante a **vir almoçar** ou a **chamar no WhatsApp** (reserva de
mesa para grupo, dúvida, delivery). O público são famílias e grupos de
trabalho de Taguatinga que querem comer bem e à vontade no almoço. Tom:
farto, generoso, familiar, com orgulho goiano — a brasa como protagonista.

## 2. Dados reais do negócio — use exatamente estes

| Campo | Valor |
|---|---|
| Nome | Restaurante Paladar Goiano |
| Instagram | [@restaurantepaladargoiano](https://www.instagram.com/restaurantepaladargoiano/) |
| WhatsApp | (61) 99325-9445 — link `https://wa.me/5561993259445` |
| Telefone fixo | (61) 3628-8289 |
| E-mail | paladargoianorestaurante@gmail.com |
| Endereço | QND 13, Loja 10 — Comercial Norte, Taguatinga Norte, Brasília-DF |
| Horário | Almoço, das 11h às 14h30 (ver seção 3) |
| Proposta | Self-service à vontade com churrasco servido na mesa, no estilo rodízio, e buffet completo de comida caseira e saladas. Ambiente familiar |
| Delivery | iFood (peça o link da loja a ele) |

## 3. Dados a confirmar antes de publicar

- **Preço do almoço.** Duas fontes dão valores diferentes (uma diz R$ 26,99 e
  R$ 31,99; outra, R$ 31,99 e R$ 36,99). **Não publique preço.** Se ele
  quiser o preço no site, só com o valor confirmado por ele e a data
- **Cortes do churrasco.** Uma fonte lista contra-filé, fraldinha com alho,
  filé grelhado, cupim, lombo, linguiça, sobrecoxa, pão de alho e abacaxi
  assado — mas veio traduzida de outro idioma. Confirme os nomes com ele.
  Reserva: "Cortes variados passando na mesa, direto da brasa"
- **Sobremesa inclusa.** Uma fonte diz que sim. Não afirme até confirmar
- **Dias da semana.** Confirme se abre todos os dias. Reserva: "Almoço, das
  11h às 14h30"
- **Qual número é o WhatsApp.** O celular (61) 99325-9445 é o mais provável.
  Confirme
- **Reserva para grupos.** Existe uma página dele no Facebook com "reserva"
  no nome. Pergunte se aceita reserva de mesa — se sim, o botão principal
  vira "Reservar mesa"

## 4. O que nunca inventar

- **Preço** (ver seção 3). Onde caberia preço: "Consulte no WhatsApp"
- **Depoimento ou nota.** Só entra texto copiado de avaliação real do
  Google, com o primeiro nome do autor. Se eu não mandar avaliações, **não
  crie a seção de depoimentos**. Não exiba nota de avaliação nenhuma
- **História, "desde 19xx", prêmio, número de clientes, selo**
- **Foto.** Não gere foto de carne ou prato por IA nem use banco de imagem
  fingindo ser do restaurante. Sem foto, use ilustração (seção 6)

## 5. Arquivos que eu anexo

- `logo.png` — a logo do Instagram
- `hero.jpg` — a melhor foto do churrasco (espeto passando na mesa,
  picanha fatiada ou brasa)
- `buffet.jpg` — o buffet
- `corte-1.jpg` … `corte-6.jpg` — cortes e pratos
- `salao.jpg` — o salão cheio, de preferência (opcional)

Use fotos pequenas em molduras, nunca esticadas em tela cheia. Faltou
alguma? Troque por ilustração em SVG.

## 6. Direção de arte

- **Conceito:** "a brasa goiana". Escuro e quente: fundo de carvão, luz de
  brasa, fumaça leve, madeira. A comida é o brilho da página
- **Paleta:** carvão (fundo), laranja-brasa (primária), vermelho-urucum
  (acento), amarelo-pequi (detalhe), creme (texto), madeira escura (cartões).
  **Se a logo tiver cores próprias, elas mandam:** ajuste a paleta à logo
- **Tipografia:** uma serifada robusta para títulos (Fraunces em peso alto,
  ou Zilla Slab), com itálico nos destaques, e uma sans para texto
  (Manrope). Google Fonts
- **Textura:** grão leve e estático; veio de madeira sutil nos cartões
- **Ilustração, onde faltar foto:** traço de brasa — espeto, faca e garfo
  cruzados, chama, pequi, panela de ferro, folha

## 7. Estrutura da página, seção por seção

1. **Abertura (loader, 2,5 a 3 s):** um carvão desenhado em traço acende —
   brasas vermelhas pulsam, fagulhas sobem; as letras de "Paladar Goiano"
   surgem uma a uma, como se iluminadas pela brasa; contador de 000 a 100
   com frases ("Acendendo a brasa", "Afiando a faca", "Montando o buffet").
   Sai com um clarão laranja que se abre do centro, revelando o topo
2. **Menu fixo:** logo, links (O rodízio, O buffet, Como chegar) e botão
   "Chamar no WhatsApp". Some ao rolar para baixo, volta ao rolar para cima
3. **Topo:** título grande com as letras entrando uma a uma — sugestão:
   "Comida goiana *à vontade*, com churrasco na mesa." Subtítulo: "Almoço na
   Comercial Norte de Taguatinga, das 11h às 14h30." Botões "Chamar no
   WhatsApp" e "Como funciona". A foto `hero.jpg` numa moldura que inclina em
   3D com o mouse; fagulhas subindo ao fundo
4. **Faixa correndo:** "Churrasco na mesa ✦ Buffet completo ✦ Comida goiana ✦
   Saladas ✦ À vontade ✦"
5. **A roda do rodízio (o efeito 3D principal):** os cortes (seção 3) e o
   buffet dispostos num anel 3D que gira como uma roda de espetos — cada
   item é um cartão com foto ou ilustração e nome, posicionado com
   `rotateY` e `translateZ` num anel. O anel gira devagar sozinho, acelera
   com a rolagem, pode ser arrastado e para no item clicado, trazendo-o para
   a frente com o nome em destaque. Sem preço
6. **Como funciona:** três passos com inclinação 3D — "Monte o prato no
   buffet", "O churrasco passa na mesa", "Coma à vontade" — com números
   grandes vazados
7. **O buffet:** foto `buffet.jpg` com revelação por cortina e texto que
   acende palavra por palavra — "Buffet completo de comida caseira e
   saladas, e o churrasco chegando na mesa enquanto você almoça. Do jeito
   goiano: farto e sem pressa."
8. **Delivery:** cartão com o iFood (quando ele passar o link) e o WhatsApp
9. **Como chegar:** endereço, horário, telefones, botão "Abrir no Google
   Maps"
   (`https://www.google.com/maps/search/?api=1&query=Restaurante+Paladar+Goiano+QND+13+Taguatinga`)
   e mapa ilustrado com o pino pulsando
10. **Chamada final:** "A brasa tá acesa. *A mesa é sua.*" com clarão laranja
    crescendo ao fundo conforme a rolagem, botão de WhatsApp e o @ do
    Instagram
11. **Rodapé:** logo, Instagram, WhatsApp, fixo, e-mail, horário, endereço e
    ano automático
12. **Botão flutuante de WhatsApp** depois do topo

Toda chamada abre o WhatsApp com mensagem pronta, ex.: "Olá! Vim pelo site do
Paladar Goiano e quero saber sobre o almoço de hoje."

## 8. Motion e 3D

- Letras dos títulos entrando uma a uma, com a palavra mascarada
- Elementos entrando ao rolar: subir com fade, desfoque que clareia,
  revelação de imagem por cortina
- Fagulhas de brasa subindo (animação CSS, poucas e leves)
- Roda do rodízio em 3D: giro automático, arraste, aceleração com a rolagem
- Passos com inclinação 3D ao passar o mouse; moldura do topo seguindo o
  mouse; no celular, balanço lento automático
- Botões magnéticos no computador; brilho que atravessa o botão principal
- Barra de progresso da rolagem
- Respeite "reduzir movimento": sem loader longo, sem giro automático, sem
  fagulhas

## 9. Regras de desempenho (a página tem que ser fluida no celular)

- Anime apenas `transform` e `opacity`. Nunca anime `top`, `left`, `width`,
  `height` ou `box-shadow` em loop
- Nada de `filter: blur()` ou `backdrop-filter` em camada grande ou que se
  mexe. Para suavizar, use gradiente
- O giro contínuo da roda é uma animação do navegador (CSS ou Web
  Animations API), e a rolagem só muda o ritmo (`playbackRate`). Não
  recalcule a roda em `requestAnimationFrame` a cada quadro
- Fagulhas em animação CSS, não em `<canvas>` redesenhado a cada quadro
- Se houver laço em JavaScript: leia todas as medidas primeiro, escreva
  depois, e só escreva quando o valor mudar. Com a página parada, o laço não
  mexe em nada
- Não troque variável CSS num elemento que tem muitos filhos a cada quadro;
  escreva o `transform` direto no elemento
- Seções abaixo do topo com `content-visibility: auto` e
  `contain-intrinsic-size`
- Sem `will-change` permanente em dezenas de elementos
- Pause animações que estão fora da tela

## 10. Técnico

- **Entrega:** um único `index.html`, sem instalar nada, pronto para arrastar
  no Netlify Drop. Imagens embutidas em WebP (base64) ou numa pasta
  `assets/` — se embutir, cada imagem entra uma vez só. Sem frameworks;
  JavaScript puro. Só Google Fonts como recurso externo
- **Celular primeiro:** confira em 390 px; nenhuma rolagem lateral; botões
  com pelo menos 44 px. A roda do rodízio no celular mostra no máximo 5
  itens visíveis e continua arrastável com o dedo
- **SEO:** `<title>` "Paladar Goiano — churrasco e comida goiana à vontade em
  Taguatinga", meta description, Open Graph, favicon da logo e JSON-LD
  `Restaurant` com `name`, `servesCuisine` ("Goiana", "Churrasco",
  "Brasileira"), `telephone`, `email`, `address`, `openingHours`
  (11:00–14:30) e `sameAs` com o Instagram
- **Acessibilidade:** textos alternativos reais, foco visível, contraste AA,
  roda do rodízio navegável por teclado (setas) e com botões anterior e
  próximo
- **Funciona sem JavaScript:** conteúdo visível mesmo se o script falhar; a
  roda vira uma grade simples

## 11. Checklist de aceite

- [ ] Todo botão abre o WhatsApp (61) 99325-9445, com mensagem pronta
- [ ] Nenhum preço, depoimento, nota ou afirmação inventada; cortes só com
      os nomes confirmados
- [ ] Roda do rodízio gira, acelera com a rolagem, pode ser arrastada e
      para no item clicado
- [ ] Loader entre 2,5 e 3 s na primeira visita e mais curto nas seguintes
- [ ] Sem rolagem lateral em 390 px; sem erro no console
- [ ] Fluido no celular: rolagem sem engasgo, animações a ~60 quadros por
      segundo
- [ ] "Reduzir movimento" desliga as animações longas
