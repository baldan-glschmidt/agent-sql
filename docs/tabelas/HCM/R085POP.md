# R085POP

## Descrição

Param Orçamento - Percentuais - por Posto

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Posto de trabalho |
| CmpPer | Date | Não | Competência |
| IteOrc | Number(003,0) | Não | Código do item de orçamento |
| PerIte | Number(008,5) | Sim | Percentual do item no posto de trabalho |
| QtdHor | Number(010,0) | Sim | Quantidade de horas extras |
| PerInc | Number(007,4) | Sim | Percentual de incremento |
| ValCal | Number(013,4) | Sim | Valor de cálculo |
| QtdHra | Number(010,0) | Sim | Quantidade de horas extras - rateadas entre as vagas |
| ValRat | Number(013,4) | Sim | Valor rateado entre as vagas |
| RepHor | String(001) | Sim | Replicar quantidade de horas extras ou valor a todos os ocupantes do posto |

---

## Chave Primária

- NumEmp
- CodCen
- EstPos
- PosTra
- CmpPer
- IteOrc

---

## Índices

### R085POPIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- CodCen
- IteOrc

---

## Relacionamentos

### IR_R085POP_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R085POP_005

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

