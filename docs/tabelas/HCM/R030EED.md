# R030EED

## Descrição

Filial - Entidade Educativa

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração |
| CodOem | Number(008,0) | Não | Código Outra Empresa |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030EED_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R030EED_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R030EED_002

**Tabela:** R030EES

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| DatAlt | DatAlt |

