# R034REF

## Descrição

Ticket Refeição do Empregado

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| TipRef | Number(004,0) | Não | Tipo ticket refeição |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034REF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R034REF_003

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

### IR_R034REF_004

**Tabela:** R044TVL

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| TipRef | CodVal |

