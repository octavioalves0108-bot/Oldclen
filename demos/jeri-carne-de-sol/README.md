# Demo — Jeri Carne de Sol (Taguatinga Norte)

Site de apresentação sob medida, com o conceito "o pôr do sol de Jeri no seu
almoço". A abertura mostra o sol se pondo atrás da duna. O topo é uma cena de
dunas em 3D, seguido do cardápio em carrossel, da seção da carne de sol, de
como pedir (salão, telefone, iFood) e de como chegar.

| Arquivo | O que é |
|---|---|
| `index.html` | O site inteiro, sem dependências além das fontes do Google |
| `og.jpg` | A imagem que aparece quando o link é mandado no WhatsApp |

## Publicar em 1 minuto

1. Abra [app.netlify.com/drop](https://app.netlify.com/drop) e arraste **a pasta
   `jeri-carne-de-sol` inteira** (não só o `index.html`, senão a imagem do
   WhatsApp não vai junto)
2. No painel do site: **Site configuration → Change site name** →
   `jericarnedesol`. O endereço vira `jericarnedesol.netlify.app`
3. Mande o link para o seu próprio WhatsApp e confira a pré-visualização

Se o nome estiver em uso, troque `jericarnedesol.netlify.app` pelo endereço
novo em todo o `index.html` (buscar e substituir: são 6 lugares).

## Configuração: um bloco só, no fim do arquivo

Procure por `var LOJA` no `index.html`:

```js
var LOJA = {
  whatsapp: '',
  telefone: '556133543056',
  ifood: 'https://www.ifood.com.br/delivery/...',
  cardapio: ''
};
```

- **`whatsapp` vazio** (como está): todo botão principal **liga** para
  (61) 3354-3056 e mostra "Ligar". O "Pedir este" do carrossel abre o iFood
- **`whatsapp: '5561999999999'`** (DDI 55, DDD e número, só dígitos): os botões
  viram **WhatsApp** com mensagem pronta ("Olá! Vim pelo site e quero…"). O
  "Pedir este" manda o nome do prato, e o cartão "Pelo telefone" vira "Pelo
  WhatsApp" com o número certo. O telefone fixo continua em "Como chegar" e no
  rodapé
- **`cardapio`**: com o link do cardápio online (Cardápio Web), aparece o botão
  "Cardápio completo" embaixo do carrossel

Sem JavaScript, os botões ligam para o fixo, que é o padrão seguro.

## Antes de publicar: confirmar com o dono

Nada abaixo foi inventado. Onde a informação não estava confirmada, o site usa
o texto provisório, e o trecho tem um comentário `CONFIRMAR` no `index.html`.

| O que confirmar | O que o site mostra hoje | O que fazer quando ele confirmar |
|---|---|---|
| O WhatsApp é o fixo (61) 3354-3056 ou outro celular? | Botões "Ligar" | Preencher `LOJA.whatsapp` |
| Dias de funcionamento | "Almoço, das 11h às 15h", sem dias | Buscar `11h às 15h` e acrescentar os dias nesses trechos; no bloco `application/ld+json`, acrescentar `"dayOfWeek"` |
| Nome da casa: "Jeri Carne de Sol" ou "Jericoacoara Carne de Sol"? | "Jeri Carne de Sol" | Se mudar, buscar e substituir o nome |
| Existe unidade na Asa Norte? | Não mencionada | Se existir e ele quiser divulgar, entra em "Como chegar" |
| Link do cardápio online | Botão escondido | Preencher `LOJA.cardapio` |

## O que ainda falta mandar

Os anexos não chegaram. O briefing previa a logo, `hero.jpg`, os pratos de 1 a
5 e `ambiente.jpg`. Por isso:

- **Logo:** no menu e no rodapé há uma assinatura provisória ("Jeri" + sol na
  duna), e o favicon é o mesmo sol. Quando a logo chegar, ela entra nesses
  lugares e a paleta é ajustada às cores dela
- **Fotos:** o cartão do topo, os cinco pratos do carrossel e a seção da carne
  de sol usam ilustração em traço grosso. É ilustração declarada (o texto
  alternativo diz "Ilustração"), não foto falsa

Não use foto de banco de imagem nem gerada por IA fingindo ser do restaurante.
As fotos reais do iFood do próprio restaurante servem, se o dono mandar os
arquivos.

### Trocar uma ilustração por foto

1. Converta a foto para WebP em [squoosh.app](https://squoosh.app) (800 px de
   largura basta) e salve dentro da pasta, por exemplo `prato-1.webp`
2. No `index.html`, no prato do carrossel, troque o bloco
   `<div class="cf-media" …> … </div>` por:

   ```html
   <div class="cf-media" role="img" aria-label="Carne de Sol Completa Jerí servida no Jeri" style="background:url(prato-1.webp) center/cover"></div>
   ```

   No cartão do topo e na seção da carne de sol, a lógica é a mesma, com os
   blocos `cartao-img` e `carne-img`
3. Publique de novo arrastando a pasta no Netlify Drop

## O que o site já faz sozinho

- A abertura dura cerca de 2,9 s na primeira visita e 1,5 s nas seguintes
- "Pedir agora" abre duas opções: ligar (ou WhatsApp) e iFood
- Os preços não aparecem. No lugar deles, cada prato diz "Preço: consulte"
- Quem ativou **"reduzir movimento"** vê o site sem abertura, sem partículas,
  sem deriva das dunas e sem carrossel automático
- Sem JavaScript, o conteúdo aparece todo e os botões ligam para o fixo
