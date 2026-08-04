# E099FIN

## Descrição

Cadastros - Usuários - Finanças

---

## Resumo

- Campos: 29
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| PagAlt | String(001) | Sim | Indicativo dos títulos que o usuário poderá alterar os valores de baixa |
| PagAba | String(001) | Sim | Indicativo se usuário pode alterar o valor de baixa do contas a pagar |
| PagAjr | String(001) | Sim | Indicativo se usuário pode alterar o valor de juros do contas a pagar |
| PagAml | String(001) | Sim | Indicativo se usuário pode alterar o valor de multa do contas a pagar |
| PagAen | String(001) | Sim | Indicativo se usuário pode alterar o valor de encargos do contas a pagar |
| PagAcr | String(001) | Sim | Indicativo se usuário pode alterar o valor de correção do contas a pagar |
| PagAac | String(001) | Sim | Indicativo se usuário pode alterar o valor outros acréscimos do contas a pagar |
| PagAsc | String(001) | Sim | Indicativo se usuário pode alterar o valor de descontos do contas a pagar |
| PagAde | String(001) | Sim | Indicativo se usuário pode alterar o valor outros descontos do contas a pagar |
| PagAlq | String(001) | Sim | Indicativo se usuário pode alterar o valor líquido do contas a pagar |
| PagMoe | String(001) | Sim | Indicativo se considera os valores de multimoeda do Contas a Pagar |
| RecAba | String(001) | Sim | Indicativo se usuário pode alterar o valor de baixa do contas a receber |
| RecAjr | String(001) | Sim | Indicativo se usuário pode alterar o valor de juros do contas a receber |
| RecAml | String(001) | Sim | Indicativo se usuário pode alterar o valor de multa do contas a receber |
| RecAen | String(001) | Sim | Indicativo se usuário pode alterar o valor de encargos do contas receber |
| RecAcr | String(001) | Sim | Indicativo se usuário pode alterar o valor de correção do contas a receber |
| RecAac | String(001) | Sim | Indicativo se usuário pode alterar o valor outros acréscimos do contas a receber |
| RecAsc | String(001) | Sim | Indicativo se usuário pode alterar o valor de descontos do contas a receber |
| RecAde | String(001) | Sim | Indicativo se usuário pode alterar o valor outros descontos do contas a receber |
| RecAlq | String(001) | Sim | Indicativo se usuário pode alterar o valor líquido do contas a receber |
| RecMoe | String(001) | Sim | Indicativo se considera os valores de multimoeda do Contas a Receber |
| PerGds | String(001) | Sim | Permite gerar devolução de saldo na baixa do Contas a Receber |
| CxbBlo | String(001) | Sim | Indicativo se usuário pode resgatar contrato de aplicação com data de bloqueio |
| MaiPar | String(001) | Sim | Indicativo se usuário poderá renegociar títulos com quantidade maior de parcelas |
| EntRen | String(001) | Sim | Indicativo se usuário poderá não dar entrada na renegociação |
| BaiPer | String(001) | Sim | Indicativo que permite o usuário baixar título considerado como perda |
| MovLoj | String(001) | Sim | Indicativo que permite o usuário movimentar conta interna da loja |

---

## Chave Primária

- CodEmp
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
