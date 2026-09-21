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
| `ABORDADO` | Falou, sem decisão | Follow-up D+1 |
| `TESTE_7_DIAS` | Aceitou o teste | Cobrar no dia 7 |
| `PROPOSTA_ENVIADA` | Viu o preço, está pensando | D+3 print, D+5 encerramento |
| `FECHADO` | Pagou | Entregar, gravar vídeo, pedir 2 indicações |
| `PERDIDO` | Não | Voltar em 60 dias |

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
