# Almox Central

Sistema de controle de almoxarifado em um único arquivo (`index.html`).

- **Estoque**: saldo de cada material, estoque mínimo, localização (corredor-prateleira-nível) e itens retornáveis.
- **Movimentações**: entrada, saída, devolução e ajuste de inventário, com quem pegou ou devolveu, data e horário. Vários itens por lançamento.
- **Modems Wi-Fi**: cadastro por MAC (um a um ou colando uma lista), modelo, número de série, status e com quem está.
- **Auditoria**: conferência por leitor de código de barras, ciclos de auditoria, divergências e histórico dos ciclos.
- **Exportação** para planilha (CSV) e busca rápida com `Ctrl K`.

## Uso compartilhado

A versão publicada no Claude usa um banco de dados compartilhado: tudo o que alguém registra aparece na hora para a equipe, com o nome de quem registrou. Para dar acesso, use **Compartilhar** na página e convide cada pessoa por e-mail com permissão de edição.

## Uso local

Abrir `index.html` direto no navegador funciona em **modo local**: os dados ficam salvos só naquele navegador, sem compartilhamento.
