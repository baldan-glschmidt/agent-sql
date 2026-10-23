# R163CRE

## Descrição

BS - Auxílio Creche / Babá

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodDep | Number(002,0) | Não | Código do dependente |
| DatPag | Date | Não | Data Pagamento |
| TipCre | String(001) | Sim | Tipo Reembolso |
| ValMen | Number(011,2) | Sim | Valor Mensalidade |
| CodOem | Number(008,0) | Sim | Estabelecimento Escolar |
| TipPdo | String(001) | Sim | Período |
| ObsRee | String(200) | Sim | Observação |
| DatCre | Date | Sim | Data Crédito |
| ValRee | Number(011,2) | Sim | Valor Reembolso |
| CreOpc | String(001) | Sim | Aprovado - Uso no Portal Web |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- DatPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R163CRE_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

