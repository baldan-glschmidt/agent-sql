# R041APO

## Descrição

Aposentadoria - Colaborador

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| CodReg | Number(003,0) | Não | Código da Regra |
| DatApo | Date | Sim | Data Aposentadoria |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R041APO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R041APO_003

**Tabela:** R041REG

| Origem | Destino |
|--------|---------|
| CodReg | CodReg |

