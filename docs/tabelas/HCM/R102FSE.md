# R102FSE

## Descrição

Filiais SESMT

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do SESMT |
| CodSmt | Number(004,0) | Não | Código do SESMT |
| DatAlt | Date | Não | Data de Alteração |
| CodFil | Number(006,0) | Não | Filial do SESMT |

---

## Chave Primária

- NumEmp
- CodSmt
- DatAlt
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102FSE_001

**Tabela:** R102SMT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodSmt | CodSmt |

### IR_R102FSE_003

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

