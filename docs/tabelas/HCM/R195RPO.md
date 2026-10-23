# R195RPO

## Descrição

Cenário - Rateio por Posto de Trabalho

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
| NumEmp | Number(004,0) | Não | Código da empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CmpOrc | Date | Não | Competência do orçamento |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Posto de Trabalho |
| PosRat | String(024) | Não | Posto de Trabalho Rateado |
| PerRat | Number(005,2) | Sim | % rateio do posto de trabalho |

---

## Chave Primária

- NumEmp
- CodCen
- EstPos
- PosTra
- CmpOrc
- PosRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195RPO_004

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R195RPO_005

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosRat | PosTra |

