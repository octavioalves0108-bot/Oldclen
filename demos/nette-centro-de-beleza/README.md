# Demo — Nette Centro de Beleza (Formosa-GO)

Página de abertura cinematográfica e vitrine para
[@nette.centrodebeleza](https://www.instagram.com/nette.centrodebeleza/).
Arquivo único: `index.html`. Abre com dois cliques e publica arrastando em
[app.netlify.com/drop](https://app.netlify.com/drop).

## O que a página faz

- **Abertura de marca.** Um anel de noivado feito de pó dourado em 3D se forma
  enquanto o contador vai a 100%. Na entrada, o anel desliza para a capa e vira
  o símbolo da marca, com um "N" no centro
- **Capa.** As letras de "Nette" giram em 3D e os números contam até o valor.
  O anel acompanha o mouse
- **Faixas.** Aceleram e invertem o sentido conforme a rolagem
- **Carrossel 3D das seis especialidades.** Dá para arrastar, usar as setas,
  as abas ou o teclado. Troca sozinho e pausa quando a pessoa interage
- **História.** A metragem sobe de 12 para 300 m² conforme a pessoa rola a
  linha do tempo
- **Assinatura.** A frase acende palavra por palavra durante a leitura
- **Visite.** Endereço, mapa, Instagram e um selo giratório de "Agende"

Quem ativou "reduzir movimento" no celular vê a página sem animação pesada.
A página também abre sem internet: as fontes trocam para Georgia.

## De onde saiu o conteúdo

O Instagram não deixa ler o perfil sem login, e os sites abaixo estavam
bloqueados no ambiente onde a página foi feita. Por isso os dados vieram dos
trechos que a busca mostra de cada um.

| Dado | Fonte |
|---|---|
| Especialidades: noivas, cabelo, maquiagem, sobrancelhas, unhas e depilação | Bio do Instagram e página do Facebook |
| Rua Olímpio Jacinto, 296 — Setor Central, Formosa-GO | applocal.com.br |
| "Serviços de beleza confiáveis e encantadores para Formosa-GO e região do DF" e "produtos diferenciados, técnicas qualificadas e equipamentos modernos" | Descrição no Facebook e no applocal |
| Linha do tempo: curso em 1996, salão de 12 m² em 1997, obras em 2008, reinauguração em 2010; 300 m² com suíte de noivas, sala de estética e sala de depilação | Matéria "Nette Centro de Beleza — 20 anos promovendo encantamento e confiança" (Revista Tops) |

**A página não tem preço nem depoimento**, pela regra de
[`gerador/COMO-USAR.md`](../../gerador/COMO-USAR.md).

## Confirmar com a dona antes de mostrar

1. **Ano de início.** O Facebook diz "desde 1995" e a matéria diz curso em 1996
   e salão em 1997. A página segue a matéria e diz "+30 anos de ofício", que é
   verdade nos dois casos
2. **300 m² e as salas.** Vêm de uma matéria de por volta de 2016. Confirme se
   a estrutura continua a mesma
3. **WhatsApp.** Os diretórios trazem (61) 3631-3137 e (61) 9648-2273. O
   segundo tem 8 dígitos, formato de celular fora de uso, então nenhum dos dois
   entrou na página (veja [`docs/07-varredura.md`](../../docs/07-varredura.md)).
   Com o número certo, preencha `whatsapp` no bloco `CONFIG` no fim do arquivo.
   A partir daí, todos os botões "Agendar" abrem o WhatsApp com a mensagem
   pronta. Enquanto o campo estiver vazio, eles levam ao Instagram
4. **Fotos.** A página ainda não tem fotos, porque o Instagram bloqueou o
   download. Em `CONFIG.fotos` você cola a URL de uma foto para cada serviço, e
   o cartão troca a arte animada pela foto
