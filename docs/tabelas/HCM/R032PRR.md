# R032PRR

## Descrição

Produção - Rateio

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipRot | Number(001,0) | Não | Tipo de Rotina |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPrd | Date | Não | Competência |
| SeqPrd | Number(005,0) | Não | Sequência |
| CodRat | Number(009,0) | Não | Código do Rateio |
| PerRat | Number(005,2) | Sim | % Rateio |

---

## Chave Primária

- NumEmp
- CodFil
- TipRot
- CmpPrd
- SeqPrd
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032PRR_004

**Tabela:** R032PRD

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| TipRot | TipRot |
| CmpPrd | CmpPrd |
| SeqPrd | SeqPrd |

### IR_R032PRR_005

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

