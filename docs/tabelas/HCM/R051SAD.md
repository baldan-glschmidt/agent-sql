# R051SAD

## Descrição

Informe/DIRF - Desconto Plano de Saúde Dependente

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| CodOem | Number(008,0) | Não | Código da Seguradora |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| CodDep | Number(002,0) | Não | Código do Dependente |
| ValDes | Number(011,2) | Sim | Valor Desconto |
| ValCop | Number(011,2) | Sim | Valor Co-participação |
| InfDes | Number(011,2) | Sim | Valor no Informe Tipo Desconto |
| InfRee | Number(011,2) | Sim | Valor no Informe Tipo Reembolso |
| OriPla | String(001) | Sim | Origem Plano |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodOem
- CodCal
- CodDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R051SAD_004

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R051SAD_005

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

