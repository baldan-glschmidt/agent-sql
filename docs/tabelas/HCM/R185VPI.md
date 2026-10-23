# R185VPI

## Descrição

Orçamento Individual - Val. Colaborador - Posto

---

## Resumo

- Campos: 15
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| CmpOrc | Date | Não | Competência do orçamento |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do posto de trabalho |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| VerOrc | Number(004,0) | Não | Versão do orçamento |
| RevOrc | Number(004,0) | Não | Revisão da versão do orçamento |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| IteOrc | Number(003,0) | Não | Código do item de orçamento |
| CodCen | Number(004,0) | Sim | Código do cenário |
| IndCal | Number(001,0) | Sim | Tipo de cálculo (1-Base/2-Valor Mensal) |
| ValOrc | Number(011,2) | Sim | Valor do orçamento |
| CodCon | String(030) | Sim | Código da conta contábil |
| CodRed | Number(008,0) | Sim | Código da conta contábil reduzida |

---

## Chave Primária

- NumEmp
- CmpOrc
- EstPos
- PosTra
- AnoBas
- VerOrc
- RevOrc
- TipCol
- NumCad
- IteOrc

---

## Índices

### R185VPIIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- AnoBas
- VerOrc
- RevOrc

---

## Relacionamentos

### IR_R185VPI_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R185VPI_006

**Tabela:** R185REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |
| RevOrc | RevOrc |

### IR_R185VPI_009

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

