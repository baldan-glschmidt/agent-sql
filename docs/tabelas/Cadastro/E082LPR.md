# E082LPR

## Descrição

Tabelas - Tabelas de Preços de Fornecedores - Log Validades

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
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
| SitReg | String(001) | Não | Situação do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Não | Data da última alteração do registro |
| HorAlt | Number(005,0) | Não | Hora da última alteração do registro |
| SeqAlt | Number(004,0) | Não | Sequência da alteração do registro |
| IndExc | String(001) | Sim | Indicativo de que o item foi excluído da tabela de preços |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- DatAlt
- HorAlt
- SeqAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E082LPR_001

**Tabela:** E082TAB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |

