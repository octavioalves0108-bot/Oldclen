# Como usar o gerador

Abra `index.html` com dois cliques. Funciona sem internet, sem instalar nada,
e também no celular.

**Meta: 10 a 15 minutos por página.** É esse número que torna 15 demos
possíveis em dois dias.

---

## O fluxo (uma página do começo ao fim)

1. **Clique em "Carregar exemplo"** na primeira vez, só para ver como fica
   pronto. Depois "Limpar tudo" e comece a valer
2. **Escolha o ramo primeiro.** Ele já preenche cor, frase e uma lista de
   serviços com preços plausíveis — você só ajusta
3. **Preencha com os dados reais** do negócio (seção abaixo: onde achar)
4. **Confira no modo Celular.** É nele que a pessoa vai ver. Sempre confira
   no celular antes de desktop
5. **"Baixar página"** → sai um arquivo `index.html`
6. **Publique:** abra [app.netlify.com/drop](https://app.netlify.com/drop) e
   arraste o arquivo. Em 30 segundos você tem um link no ar
7. **Salve o link** na coluna `Link_Demo` do `crm/pipeline.csv`

---

## Onde achar os dados (15 min de garimpo por negócio)

| Campo | Onde pegar |
|---|---|
| Nome, endereço, horário, telefone | Ficha do Google Maps |
| Nota e nº de avaliações | Ficha do Google — use os números reais |
| Depoimentos | **Copie as avaliações reais do Google.** Nunca invente |
| Fotos | Instagram dele: abra a foto, botão direito → "Copiar endereço da imagem" |
| Serviços e preços | Instagram, stories fixados, ou a tabela na parede da loja |

### Duas regras que não se quebram

**Nunca invente depoimento.** Use as avaliações reais do Google dele. Se ele
perceber uma avaliação falsa com o nome do negócio dele, você perdeu a venda
e a reputação na rua — e Taguatinga é pequena para quem trabalha com comércio
local.

**Nunca invente preço.** Se não souber, escreva "Consulte" ou "Orçamento sem
compromisso". Preço errado na tela vira discussão em vez de venda.

---

## Detalhes que aumentam o impacto

- **Use 3 ou 6 serviços.** Com 4 ou 5 sobra um card solto na última fileira
- **A foto do topo é o que mais impressiona.** Escolha a melhor foto do
  Instagram dele — de preferência do espaço ou de um resultado, não o logo
- **Nota do Google no topo:** se ele tem 4.8 com 200 avaliações, isso na tela
  é orgulho. Ele vai querer mostrar para alguém, e é exatamente o que você quer
- **WhatsApp:** digite com DDD (`61 99999-0000`). O botão flutuante já abre a
  conversa com mensagem pronta
- **Mande o link pelo WhatsApp** para ver como aparece a pré-visualização.
  É assim que ele vai receber

---

## O que a página já vem fazendo

- Botão de WhatsApp flutuante, com mensagem pronta escrita
- Cinco pontos de contato ao longo da página, todos levando ao WhatsApp
- Dados estruturados (`LocalBusiness`) para o Google entender o negócio
- Título, descrição e imagem de compartilhamento configurados
- Arquivo de ~12 KB: abre instantâneo até em 3G ruim
- Feita para celular primeiro, que é onde 90% vai abrir

---

## Se ele pedir uma mudança na hora

**Faça na frente dele.** Abra o gerador, mude, baixe, publique de novo no
Netlify. Leva menos de dois minutos.

Essa demonstração é o argumento mais forte que você tem para os R$ 250/mês —
é literalmente o serviço acontecendo na frente dele. Veja a objeção 3 em
[`../docs/04-objecoes-e-fechamento.md`](../docs/04-objecoes-e-fechamento.md).

---

## Quando o cliente fechar

O Netlify grátis dá um endereço tipo `nome-do-negocio.netlify.app`, e ele
serve perfeitamente para a demo.

Quando fechar, registre o domínio próprio (`nomedonegocio.com.br`) no
Registro.br — custa cerca de R$ 40 por ano. É parte do que ele está pagando
nos R$ 800, e é o que faz a página parecer profissional de verdade.
