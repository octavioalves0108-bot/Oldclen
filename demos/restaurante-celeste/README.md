# Demo — Restaurante Celeste (Taguatinga Norte)

Site de apresentação sob medida: uma página só, com abertura animada, cardápio
da semana em cartões que viram, reserva da feijoada, carrossel de pratos,
delivery, como chegar e WhatsApp em todos os botões.

| Arquivo | O que é |
|---|---|
| `index.html` | O site inteiro. Logo e foto já vão embutidas, não precisa de mais nada |
| `og.jpg` | A imagem que aparece quando o link é mandado no WhatsApp |

## Publicar em 1 minuto

1. Abra [app.netlify.com/drop](https://app.netlify.com/drop) e arraste **a pasta
   `restaurante-celeste` inteira** (não só o `index.html`, senão a imagem do
   WhatsApp não vai junto)
2. No painel do site: **Site configuration → Change site name** →
   `restauranteceleste`. O endereço vira `restauranteceleste.netlify.app`
3. Mande o link para o seu próprio WhatsApp e confira a pré-visualização

Se o nome `restauranteceleste` já estiver em uso, escolha outro e troque
`restauranteceleste.netlify.app` pelo endereço novo em todo o `index.html`
(buscar e substituir: são 6 lugares). Sem isso, o link abre normalmente, mas a
imagem da pré-visualização não aparece.

## Antes de publicar: confirmar com o dono

Nada abaixo foi inventado. Onde a informação não estava confirmada, o site usa
um texto provisório. No `index.html`, os trechos provisórios têm um comentário
`CONFIRMAR` (é só buscar essa palavra), e a tabela diz onde mexer em cada caso.

| O que confirmar | O que o site mostra hoje | Onde mudar quando ele confirmar |
|---|---|---|
| Número do endereço: "lote 24" ou "casa 10"? | `QNH 10 — Taguatinga Norte` | Busque `QNH 10 — Taguatinga Norte` (menu, Como chegar e rodapé) e `QNH 10, Taguatinga Norte` (dados para o Google) |
| O WhatsApp é mesmo o fixo 3256-8503? | Todos os botões vão para `556132568503` | Se ele passar um celular, troque `556132568503` e `3256-8503` em todo o arquivo |
| Dias do baião de dois e do bobó de camarão | "Pratos especiais durante a semana — pergunte no WhatsApp" | Cartões de quinta e sábado e os dois pratos no carrossel (os comentários `CONFIRMAR` dizem o texto) |
| Prato do dia de segunda a quarta | "Prato do dia — consulte no WhatsApp" | Cartões de segunda, terça e quarta |
| Taxa e raio de entrega | "Taxa de entrega: consulte no WhatsApp", sem valor | Cartão Delivery e legenda do mapa |
| Nome do prato da foto | "Empanado com legumes" (descrição do que aparece na foto) | Primeiro prato do carrossel |

## Fotos que melhoram muito a demo

A foto usada é um print de 336×344 px. No celular fica boa, mas numa tela
grande perde nitidez. Peça ao dono:

- **A foto original** desse prato (a que ele postou no Instagram, direto do celular)
- **Uma foto da feijoada**: hoje a seção da feijoada usa ilustração, porque não
  existe foto dela e usar a de outro prato seria enganoso
- **Fotos dos pratos** do carrossel: hoje só o primeiro tem foto, os outros
  usam ilustração em traço

Não use foto de banco de imagem nem gerada por IA fingindo ser do restaurante.

### Trocar uma ilustração por foto

1. Converta a foto para WebP em [squoosh.app](https://squoosh.app) (largura de
   800 px basta) e salve dentro da pasta, por exemplo `feijoada.webp`
2. No `index.html`, ache o prato no carrossel e troque o bloco
   `<div class="cf-media cf-ill" …> … </div>` inteiro por:

   ```html
   <div class="cf-media" role="img" aria-label="Feijoada servida no Restaurante Celeste" style="background:url(feijoada.webp) center/cover"></div>
   ```

3. Publique de novo arrastando a pasta no Netlify Drop

## O que o site já faz sozinho

- O cartão de **hoje** vem destacado e virado, pela hora de Brasília. No domingo
  aparece "Hoje estamos fechados — volte amanhã a partir das 11h"
- O selo **aberto agora / fechado** acompanha o horário (seg a sáb, 11h–14h30)
- A **reserva da feijoada** monta a mensagem com o dia e o número de pessoas
- Toda mensagem de WhatsApp começa com "Olá! Vim pelo site…", para o dono saber
  de onde veio o cliente
- A abertura dura cerca de 2,8 s na primeira visita e 1,5 s nas seguintes
- Quem ativou **"reduzir movimento"** no celular vê o site sem abertura, sem
  vapor e sem carrossel automático
- Sem JavaScript, o conteúdo aparece todo, sem abertura
