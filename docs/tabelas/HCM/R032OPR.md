# R032OPR

## Descrição

Pagtos Outras Empresas - Rateio

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
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPoe | Date | Não | Competência de Pagto O.Empresa |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| SeqPoe | Number(003,0) | Não | Sequência |
| CodRat | Number(009,0) | Não | Código do Rateio |
| PerRat | Number(005,2) | Sim | % Rateio |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPoe
- CodOem
- SeqPoe
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032OPR_004

**Tabela:** R032OPG

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CmpPoe | CmpPoe |
| CodOem | CodOem |
| SeqPoe | SeqPoe |

### IR_R032OPR_005

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

