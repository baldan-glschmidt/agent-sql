# E032TFI

## Descrição

Cadastros - Financeiras - Tabelas de Financiamento

---

## Resumo

- Campos: 21
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFin | Number(004,0) | Não | Código da financeira |
| NumTab | Number(008,0) | Não | Número da tabela de financiamento |
| ValIni | Date | Sim | Validade inicial da tabela de juros da financeira |
| ValFin | Date | Sim | Validade final da tabela de juros da financeira |
| DesTfi | String(100) | Não | Descrição da tabela financeira |
| VarPar | Number(007,4) | Sim | Percentual de variação das parcelas do financiamento |
| TabExp | Number(008,0) | Sim | Número da Tabela de Financiamento para Exportação |
| NumPro | String(255) | Sim | Número da tabela de produto para exportação |
| CodExp | String(255) | Sim | Código para Exportação (TOP) |
| VlrIof | Number(009,6) | Sim | Valor do coeficiente de IOF ao mês do financiamento |
| IofAdc | Number(009,6) | Sim | Percentual do IOF acicional do financiamento |
| TaxCre | Number(005,2) | Sim | Taxa para Abertura de Crédito |
| TabEnt | String(001) | Sim | Tabela de Financiamento Obriga Entrada |
| IndPad | String(001) | Não | Indicativo se esta tabela de preços é padrão para sugestão na venda |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFin
- NumTab

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
