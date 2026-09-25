# Almox Central

Sistema de controle de almoxarifado em um único arquivo (`index.html`).

- **Estoque**: saldo de cada material, estoque mínimo, localização (corredor-prateleira-nível) e itens retornáveis.
- **Movimentações**: entrada, saída, devolução e ajuste de inventário, com quem pegou ou devolveu, data e horário. Vários itens por lançamento.
- **Modems Wi-Fi**: cadastro por MAC (um a um ou colando uma lista), modelo, número de série, status e com quem está.
- **Auditoria**: conferência por leitor de código de barras, ciclos de auditoria, divergências e histórico dos ciclos.
- **Exportação** para planilha (CSV) e busca rápida com `Ctrl K`.

## Três jeitos de usar

| Onde | Quem vê os mesmos dados | Como |
|---|---|---|
| **Conta Google** (recomendado para a equipe) | Qualquer pessoa com o link, sem login | Siga [`INSTALAR-GOOGLE.md`](INSTALAR-GOOGLE.md). Os dados ficam numa Planilha Google sua. |
| **Link do Claude** | Pessoas convidadas que tenham conta Claude | Página publicada no Claude, com banco próprio. |
| **Arquivo aberto no navegador** | Só aquele navegador | Abra `index.html` com dois cliques. |

O mesmo `index.html` funciona nos três. Ele detecta onde está rodando e escolhe onde salvar.

- `index.html`: o sistema
- `apps-script/Codigo.gs`: o servidor para a versão Google
