# Como usar o pipeline

Abra `pipeline.csv` no Google Sheets (Arquivo → Importar) ou no Excel.
Apague as três linhas de EXEMPLO quando entender o formato.

**Atualize todo dia à noite, 20 minutos.** Um lead esquecido é dinheiro
jogado fora, e esquecer é o padrão quando a semana aperta.

## Status possíveis

| Status | Significado | Próximo passo |
|---|---|---|
| `ALVO` | Qualificado, demo ainda não feita | Gerar a demo |
| `DEMO_PRONTA` | Página publicada, ainda não abordado | Ir na rua |
| `ABORDADO` | Falou, sem decisão | Follow-up D+2 |
| `TESTE_7_DIAS` | Aceitou o teste | Cobrar no dia 7 |
| `PROPOSTA_ENVIADA` | Viu o preço, está pensando | D+2 e D+5 encerramento |
| `FECHADO` | Pagou | Entregar, gravar vídeo, pedir 2 indicações, lançar em `clientes-ativos.csv` |
| `PERDIDO` | Não | Apagar a demo; voltar em 60 dias |
| `NAO_CONTATAR` | Pediu para parar | Nunca mais mandar nada (LGPD) |

## Colunas que importam mais do que parecem

- **`Placar_Qualificacao`** — de 0 a 5, conforme a régua em
  [`../docs/02-prospeccao-taguatinga.md`](../docs/02-prospeccao-taguatinga.md).
  **Só gere demo para 4 ou 5.** Essa disciplina é o que protege suas horas
- **`Usa_Linktree`** — `SIM` é alvo de ouro. Ele já sabe que precisa de um
  destino, só tem uma gambiarra. Aborde esses primeiro
- **`Indicado_Por`** — preencha no mesmo dia. Fale com todo indicado em até 48h
- **`Indicacoes_Coletadas`** — dois nomes por cliente fechado, sem exceção.
  Esta coluna é a que te leva a 30

## Três filtros para rodar toda noite

1. `Data_Proximo_Contato` = amanhã → sua lista de follow-up do dia seguinte
2. `Status` = `TESTE_7_DIAS` e já passaram 7 dias → ligue hoje
3. `Status` = `FECHADO` e `Indicacoes_Coletadas` vazio → você esqueceu de pedir.
   Volte lá

---

# Carteira de clientes: `clientes-ativos.csv`

O pipeline acompanha a venda. **Esta planilha acompanha o dinheiro que volta
todo mês.** Importe no Google Planilhas também. Uma linha por cliente fechado.

| Coluna | O que anotar |
|---|---|
| `Plano` | `ASSINATURA`, `LIVRE` ou `AVISTA` ([`../docs/00-plano-mestre.md`](../docs/00-plano-mestre.md), seção 3) |
| `Dia_Vencimento` | O dia do mês que ele escolheu |
| `Fim_Permanencia` | Data da publicação + 6 meses (só no plano Assinatura) |
| `Pix_Agendado` | `SIM` se ele programou o Pix recorrente no app dele |
| `Contrato_Assinado` | `SIM` só com PDF assinado ou "li e aceito" guardado |
| `Status_Pagamento` | `EM_DIA`, `ATRASADO`, `PAUSADO` ou `ENCERRADO` |
| `Ultimo_Relatorio` | Data do último relatório mensal enviado |
| `Meses_Gratis_Devidos` | Um por indicado que fechou. Desconte na próxima mensalidade |

## Dois filtros para rodar todo dia 5

1. `Ultimo_Relatorio` com mais de 30 dias → mande o relatório hoje
2. `Status_Pagamento` diferente de `EM_DIA` → siga a régua de atraso
   ([`../docs/00-plano-mestre.md`](../docs/00-plano-mestre.md), seção 12)

Esta planilha também é o seu registro de recebimentos para o Carnê-Leão e
para o Imposto de Renda. Não apague linha de cliente que saiu: mude o status
para `ENCERRADO`.
