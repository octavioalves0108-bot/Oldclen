# NEXO Finance: controle de gastos e poupança

Tudo fica em **um único arquivo**: `index.html`. Cada pessoa entra com **e-mail e senha**
e vê só os próprios dados, sincronizados na nuvem (Supabase, grátis) entre celular e computador.

## Configuração única (uns 5 minutos)
1. **Publique o app** para ter um link: arraste o `index.html` em https://app.netlify.com/drop.
2. **Crie o projeto na nuvem:** entre em https://supabase.com, crie uma conta grátis e clique em **New project**.
3. **Crie a tabela:** no projeto, abra **SQL Editor**, cole o SQL abaixo (ele também aparece no app, com botão de copiar) e clique em **Run**.
4. **Configure o link do app:** em **Authentication → URL Configuration**, coloque o link do passo 1 em **Site URL**.
   Assim os e-mails de confirmação e de "esqueci minha senha" abrem o app.
5. **Conecte o app:** em **Project Settings → API**, copie a **Project URL** e a chave **anon public**.
   Abra o app e cole as duas na tela "Conectar à nuvem". Para ninguém mais precisar dessa tela, você também
   pode colar as duas chaves no código, em `const CLOUD = { url: '', key: '' }`, e publicar de novo.

```sql
create table if not exists public.user_state (
  user_id uuid primary key references auth.users(id) on delete cascade,
  data jsonb not null,
  updated_at timestamptz not null default now()
);
alter table public.user_state enable row level security;
create policy "ler meus dados" on public.user_state for select using (auth.uid() = user_id);
create policy "criar meus dados" on public.user_state for insert with check (auth.uid() = user_id);
create policy "atualizar meus dados" on public.user_state for update using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "apagar meus dados" on public.user_state for delete using (auth.uid() = user_id);
```

A chave "anon" pode ficar no app porque é pública por natureza. Quem protege os dados são as regras
(RLS) do SQL: cada usuário só consegue ler e alterar a própria linha. As senhas ficam com o Supabase,
que guarda apenas uma versão criptografada; o app nunca armazena senha.

## Contas
- **Criar conta:** e-mail e senha com pelo menos 8 caracteres, usando letras e números. O Supabase envia um e-mail de confirmação
  (dá para desligar em Authentication → Providers → Email → "Confirm email").
- **Esqueci minha senha:** o link chega por e-mail e abre o app na tela "Criar nova senha".
- **Sair:** os dados continuam na nuvem, e a cópia do aparelho é apagada por segurança.
- **Sem internet:** tudo continua funcionando e é salvo no aparelho. O ícone de nuvem no topo mostra o status,
  e as alterações são enviadas quando a conexão voltar.
- **Dados antigos:** se você já usava o app antes do login, na primeira entrada ele oferece levar os dados antigos para a sua conta.

## O que tem
- **Início:** saldo do mês, quanto você pode gastar por dia sem furar as contas nem a poupança, meta do mês, próximas contas, orçamento e últimos lançamentos.
- **Lançamentos:** despesas e receitas com categoria e forma de pagamento. Tem filtros, busca e exportação em CSV. Atalho: tecla **N**.
- **Orçamento:** limite por categoria, com alerta ao chegar em 80% e ao estourar. Também sugere limites com base na média dos últimos 3 meses.
- **Contas fixas:** mostra o vencimento e, ao tocar em "Pagar", lança o gasto sozinho.
- **Metas de poupança:** guardar e retirar dinheiro, prazo e quanto guardar por mês para chegar lá.
- **Relatórios:** gastos por categoria, receitas × despesas, gasto por dia e um veredito do mês.

## Lembretes (com o app aberto, mesmo minimizado)
- **Dia do pagamento:** lembra de separar a poupança antes de gastar.
- **Poupança semanal:** avisa se você está guardando abaixo do ritmo da meta.
- **Anotar gastos:** lembrete diário, que só aparece se você não registrou nada no dia.
- **Contas:** avisa antes de vencer e quando alguma atrasar.

## Celular
1. Arraste o arquivo em https://app.netlify.com/drop para receber um link.
2. Abra o link no celular e toque em "Adicionar à tela inicial".
3. Abra pelo ícone e ative as notificações.

O backup em arquivo (**Configurações → Exportar backup**) continua disponível, mas é opcional.
