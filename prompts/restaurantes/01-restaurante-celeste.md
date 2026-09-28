# Prompt — site do Restaurante Celeste (Taguatinga Norte)

**Como usar:** junte os arquivos da seção 5 (logo e fotos do Instagram dele),
confirme os itens da seção 3 pelo WhatsApp ou pelo Google Maps, e então copie
tudo que está abaixo da linha e cole numa IA de código, como o Claude.

---

Você é um designer e desenvolvedor front-end sênior, especialista em sites
de restaurante com acabamento premium. Crie o site de apresentação do
**Restaurante Celeste**, um restaurante de comida caseira em Taguatinga Norte
(Brasília-DF).

## 1. Objetivo

Uma página única, que abre com uma animação de carregamento de marca, e que
converte visita em **mensagem no WhatsApp** — para reservar a feijoada,
pedir marmita ou tirar dúvida. O público é o morador e o trabalhador de
Taguatinga, Águas Claras e Ceilândia que quer almoço caseiro de verdade.
Tom: acolhedor, afetivo, "comida de vó", sem ser brega.

## 2. Dados reais do negócio — use exatamente estes

| Campo | Valor |
|---|---|
| Nome | Restaurante Celeste |
| Instagram | [@restauranteceleste](https://www.instagram.com/restauranteceleste/) |
| WhatsApp | (61) 3256-8503 — link `https://wa.me/556132568503` |
| Endereço | QNH 10, Taguatinga Norte, Brasília-DF (ver seção 3) |
| Horário | Segunda a sábado, 11h às 14h30 |
| Proposta | Comida caseira com sabor de comida de vó, ambiente familiar, tudo feito na hora, cardápio variado |
| Destaques da semana | Feijoada às sextas e sábados, com vagas limitadas e reserva pelo WhatsApp. Baião de dois e bobó de camarão às quintas e sábados |
| Serviços | Almoço no local, delivery e marmitas |
| Área de entrega | Taguatinga, Águas Claras e Ceilândia |

## 3. Dados a confirmar antes de publicar

Estes vieram de fontes que se contradizem ou envelheceram. Não publique sem
confirmação — use o texto reserva indicado até lá.

- **Número do endereço:** uma fonte diz "QNH 10, lote 24", um post do próprio
  perfil diz "QNH 10, casa 10". Reserva: "QNH 10 — Taguatinga Norte"
- **Se o WhatsApp é mesmo esse número fixo** (WhatsApp Business aceita fixo).
  Se ele passar um celular, troque em todos os links
- **Dias do baião de dois e do bobó de camarão.** Reserva: "Pratos especiais
  durante a semana — pergunte no WhatsApp"
- **Pratos do dia de segunda a quarta.** Reserva: "Prato do dia — consulte no
  WhatsApp"
- **Taxa e raio de entrega.** Reserva: não mencione valores

## 4. O que nunca inventar

- **Preço.** Não publique nenhum valor. Onde caberia preço, escreva
  "Consulte no WhatsApp"
- **Depoimento ou nota de avaliação.** Só entra texto copiado de uma
  avaliação real do Google, com o primeiro nome do autor. Se eu não mandar
  avaliações, **não crie a seção de depoimentos**
- **Prêmio, "desde 19xx", número de clientes, selo** ou qualquer afirmação
  que não esteja nas seções 2 e 3
- **Foto.** Não gere foto de prato por IA nem use banco de imagem fingindo
  ser do restaurante. Sem foto, use ilustração (seção 6)

## 5. Arquivos que eu anexo

- `logo.png` — a logo do Instagram dele
- `hero.jpg` — a melhor foto de prato (de preferência a feijoada)
- `prato-1.jpg` … `prato-6.jpg` — pratos do cardápio
- `ambiente.jpg` — salão ou fachada (opcional)

Use as fotos em tamanho moderado, dentro de molduras, se forem de baixa
resolução — nunca estique uma foto pequena em tela cheia. Se faltar alguma,
troque por ilustração em SVG no estilo da página.

## 6. Direção de arte

- **Conceito:** "cozinha afetiva". Luz de meio-dia entrando pela janela,
  panela de barro, vapor subindo. O nome Celeste pede um azul-céu, que aqui
  entra como acento — o calor vem da comida
- **Paleta:** creme quente (fundo), terracota de panela de barro (primária),
  azul-celeste suave (acento), marrom de feijão (texto escuro), verde-couve
  (pontos de detalhe). **Se a logo tiver cores próprias, elas mandam:**
  ajuste a paleta à logo
- **Tipografia:** uma serifada acolhedora para títulos (Fraunces ou DM Serif
  Display, com itálico) e uma sans limpa para texto (Manrope). Google Fonts
- **Textura:** grão de papel bem leve, estático. Nada de toalha xadrez, nada
  de clipart
- **Ilustração, onde faltar foto:** traço fino, linha única, na cor terracota
  — panela, colher de pau, cumbuca, folha de couve, prato com vapor

## 7. Estrutura da página, seção por seção

1. **Abertura (loader, 2,5 a 3 s):** uma panela de barro desenhada em traço
   que se preenche de cor; três fios de vapor sobem e se desfazem; as letras
   de "Restaurante Celeste" surgem uma a uma, de baixo para cima, com leve
   desfoque; um contador de 000 a 100 com frases que trocam ("Acendendo o
   fogão", "Temperando o feijão", "Pondo a mesa"). Sai com uma cortina que
   sobe como vapor, revelando o topo
2. **Menu fixo:** logo, links (Cardápio da semana, Feijoada, Delivery, Como
   chegar) e botão "Pedir no WhatsApp". Some ao rolar para baixo, volta ao
   rolar para cima
3. **Topo:** título grande com as letras entrando uma a uma — sugestão:
   "Comida de vó, *feita na hora*." Subtítulo: "Almoço caseiro em Taguatinga
   Norte, de segunda a sábado, das 11h às 14h30." Botões "Reservar a
   feijoada" e "Ver o cardápio da semana". Foto `hero.jpg` numa moldura com
   leve inclinação 3D que segue o mouse
4. **Faixa correndo:** "Feijoada sexta e sábado ✦ Comida caseira ✦ Marmitas ✦
   Delivery em Taguatinga, Águas Claras e Ceilândia ✦"
5. **Cardápio da semana (o efeito 3D principal):** seis cartões, de segunda a
   sábado, que viram em 3D (flip) ao passar o mouse ou tocar. Na frente, o
   dia; no verso, o destaque do dia (sexta e sábado: feijoada; quinta e
   sábado: baião de dois e bobó — ver seção 3; nos outros: "Prato do dia —
   consulte no WhatsApp"). O cartão de hoje vem destacado e já virado,
   calculado pelo dia da semana do visitante. Domingo: aviso "Hoje estamos
   fechados — volte amanhã a partir das 11h"
6. **Feijoada:** seção de impacto com a melhor foto, texto curto sobre a
   feijoada de sexta e sábado, o aviso "vagas limitadas" e o botão
   "Reservar meu lugar", com mensagem pronta no WhatsApp: "Olá! Quero
   reservar a feijoada de [sexta/sábado] para [número] pessoas."
7. **Pratos em destaque:** carrossel 3D (coverflow) com as fotos
   `prato-1` a `prato-6`, nome do prato e botão "Pedir este". Arrastar,
   clicar, setas do teclado e troca automática. Sem preço
8. **Delivery e marmitas:** três cartões (Almoço no local, Delivery, Marmitas)
   e um mapinha ilustrado com Taguatinga, Águas Claras e Ceilândia acendendo
   em sequência
9. **Sobre:** um parágrafo que acende palavra por palavra conforme a rolagem —
   "Aqui a comida é feita como em casa: na hora, com tempero de vó e sem
   pressa. Tem feijoada de sexta e sábado, prato do dia de segunda a sábado e
   marmita pra quem não pode parar."
10. **Como chegar:** endereço, horário, botão "Abrir no Google Maps"
    (`https://www.google.com/maps/search/?api=1&query=Restaurante+Celeste+QNH+10+Taguatinga+Norte`)
    e mapa ilustrado com o pino pulsando
11. **Chamada final:** "Bateu a fome? *A panela tá no fogo.*" com botão grande
    de WhatsApp e o @ do Instagram
12. **Rodapé:** logo, Instagram, WhatsApp, horário, endereço e ano automático
13. **Botão flutuante de WhatsApp** que aparece depois do topo

Todas as chamadas levam ao WhatsApp com mensagem pronta citando de onde a
pessoa veio (ex.: "Olá! Vim pelo site e quero pedir uma marmita.").

## 8. Motion e 3D

- Letras dos títulos entrando uma a uma, com a palavra mascarada (a letra
  sobe de trás de uma linha invisível)
- Elementos entrando ao rolar: subir com fade, desfoque que clareia,
  revelação de imagem por cortina
- Vapor animado saindo das ilustrações de panela
- Moldura do topo com inclinação 3D seguindo o mouse; no celular, balanço
  lento automático
- Cartões da semana com flip 3D; carrossel coverflow 3D nos pratos
- Botões magnéticos no computador; brilho que atravessa o botão principal
- Barra de progresso da rolagem no topo da tela
- Respeite "reduzir movimento" do sistema: sem loader longo, sem autoplay,
  sem vapor contínuo

## 9. Regras de desempenho (a página tem que ser fluida no celular)

- Anime apenas `transform` e `opacity`. Nunca anime `top`, `left`, `width`,
  `height` ou `box-shadow` em loop
- Nada de `filter: blur()` ou `backdrop-filter` em camada grande ou que se
  mexe. Para suavizar, use gradiente
- Movimento contínuo (vapor, faixa correndo, balanço) em animação CSS, não
  em `requestAnimationFrame`
- Se houver laço em JavaScript: leia todas as medidas primeiro, escreva
  depois, e só escreva quando o valor mudar. Com a página parada, o laço não
  mexe em nada
- Não troque variável CSS num elemento que tem muitos filhos a cada quadro;
  escreva o `transform` direto no elemento
- Seções abaixo do topo com `content-visibility: auto` e
  `contain-intrinsic-size`
- Sem `will-change` permanente em dezenas de elementos (por exemplo, em cada
  letra)
- Pause animações que estão fora da tela

## 10. Técnico

- **Entrega:** um único `index.html`, sem instalar nada, pronto para arrastar
  no Netlify Drop. Imagens embutidas em WebP (base64) ou numa pasta
  `assets/` ao lado — se embutir, cada imagem entra uma vez só. Sem
  frameworks; JavaScript puro. Só Google Fonts como recurso externo
- **Celular primeiro:** confira em 390 px de largura; nenhuma rolagem
  lateral; botões com pelo menos 44 px de altura
- **SEO:** `<title>` "Restaurante Celeste — comida caseira em Taguatinga
  Norte", meta description, Open Graph, favicon da logo e JSON-LD
  `Restaurant` com `name`, `servesCuisine` ("Brasileira", "Caseira"),
  `telephone`, `address`, `openingHoursSpecification` (seg–sáb,
  11:00–14:30), `acceptsReservations: true` e `sameAs` com o Instagram
- **Acessibilidade:** textos alternativos reais nas fotos, foco visível,
  contraste AA, navegação por teclado no carrossel e nos cartões
- **Funciona sem JavaScript:** o conteúdo aparece mesmo se o script falhar;
  o loader só existe quando o JavaScript roda

## 11. Checklist de aceite

- [ ] Todo botão abre o WhatsApp certo, com mensagem pronta
- [ ] Nenhum preço, depoimento ou afirmação inventada
- [ ] O cartão do dia de hoje aparece destacado
- [ ] Loader entre 2,5 e 3 s na primeira visita e mais curto nas seguintes
- [ ] Sem rolagem lateral em 390 px; sem erro no console
- [ ] Fluido no celular: rolagem sem engasgo, animações a ~60 quadros por
      segundo
- [ ] "Reduzir movimento" desliga as animações longas
