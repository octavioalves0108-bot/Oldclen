# Como colocar o Almox Central no ar para toda a equipe

Nesta versão o sistema fica na **sua conta Google**. Os dados ficam guardados numa Planilha Google sua, e qualquer pessoa que abrir o link vê e registra tudo em tempo real. Ninguém precisa de login. É grátis.

Você precisa de dois arquivos:

- `almox-central.html`, o sistema (neste repositório é o `almox/index.html`)
- `Codigo.gs`, o servidor (`almox/apps-script/Codigo.gs`). O código dele também aparece no próprio sistema, em **Sistema → Ver código do servidor**.

## Passo a passo (uns 5 minutos)

1. Abra **sheets.new** no navegador. Isso cria uma planilha nova. Dê o nome **Almox Central**.
2. No menu da planilha, clique em **Extensões → Apps Script**.
3. Vai abrir um editor com um arquivo `Código.gs`. Apague tudo o que estiver nele e cole o conteúdo do `Codigo.gs`.
4. Clique no **+** ao lado de "Arquivos", escolha **HTML** e dê o nome **Index** (só isso, sem ".html"). Apague o que vier dentro e cole **todo** o conteúdo do `almox-central.html`. Para copiar, abra o arquivo no Bloco de Notas e use Ctrl+A e depois Ctrl+C.
5. Salve com **Ctrl+S**.
6. Clique em **Implantar → Nova implantação**. Na engrenagem ao lado de "Selecione o tipo", escolha **App da Web** e preencha:
   - Executar como: **Eu**
   - Quem pode acessar: **Qualquer pessoa**
7. Clique em **Implantar**. O Google pede autorização. Escolha sua conta. Se aparecer "O Google não verificou este app", clique em **Avançado → Acessar Almox Central (não seguro)** e depois em **Permitir**. O aviso aparece porque o app foi criado por você, não pelo Google.
8. Copie o **URL do app da Web**. Ele começa com `https://script.google.com/macros/s/...`. **Esse é o link do sistema.** Mande para a equipe pelo WhatsApp ou por e-mail.

Na primeira vez que alguém abre o link, o sistema pergunta o nome da pessoa. Esse nome aparece em cada movimentação e auditoria que ela registrar.

## Bom saber

- O Google mostra uma faixa no topo dizendo que o app foi criado por um usuário do Google Apps Script. É normal.
- Os dados ficam nas abas `materiais`, `movs`, `modems` e `config` da planilha. **Não edite essas abas à mão.** Para ver os dados em forma de tabela, use os botões **Exportar** no sistema. Eles baixam a planilha e também criam abas "Relatório ..." legíveis na sua Planilha Google.
- As mudanças aparecem para os outros em até 5 segundos.
- **Quer exigir um código de acesso?** No `Codigo.gs`, preencha `const SENHA_EQUIPE = 'seucodigo';`, salve e publique uma nova versão (veja abaixo). Cada aparelho pede o código uma vez.
- **Para atualizar o sistema depois**, cole o código novo e vá em **Implantar → Gerenciar implantações → lápis (editar) → Versão: Nova versão → Implantar**. O link continua o mesmo.
