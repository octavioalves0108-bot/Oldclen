# Demo — Clínica OdontoLógica (Formosa-GO)

Página de abertura cinematográfica e vitrine para
[@odontologicaformosa](https://www.instagram.com/odontologicaformosa/).
Arquivo único: `index.html`. Abre com dois cliques e publica arrastando em
[app.netlify.com/drop](https://app.netlify.com/drop).

## O que a página faz

- **Abertura.** Um molar feito de partículas de luz se forma em 3D dentro de
  um visor de escaneamento, com um feixe percorrendo o dente de cima a baixo.
  Ao chegar a 100%, a "luz do refletor" acende e o dente desliza para a capa
- **Capa.** "Odonto" e "Lógica" entram com as letras girando em 3D. O dente
  gira como numa vitrine e acompanha o mouse. O visor mostra o ângulo do giro
  em tempo real, e o feixe volta a passar de tempos em tempos
- **Faixas.** Aceleram e invertem o sentido conforme a rolagem
- **Carrossel 3D dos tratamentos.** Dá para arrastar, usar as setas, as abas ou
  o teclado. Troca sozinho e pausa quando a pessoa interage
- **Método.** O dente se forma de novo no visor e gira conforme a pessoa lê as
  cinco etapas. Um anel de progresso acompanha a leitura
- **Manifesto.** Um cartão claro se abre com a rolagem e a frase acende palavra
  por palavra
- **Agende.** Instagram, local e um selo giratório de "Agende"

Quem ativou "reduzir movimento" no celular vê a página sem animação pesada.
Sem internet, as fontes trocam para Georgia.

## De onde saiu o conteúdo

O Instagram não deixa ler o perfil sem login, e os diretórios da cidade estavam
bloqueados no ambiente onde a página foi feita. A busca trouxe muito pouco:

| Dado | Fonte |
|---|---|
| Nome "Clinica OdontoLógica", Formosa | Título do perfil no Instagram |
| Clínica odontológica e harmonização orofacial | Página "Odonto Lógica · Formosa GO" no Facebook ([facebook.com/odontologicafsa](https://www.facebook.com/odontologicafsa/)) |

**A página não tem endereço, telefone, preço, depoimento nem número de
história**, porque nenhum desses dados apareceu. Não há "+X anos" nem "X mil
pacientes".

## Confirmar com a clínica antes de mostrar

1. **Se o Facebook é o mesmo lugar.** O nome e a cidade batem com o Instagram,
   mas o endereço do perfil é outro (`odontologicafsa`). A harmonização
   orofacial vem só dessa página
2. **Os tratamentos do carrossel.** Só a harmonização orofacial está
   confirmada. Avaliação, prevenção, restaurações e clareamento são
   procedimentos comuns de clínica geral, colocados como sugestão, no mesmo
   espírito do [`gerador`](../../gerador/COMO-USAR.md). Troque pelos que a
   clínica realmente divulga: cada cartão é um bloco `<article class="card">`
   no HTML, e os títulos das abas ficam logo abaixo
3. **O texto do método** (escuta, diagnóstico, planejamento, tratamento,
   acompanhamento) e o manifesto são textos de apresentação, não fatos sobre a
   clínica. Mostre para a dona e ajuste o tom
4. **Endereço e WhatsApp.** Preencha `endereco` e `whatsapp` no bloco `CONFIG`
   no fim do arquivo. O endereço aparece em "Onde", com link para o mapa. Com o
   WhatsApp preenchido, todos os botões "Agendar" passam a abrir a conversa com
   a mensagem pronta. Enquanto o campo estiver vazio, eles levam ao Instagram
5. **Fotos.** Em `CONFIG.fotos` você cola a URL de uma foto para cada
   tratamento, e o cartão troca a arte animada pela foto
