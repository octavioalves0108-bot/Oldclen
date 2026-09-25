# Demo — Clínica Integrada UltraFisio

Página de abertura cinematográfica e vitrine para
[@ultrafisioo](https://www.instagram.com/ultrafisioo/).
Arquivo único: `index.html`. Abre com dois cliques e publica arrastando em
[app.netlify.com/drop](https://app.netlify.com/drop).

## O que a página faz

- **Abertura.** Uma coluna vertebral de partículas se monta de baixo para
  cima, vértebra por vértebra, enquanto o contador vai a 100%. Um impulso de
  energia verde sobe pela coluna sem parar
- **Capa.** "ULTRA" em letra pesada e "Fisio" em itálico entram girando em
  3D. A coluna gira, acompanha o mouse e mostra o ângulo em tempo real, ao
  lado de um traçado que pulsa
- **Faixas.** Aceleram e invertem o sentido conforme a rolagem
- **Carrossel 3D dos tratamentos.** Os cartões laterais giram em direção a
  quem olha. Dá para arrastar, usar as setas, as abas ou o teclado
- **Método.** A coluna se forma de novo e dá uma volta completa enquanto a
  pessoa lê as quatro etapas, com um anel de progresso
- **Movimento.** Um cartão claro se abre com a rolagem e a frase acende
  palavra por palavra
- **Agende.** Instagram e um selo giratório de "Agende"

Quem ativou "reduzir movimento" no celular vê a página sem animação pesada.

## De onde saiu o conteúdo

O Instagram não deixa ler o perfil sem login, e a busca trouxe quase nada:

| Dado | Fonte |
|---|---|
| Nome "Clínica Integrada UltraFisio" | Título do perfil no Instagram |
| É fisioterapia | O próprio nome e um reel do perfil |

**A cidade não apareceu em lugar nenhum.** Há outras "UltraFisio" em
Botucatu, São Paulo e Brazlândia, mas com outros perfis, então nenhum dado
delas foi usado. A página não cita cidade, endereço, telefone, preço,
depoimento nem número algum.

## Confirmar com a clínica antes de mostrar

1. **Os tratamentos do carrossel são todos sugestão.** Fisioterapia ortopédica,
   coluna e postura, fisioterapia esportiva, pilates e reabilitação funcional
   são serviços comuns em clínica de fisioterapia, colocados no espírito do
   [`gerador`](../../gerador/COMO-USAR.md). Troque pelos que a clínica
   realmente oferece: cada cartão é um bloco `<article class="card">` no HTML,
   e os nomes das abas ficam logo abaixo. "Integrada" costuma significar mais
   de uma área (nutrição, psicologia, pilates…), o que vale perguntar
2. **Os textos** da capa, do método e do manifesto são de apresentação, não
   fatos sobre a clínica
3. **Cidade, endereço e WhatsApp.** Preencha `cidade`, `endereco` e `whatsapp`
   no bloco `CONFIG` no fim do arquivo. A cidade aparece no alto da capa, o
   endereço ganha um bloco com link para o mapa e os botões "Agendar" passam a
   abrir o WhatsApp com a mensagem pronta
4. **Fotos.** Em `CONFIG.fotos` você cola a URL de uma foto por tratamento
5. **Logo.** A marca da navegação (vértebras empilhadas) foi criada para a
   demo. Com o logo real, dá para trocar
