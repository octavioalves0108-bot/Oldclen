# Demo — Pousada do Sol (Alto Paraíso de Goiás)

Página de marca com abertura cinematográfica para
[@pousadadosol.altoparaiso](https://www.instagram.com/pousadadosol.altoparaiso/).
É uma demo pronta: o `index.html` é um arquivo só, com logo e fotos embutidos
(~500 KB). Para publicar, arraste ele em
[app.netlify.com/drop](https://app.netlify.com/drop).

## O que tem na página

| Bloco | O que faz |
|---|---|
| Abertura (loader) | Logo num medalhão com raios de sol se desenhando e órbitas 3D girando. As letras sobem uma a uma, o contador vai de 000 a 100 e a tela se abre no horizonte. Nas visitas seguintes na mesma sessão, a abertura é mais curta |
| Topo | Título com as letras entrando uma a uma e fotos empilhadas em 3D que seguem o mouse, com poeira dourada flutuando. No celular, o 3D gira sozinho |
| Faixas | Duas faixas de texto correndo em sentidos opostos que entortam com a velocidade da rolagem |
| Experiências | Carrossel 3D (coverflow) com 7 itens. Aceita arrastar, clicar, setas do teclado e troca sozinho a cada 5,5 s. Cada item tem um botão de WhatsApp com mensagem pronta citando aquele item |
| A pousada | Texto que acende palavra por palavra conforme a rolagem, mais contadores animados |
| Chapada | Mosaico de fotos com revelação e parallax |
| Comodidades | 12 cartões com inclinação 3D ao passar o mouse |
| Como chegar | Mapa ilustrado com rota animada, endereço e botão do Google Maps |
| Final | Sol que nasce conforme a rolagem e chamada para reservar |

Respeita "reduzir movimento" do sistema: sem abertura longa, sem autoplay e sem
partículas.

## De onde vieram os dados

O Instagram não abre sem login, então os dados vieram das fichas públicas da
pousada (Booking, Tripadvisor, Kayak/Travelocity) e das fotos que o dono
publicou:

- WhatsApp **(61) 99676-1539**, com "reservas somente pelo WhatsApp"
- Rua Gumercindo Barbosa, Alto Paraíso de Goiás – GO, 73770-000
- 15 quartos com banheiro privativo, Wi-Fi e frigobar; pátio com vista para o
  jardim e alguns com varanda
- Piscina ao ar livre, jardins, terraço, churrasqueira, área de piquenique,
  lavanderia, lareira na sala compartilhada, estacionamento grátis
- Café da manhã em buffet (frutas, sucos naturais, pães e bolos caseiros), com
  araras soltas visitando
- Ajuda para montar roteiro e apoio com passeios e ingressos
- 1 km do centro, cerca de 2 km da rodoviária, cerca de 37 km do Vale da Lua e do
  Parque Nacional

## Confira antes de mostrar ao dono

- **WhatsApp**: mande uma mensagem de teste pelo botão
- **Endereço**: as fichas divergem ("Q.4B, L.0 s/n, Beco 1, Setor Central" em
  uma e "nº 911" em outra). A página usa só o nome da rua
- **Brasília ≈ 230 km** no mapa é a distância de estrada conhecida, não veio da
  ficha
- **Lareira e frigobar**: aparecem nas fichas, mas vale confirmar que continuam

**Ficaram de fora de propósito:** preços, depoimentos e nota de avaliação.
Seguindo a regra do `gerador/COMO-USAR.md`, nada disso entra sem os números e
textos reais do Google da pousada. Se ele tiver uma nota boa no Google, ela
merece entrar no topo.

## Como editar

Os textos ficam em `fonte/template.html`, com as imagens no lugar de
`{{nome}}`. Depois de editar:

```
python3 fonte/build.py
```

Isso regenera o `index.html` embutindo as fotos de `fonte/img/`. Cada imagem
entra uma vez só no arquivo final. Para trocar uma foto, salve um `.webp` com o
mesmo nome em `fonte/img/` e rode o comando de novo. O script precisa só de
Python 3, sem bibliotecas extras.
