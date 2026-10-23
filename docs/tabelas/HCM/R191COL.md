# R191COL

## Descrição

Objetivos Coletivos - Colaboradores Avaliados

---

## Resumo

- Campos: 9
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência |
| EmpAvl | Number(004,0) | Não | Código da Empresa do Avaliado |
| TipAvl | Number(001,0) | Não | Tipo Colaborador Avaliado |
| CadAvl | Number(009,0) | Não | Código do Colaborador Avaliado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva
- EmpAvl
- TipAvl
- CadAvl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R191COL_005

**Tabela:** R191AVA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| TipAva | TipAva |
| SeqAva | SeqAva |

