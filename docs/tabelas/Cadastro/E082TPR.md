# E082TPR

## Descrição

Tabelas - Tabelas de Preços de Fornecedores - Validades

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data início de validade da tabela de preço |
| DatFim | Date | Não | Data final de validade da tabela de preço |
| UsaQtd | String(001) | Sim | Indicativo se a tabela utiliza critério de preço por quantidade de compra |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| DatRea | Date | Sim | Data do último reajuste processado sobre a tabela |
| PerRea | Number(005,2) | Sim | Percentual do último reajuste processado sobre a tabela |
| SitReg | String(001) | Não | Situação do registro |
| ObsTpr | String(100) | Sim | Validades - Observação |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E082TPR_001

**Tabela:** E082TAB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |

