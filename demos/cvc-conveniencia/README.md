# Demo — CVC Conveniência

Página de marca com abertura cinematográfica para
[@cvcconveniencia](https://www.instagram.com/cvcconveniencia/). É um arquivo
único (`index.html`, ~145 KB) com a logo embutida. Para publicar, arraste o
arquivo em [app.netlify.com/drop](https://app.netlify.com/drop).

## O que tem na página

| Bloco | O que faz |
|---|---|
| Abertura | A coruja da logo se desenha em traço laranja, se preenche e pisca, flutuando sobre ondas de "localização" em 3D. O contador vai de 000 a 100 com mensagens ("Gelando as bebidas", "Acordando a coruja"...) |
| Pergunta de idade | "Você tem 18 anos ou mais?" dentro da própria abertura. Quem responde "sim" entra com um círculo laranja que se abre a partir da coruja. A resposta fica guardada no navegador, então a pergunta não se repete |
| Topo | "A noite pede. A CVC *tem.*" com as letras subindo uma a uma. Ao lado, uma lata 3D girando com a coruja e a marca no rótulo, cubos de gelo 3D e bolhas subindo. A lata gira mais rápido quando a página rola e inclina com o mouse |
| Faixas | Categorias correndo em sentidos opostos, entortando com a velocidade da rolagem |
| Seleção da casa | Carrossel 3D com as categorias confirmadas (por padrão, cervejas, gelo, carvão e snacks; há 9 prontas). Cada item tem bolhas, gotas, brasas ou fumaça animadas e um botão de pedido |
| A CVC | Texto que acende palavra por palavra. A coruja ao lado pisca e segue o cursor com os olhos |
| Como pedir | Três passos em cartões com inclinação 3D |
| Instagram | Celular em 3D com o perfil estilizado, que inclina com o mouse |
| Final | "Bateu a vontade? Chama a *coruja*." com brilho que cresce conforme a rolagem |

Rodapé e carrossel levam o aviso "Beba com moderação · venda proibida para
menores de 18 anos". Com "reduzir movimento" ligado no sistema, as animações
longas são desligadas. No computador, a roda do mouse tem rolagem suave com
inércia; no celular, a rolagem é a nativa do aparelho.

## Para continuar fluida

Num teste com o processador desacelerado 4×, simulando um celular comum, a
página roda a ~60 quadros por segundo no topo e rolando, e a 44–51 no
carrossel. Antes da otimização rodava a 12–20. Se for editar, mantenha estas
regras:

- **Animar só `transform` e `opacity`.** Animar `top`, `width` ou `left`
  recalcula o layout a cada quadro
- **Nada de `filter: blur()` ou `backdrop-filter` em camada grande ou que se
  mexe.** Para suavizar, use gradiente
- **Movimento contínuo por CSS, não por script.** As bolhas, o gelo e o giro
  da lata são animações que o navegador executa sozinho. O script só ajusta o
  ritmo
- **No laço do script, ler tudo primeiro e escrever depois, e só quando o
  valor muda.** Ler a posição de algo logo depois de mudar um estilo força o
  navegador a recalcular a página no meio do quadro
- **Não trocar variável CSS num elemento que tem muitos filhos.** Isso
  recalcula todos eles; escreva o `transform` direto no elemento
- **As seções abaixo do topo usam `content-visibility: auto`.** O navegador
  pula o desenho delas enquanto estão fora da tela

## De onde vieram os dados — leia antes de mostrar

**O Instagram não abre sem login, e não há nada público sobre a loja.** A busca
só traz a agência CVC Viagens e outras conveniências. Portanto:

- **A logo** é a imagem enviada. A coruja laranja foi vetorizada a partir dela
  para aparecer nítida em tamanho grande (loader, lata, seção "A CVC" e final).
  A imagem original, com o fundo de garrafas, aparece no menu, no rodapé, no
  perfil do celular e como ícone da aba
- **As 6 categorias são as típicas de conveniência.** Não vieram do perfil.
  Confirme com o dono o que ele vende de fato e tire o que não tiver (por
  exemplo, vinho). As ilustrações são desenhadas em código, sem marca de
  produto nenhuma
- **Não há endereço, horário nem WhatsApp**, porque nada disso foi encontrado.
  Os botões de pedido abrem o Direct do Instagram (`ig.me/m/cvcconveniencia`)
- **O celular da seção Instagram é uma ilustração.** Mostra só nome, @ e a
  logo, sem número de seguidores nem posts reais

**Ficaram de fora de propósito:** preço, depoimento, nota, horário, entrega e
promoção. Seguindo a regra do `gerador/COMO-USAR.md`, nada disso entra sem
dado real.

## Prompt para refazer com os dados reais

[`../../prompts/cvc-conveniencia.md`](../../prompts/cvc-conveniencia.md) descreve
esta página inteira num prompt, no mesmo formato dos prompts de restaurante.
Serve para regenerar o site quando o dono confirmar WhatsApp, endereço,
horário e produtos, ou para gerar em outra ferramenta. A coruja vetorizada
que ele pede como anexo está em `fonte/img/coruja.svg`.

## Como editar

### Preencher o que o dono confirmar

Tudo fica num bloco só, no começo do `<script>` do `fonte/template.html`.
Campo vazio = a informação não aparece em lugar nenhum:

```js
var LOJA={
  instagram:'cvcconveniencia',
  whatsapp:'',        // ex.: '5561999990000' (DDI + DDD + número)
  pedirIdade:true,    // false desliga a pergunta de idade
  categorias:['cervejas','gelo','carvao','snacks'],
  endereco:'',        // preenchido = seção "Onde estamos" com mapa
  horario:'',         // ex.: 'Todos os dias, das 16h às 2h'
  horarioSchema:'',   // o mesmo no formato do Google: 'Mo-Su 16:00-02:00'
  entrega:'',         // ex.: 'Entregamos em Taguatinga Norte e Sul'
  pagamento:'',       // ex.: 'Pix, cartão e dinheiro'
  logoUrl:''          // endereço público da logo, depois de publicar
};
```

- **`whatsapp`:** preenchido, todos os botões abrem o WhatsApp com mensagem
  pronta citando o item, e os textos "Direct" viram "WhatsApp" sozinhos
- **`categorias`:** quais cards entram no carrossel, na faixa laranja e nos
  destaques do celular. Opções: `cervejas`, `destilados`, `vinhos`,
  `energeticos`, `agua`, `gelo`, `carvao`, `snacks`, `doces`. O padrão é a
  reserva combinada no prompt. Tabacaria não tem card: a Lei 9.294/1996
  proíbe propaganda de tabaco fora do ponto de venda
- **`endereco`, `horario`, `entrega`, `pagamento`:** qualquer um preenchido
  faz aparecer a seção "Onde estamos" e o link no menu. Com endereço, entram
  o mapa e o botão do Google Maps
- **JSON-LD:** telefone, endereço, horário e logo só entram quando
  preenchidos

### Gerar o index.html de novo

```
python3 fonte/build.py
```

O script embute a logo (`fonte/img/logo.webp`) e o desenho da coruja
(`fonte/owl.json`) no `index.html`. Precisa só de Python 3.

### Trocar ilustração por foto

Se o dono mandar fotos reais, cada card do carrossel pode receber uma foto no
lugar da ilustração, como foi feito na demo da Pousada do Sol. Basta trocar o
`<svg class="prod">` do card por `<img src="{{nome}}">` e salvar o
`nome.webp` em `fonte/img/`.
