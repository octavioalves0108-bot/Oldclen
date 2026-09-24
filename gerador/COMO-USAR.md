# Como usar o gerador

Abra `index.html` com dois cliques. Funciona sem internet, sem instalar nada,
e também no celular.

**Meta: 10 a 15 minutos por página.** É esse número que torna 15 demos
possíveis em dois dias.

---

## O fluxo (uma página do começo ao fim)

0. **Deixe o Modo em "Demonstração".** A página não entra no Google enquanto
   ele não fechar. Só troque para "Cliente" na entrega
1. **Clique em "Carregar exemplo"** na primeira vez, só para ver como fica
   pronto. Depois "Limpar tudo" e comece a valer
2. **Escolha o ramo primeiro.** Ele já preenche cor, frase e uma lista de
   serviços com preços plausíveis — você só ajusta
3. **Preencha com os dados reais** do negócio (seção abaixo: onde achar)
4. **Confira no modo Celular.** É nele que a pessoa vai ver. Sempre confira
   no celular antes de desktop
5. **"Baixar página"** → sai um arquivo `index.html`. Coloque dentro de uma
   pasta com o nome do negócio (`studio-bella/index.html`) e **guarde essa
   pasta**: o arquivo é também o seu backup (veja "Alterar uma página já
   publicada", abaixo)
6. **Publique no Cloudflare Pages:** no painel do Cloudflare, **Workers &
   Pages → Create → aba Pages → Upload assets (Direct Upload)**. Dê ao projeto
   o nome do negócio e arraste a pasta. O link fica `studio-bella.pages.dev`
   *(os nomes dos botões mudam de vez em quando; procure "Pages" e "Direct
   Upload")*
7. **Salve o link** na coluna `Link_Demo` do `crm/pipeline.csv`

> **Por que não o Netlify Drop:** contas novas do Netlify (desde 4/9/2025)
> têm cerca de 20 publicações grátis por mês, e ao estourar **todos os sites
> da conta pausam**, inclusive os de clientes pagantes. Detalhes em
> [`../docs/00-plano-mestre.md`](../docs/00-plano-mestre.md), seção 1.1.

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
Cloudflare Pages (no mesmo projeto: *Create deployment* e arraste a pasta).
Leva menos de dois minutos.

Essa demonstração é o argumento mais forte que você tem para os R$ 250/mês —
é literalmente o serviço acontecendo na frente dele. Veja a objeção 3 em
[`../docs/04-objecoes-e-fechamento.md`](../docs/04-objecoes-e-fechamento.md).

---

## Alterar uma página já publicada

Toda página baixada pelo gerador leva dentro dela os dados do formulário.
Para mudar um preço daqui a três meses:

1. Clique em **"Abrir página salva (.html)"** e escolha o `index.html` do
   cliente (do seu backup no Google Drive)
2. O formulário volta preenchido. Mude o que ele pediu
3. Baixe e publique de novo no mesmo projeto do Cloudflare
4. Substitua o arquivo do backup pelo novo

Páginas feitas antes desta versão não têm esses dados: preencha uma última
vez e, daí em diante, elas abrem normalmente.

---

## Quando o cliente fechar

O `nome-do-negocio.pages.dev` serve para a demo. Na entrega:

1. Troque o **Modo para "Cliente"**, confira os dados com ele e baixe de novo
2. O domínio (`nomedonegocio.com.br`) é registrado **no nome do cliente**, na
   conta dele no Registro.br. Ele paga os R$ 40 por ano direto para o
   Registro.br
3. Siga o checklist de entrega de
   [`../docs/00-plano-mestre.md`](../docs/00-plano-mestre.md), seção 11
   (domínio, HTTPS, estatísticas, Google e backup)
