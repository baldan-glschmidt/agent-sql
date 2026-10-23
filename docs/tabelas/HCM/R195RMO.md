# R195RMO

## Descrição

Cenário - Rateio por Colaborador

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do empregado |
| CmpOrc | Date | Não | Competência do orçamento |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosRat | String(024) | Não | Posto de Trabalho Rateado |
| PerRat | Number(005,2) | Sim | % rateio do posto de trabalho |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- CmpOrc
- EstPos
- PosRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195RMO_006

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosRat | PosTra |

