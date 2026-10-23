# R005FEC

## Descrição

Feriados para Serviços

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFer | Number(004,0) | Não | Código da Tabela de Feriados |
| DatFer | Date | Não | Data do Feriado |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Tabela Organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| UtiSrv | Number(001,0) | Sim | Dia da Semana para Feriado |

---

## Chave Primária

- CodFer
- DatFer
- NumEmp
- TabOrg
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005FEC_000

**Tabela:** R002FEM

| Origem | Destino |
|--------|---------|
| CodFer | CodFer |

### IR_R005FEC_002

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R005FEC_003

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R005FEC_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

