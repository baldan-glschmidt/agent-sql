# E028ICP

## Descrição

Tabelas - Condição de Pagamento - Parcelas

---

## Resumo

- Campos: 19
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| SeqIcp | Number(002,0) | Não | Ordem sequencial para controle das parcelas |
| QtdPar | Number(003,0) | Não | Quantidade de parcelas |
| DiaPar | Number(003,0) | Sim | Quantidade de dias de intervalo entre as parcelas |
| DiaFix | String(001) | Não | Indicativo se o dia do vencimento é fixo para períodos de 30 em 30 dias |
| PerRat | Number(005,2) | Não | Percentual do total a ser considera para a condição de pagamento |
| QtdDsc | Number(003,0) | Sim | Quantidade de parcelas com desconto |
| PerDsc | Number(004,2) | Sim | Percentual de desconto para as parcelas com desconto |
| TolDsc | Number(003,0) | Sim | Quantidade de dias de tolerância para o desconto da parcela |
| GerBai | String(001) | Sim | Indicativo se, no momento da geração do título, o mesmo é baixado automaticamente. |
| TnsBai | String(005) | Sim | Código da Transação de Baixa Automática |
| IndIcs | String(001) | Não | Indicativo se recalcula o desconto nas parcelas desconsiderando ST |
| DscAnt | Number(004,2) | Sim | Percentual de desconto por antecipação para os títulos gerados |
| DscPon | Number(004,2) | Sim | Percentual de desconto por pontualidade para os títulos gerados |
| DatFix | Date | Sim | Dia/Mês Fixo para a geração das parcelas baseando-se na tabela de preço |
| FixDia | Number(003,0) | Sim | Dia fixo para a geração das parcelas baseando-se na tabela de preço |
| IndPag | String(001) | Sim | Indicativo da forma de pagamento |
| CodFpg | Number(002,0) | Sim | Código da Forma de Pagamento |

---

## Chave Primária

- CodEmp
- CodCpg
- SeqIcp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E028ICP_001

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCpg | CodCpg |

