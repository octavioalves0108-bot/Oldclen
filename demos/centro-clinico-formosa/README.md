# Demo — Centro Clínico de Formosa (Formosa-GO)

Página de abertura cinematográfica e vitrine para
[@centroclinicodeformosa](https://www.instagram.com/centroclinicodeformosa/).
Arquivo único: `index.html`, com o logo embutido. Abre com dois cliques e
publica arrastando em [app.netlify.com/drop](https://app.netlify.com/drop).

## O que a página faz

- **Abertura.** O símbolo do logo (quatro traços em volta do centro) se forma
  em partículas creme: os traços crescem do centro para fora e o anel caramelo
  fecha por último, enquanto o contador vai a 100%
- **Capa.** "Centro" e "Clínico" entram com as letras girando em 3D. O símbolo
  gira devagar no próprio plano, inclina em 3D como uma medalha e acompanha o
  mouse, ao lado de um eletrocardiograma
- **Faixas.** Aceleram e invertem o sentido conforme a rolagem
- **Carrossel 3D dos atendimentos.** Os cartões laterais giram em direção a
  quem olha. Dá para arrastar, usar as setas, as abas ou o teclado
- **Jornada.** O símbolo se forma de novo e gira enquanto a pessoa lê as quatro
  etapas, com um anel de progresso
- **Cuidado.** Um cartão claro se abre com a rolagem e a frase acende palavra
  por palavra
- **Visite.** Cidade, Instagram e um selo giratório com o logo

Quem ativou "reduzir movimento" no celular vê a página sem animação pesada.

## De onde saiu o conteúdo

O Instagram não deixa ler o perfil sem login, e a busca trouxe muito pouco:

| Dado | Fonte |
|---|---|
| Nome "Centro Clínico de Formosa" | Post do perfil no Instagram |
| Categoria "Clínica médica", Formosa-GO | Perfil no Instagram |
| Cores e símbolo | O logo enviado |

Nenhuma especialidade, endereço ou telefone apareceu. A página não tem preço,
depoimento nem número de história.

## Confirmar com a clínica antes de mostrar

1. **Os atendimentos do carrossel são todos sugestão.** Clínica geral,
   especialidades, exames e check-up preventivo são o básico de uma clínica
   médica, colocados no espírito do [`gerador`](../../gerador/COMO-USAR.md).
   Troque pelas especialidades que a clínica realmente tem (cardiologia,
   ginecologia…): cada cartão é um bloco `<article class="card">` no HTML, e os
   nomes das abas ficam logo abaixo
2. **Os textos** da capa, da jornada e do manifesto são de apresentação, não
   fatos sobre a clínica
3. **Endereço e WhatsApp.** Preencha `endereco` e `whatsapp` no bloco `CONFIG`
   no fim do arquivo. O endereço aparece em "Onde", com link para o mapa, e os
   botões "Agendar" passam a abrir o WhatsApp com a mensagem pronta
4. **Logo.** O arquivo enviado tem 148 px e aparece pequeno (navegação, selo e
   verso dos cartões). Com a versão em alta resolução ou SVG, dá para usar maior
5. **Fotos.** Em `CONFIG.fotos` você cola a URL de uma foto por atendimento
