# R206LOJ

## Descrição

PLR Paquetá - Lojas

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CmpAlt | Date | Não | Competência de Referência |
| EqpSeg | String(001) | Sim | Loja Utiliza Equipamento de Segurança (S,N) |
| GirAdq | Number(005,2) | Sim | Percentual de Giro Adequado |
| IteNfs | Number(005,2) | Sim | Itens p/ Nota Fiscal |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CmpAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R206LOJ_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R206LOJ_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

