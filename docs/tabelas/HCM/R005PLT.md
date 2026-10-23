# R005PLT

## Descrição

Funcionários em Plantão

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTrm | Number(002,0) | Não | Terminal |
| DatPlt | Date | Não | Data do Plantão |
| CodTur | Number(002,0) | Não | Turno do Plantão |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |

---

## Chave Primária

- CodTrm
- DatPlt
- CodTur
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005PLT_000

**Tabela:** R005TRM

| Origem | Destino |
|--------|---------|
| CodTrm | CodTrm |

### IR_R005PLT_003

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

