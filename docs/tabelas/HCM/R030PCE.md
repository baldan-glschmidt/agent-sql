# R030PCE

## Descrição

Comissão de Empregados - Participantes da Comissão Eleitoral

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodMan | Number(004,0) | Não | Código do Mandato |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |

---

## Chave Primária

- NumEmp
- CodMan
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030PCE_001

**Tabela:** R030MAN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodMan | CodMan |

### IR_R030PCE_003

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

