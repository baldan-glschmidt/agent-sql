# R110ARC

## Descrição

Atendimentos - Receitas do Atendimento

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatAte | Date | Não | Data do Atendimento |
| HorAte | Number(005,0) | Não | Hora do Atendimento |
| CodAte | Number(006,0) | Não | Código do Atendente |
| NumRec | Number(006,0) | Não | Número da Receita Médica |

---

## Chave Primária

- NumEmp
- CodFic
- DatAte
- HorAte
- CodAte
- NumRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110ARC_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110ARC_003

**Tabela:** R110MAT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |
| DatAte | DatAte |
| HorAte | HorAte |

### IR_R110ARC_005

**Tabela:** R110MRC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodAte | CodAte |
| NumRec | NumRec |

