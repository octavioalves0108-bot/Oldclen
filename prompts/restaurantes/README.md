# Restaurantes sem site — Taguatinga Norte

Levantamento de 28/09/2026: três restaurantes com Instagram e telefone, sem
site próprio encontrado, cada um com um prompt completo para gerar o site.

| # | Restaurante | Cozinha | Instagram | Contato | Prompt |
|---|---|---|---|---|---|
| 1 | **Restaurante Celeste** | Comida caseira | [@restauranteceleste](https://www.instagram.com/restauranteceleste/) | WhatsApp (61) 3256-8503 | [`01-restaurante-celeste.md`](01-restaurante-celeste.md) |
| 2 | **Jeri Carne de Sol** | Nordestina | [@jericoacoararestaurante](https://www.instagram.com/jericoacoararestaurante/) | (61) 3354-3056 | [`02-jeri-carne-de-sol.md`](02-jeri-carne-de-sol.md) |
| 3 | **Paladar Goiano** | Goiana, churrasco na mesa | [@restaurantepaladargoiano](https://www.instagram.com/restaurantepaladargoiano/) | (61) 99325-9445 | [`03-paladar-goiano.md`](03-paladar-goiano.md) |

Os três também entraram no [`../../crm/pipeline.csv`](../../crm/pipeline.csv)
com status `ALVO`.

## Como foi feito — e o que ainda falta você conferir

O levantamento foi feito só por busca na web. Google Maps, Instagram, iFood e
os guias comerciais estavam bloqueados no ambiente. Por isso:

| Critério | Como ficou |
|---|---|
| **Sem site** | Nenhum site próprio apareceu nas buscas pelo nome de cada um. Os 7 descartados abaixo foram cortados justamente por terem site. **Confirme na ficha do Google Maps** — é o único lugar onde a ausência de site é certa ([`../../docs/07-varredura.md`](../../docs/07-varredura.md), passo 2) |
| **Instagram ativo** | Os perfis existem e têm conteúdo (Celeste com post recente no Threads do mesmo @; Paladar Goiano com ~28 mil seguidores e 322 posts; Jeri com ~2,2 mil seguidores e 56 posts). **A data do último post não pôde ser vista.** Confira se postaram nos últimos 15 dias e se há Linktree ou `wa.me` na bio (alvo de ouro) |
| **Telefone** | Veio de fichas públicas, que envelhecem. **Não mande mensagem antes de conferir o número no Maps** ([`../../docs/07-varredura.md`](../../docs/07-varredura.md), "Duas limitações") |
| **Nota e avaliações** | Não deu para ver a nota do Google. Nos agregadores: Jeri 4,5 (640 avaliações); Paladar Goiano **3,5** (1.179). A régua do repositório descarta abaixo de 4,0 no Google — **confira a do Paladar antes de montar a demo** |

**Restaurante não está nas faixas A nem B** de
[`../../docs/02-prospeccao-taguatinga.md`](../../docs/02-prospeccao-taguatinga.md),
e lanchonete está na C. Dos três, o Paladar Goiano (rodízio, grupo, família)
é o de ticket mais alto; o Celeste e o Jeri vivem de almoço do dia a dia.
Espere negociação no preço.

## Antes de gerar cada site

1. Abra a ficha no Google Maps e confirme: sem botão "Site", telefone, nota
   e número de avaliações. Copie 3 avaliações reais — viram os depoimentos
2. Abra o Instagram: data do último post, o que tem na bio, e **baixe a logo
   e as fotos** pedidas na seção 5 de cada prompt
3. Resolva os itens da seção 3 do prompt (dados a confirmar)
4. Cole o prompt numa IA de código com as fotos anexadas. Se tiver as
   avaliações, acrescente ao fim: "Depoimentos reais do Google: …"

Os prompts pedem o mesmo padrão das demos em [`../../demos/`](../../demos/):
arquivo único para o Netlify Drop, abertura animada, 3D, e as regras de
fluidez que deixaram a demo da CVC a ~60 quadros por segundo no celular.

## Descartados nesta busca (não precisa checar de novo)

| Restaurante | Motivo |
|---|---|
| Chamas Grill | Tem site: chamasgrilldf.com.br |
| Adega da Cachaça | Tem site: adegadacachacabar.com.br |
| Feijãozinho | Tem site: feijaozinhorestaurante.com.br |
| Mangút | Tem site: mangutrestaurante.com.br |
| Fogo do Galpão | Tem site: fogodogalpao.com.br |
| Mangabas Gastrobar | Tem site: mangabasgastrobar.com.br |
| Zezinho Carne de Sol | Domínio zezinhocarnedesol.com listado no Foursquare |
| Fogão Goiano (Comercial Norte) | Consta como fechado permanentemente |

**Reservas para a próxima leva**, ainda não verificadas: Recanto Nordestino
(EQNL 6/8, Taguatinga Norte), Mandaka (QSD 23, Taguatinga Sul) e Sabor da Casa
(QSE 06, Taguatinga Sul).

## Fontes

- Restaurante Celeste: [post no Threads do @restauranteceleste](https://www.threads.com/@restauranteceleste/post/DYfQh9dlAcA)
  (endereço QNH 10 e WhatsApp 3256-8503) e resultados de busca com horário,
  feijoada e área de entrega
- Jeri Carne de Sol: [Instagram](https://www.instagram.com/jericoacoararestaurante/),
  [iFood](https://www.ifood.com.br/delivery/brasilia-df/jeri-carne-de-sol-comida-brasileira-taguatinga-norte-taguatinga/4751c874-7326-4f6b-b560-86506ed8773b),
  [Restaurant Guru](https://restaurantguru.com/Jericoacoara-Carne-de-Sol-Brasilia)
- Paladar Goiano: [Instagram](https://www.instagram.com/restaurantepaladargoiano/),
  [Facebook](https://www.facebook.com/paladargoianorestaurante/),
  [Bendito Guia](https://www.benditoguia.com.br/empresa/restaurante-paladar-goiano-taguatinga-norte-taguatinga-brasilia-df),
  [Restaurant Guru](https://restaurantguru.com/RestauranteCafe-Paladar-Goiano-Brasilia)
