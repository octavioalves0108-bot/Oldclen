# Demo — Gente Linda Centro Clínico (Formosa-GO)

Página de abertura cinematográfica e vitrine para
[@institutogentelindafsa](https://www.instagram.com/institutogentelindafsa/).
Arquivo único: `index.html`, com o logo embutido. Abre com dois cliques e
publica arrastando em [app.netlify.com/drop](https://app.netlify.com/drop).

## O que a página faz

- **Abertura.** O logo vira um coração 3D de partículas, com uma pessoa azul e
  outra vermelha. As duas metades chegam pelos lados e se abraçam no centro
  enquanto o contador vai a 100%. Na entrada, um halo azul e vermelho se abre
- **Capa.** "Gente" e "Linda" entram com as letras girando em 3D. O coração
  bate em ritmo cardíaco (duas batidas curtas), balança, acompanha o mouse e
  tem um eletrocardiograma correndo ao lado
- **Faixas.** Aceleram e invertem o sentido conforme a rolagem
- **Carrossel 3D das quatro especialidades.** Os cartões laterais giram em
  direção a quem olha. Dá para arrastar, usar as setas, as abas ou o teclado
- **Para quem.** O coração se forma de novo e gira enquanto a pessoa lê sobre
  crianças, adolescentes e adultos, com um anel de progresso
- **Acolher.** Um cartão claro se abre com a rolagem e a frase acende palavra
  por palavra
- **Visite.** Endereço com mapa, Instagram e um selo giratório com o logo

Quem ativou "reduzir movimento" no celular vê a página sem animação pesada.

## De onde saiu o conteúdo

O Instagram não deixa ler o perfil sem login. Os dados vieram dos trechos que a
busca mostra:

| Dado | Fonte |
|---|---|
| "Instituto de acolhimento psicológico & psicopedagógico" | Bio do Instagram |
| Psicologia, psicopedagogia, fonoaudiologia e psiquiatria para crianças, adolescentes e adultos | Instagram e Facebook |
| "Há mais de 16 anos cuidando da sua…" | Título de um post do Instagram |
| Rua Severiano Batista de Oliveira, 381 — Qd. 108, Sala 04 — Centro | Solutudo e brasil-empresas (duas fontes batem) |
| Cores e símbolo | O logo enviado |

A página não tem preço nem depoimento.

## Confirmar com a clínica antes de mostrar

1. **"+16 anos".** Vem do próprio post, mas o CNPJ é de 2013 (cerca de 13
   anos). A clínica pode ser anterior ao CNPJ; confirme o número
2. **Os textos de cada fase da vida** (crianças, adolescentes, adultos) e quais
   especialidades aparecem em cada uma são textos de apresentação, não fatos.
   Vale mostrar para a dona
3. **Telefone e WhatsApp.** Os diretórios trazem (61) 3631-1989 e
   (61) 9613-0916. O segundo tem 8 dígitos, formato de celular fora de uso,
   então nenhum entrou na página. Preencha `telefone` e `whatsapp` no bloco
   `CONFIG` no fim do arquivo. Com o WhatsApp preenchido, os botões "Agendar"
   abrem a conversa com a mensagem pronta
4. **Logo.** O arquivo enviado tem 146 px, pequeno demais para ampliar. Ele
   aparece só no selo da seção "Visite"; na navegação e no coração 3D a marca
   foi redesenhada em vetor. Com o logo em alta resolução (ou SVG), dá para
   usá-lo nos dois lugares
5. **Fotos.** Em `CONFIG.fotos` você cola a URL de uma foto por especialidade
