# R034LCO

## Descrição

Colaboradores do Lote

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
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodLot | Number(004,0) | Não | Código do Lote |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |

---

## Chave Primária

- NumEmp
- CodLot
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034LCO_001

**Tabela:** R034LOT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodLot | CodLot |

### IR_R034LCO_003

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

