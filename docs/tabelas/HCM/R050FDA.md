# R050FDA

## Descrição

Formação DARF

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodRec | Number(004,0) | Não | Código do Recolhimento |
| CodBas | Number(002,0) | Não | Código da Base |
| PerBas | Number(009,6) | Sim | Percentual Base |

---

## Chave Primária

- NumEmp
- CodRec
- CodBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R050FDA_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R050FDA_001

**Tabela:** R050REC

| Origem | Destino |
|--------|---------|
| CodRec | CodRec |

### IR_R050FDA_002

**Tabela:** R026BIF

| Origem | Destino |
|--------|---------|
| CodBas | CodBas |

