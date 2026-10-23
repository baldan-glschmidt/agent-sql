# R185VPO

## Descrição

Orçamento Individual - Val. Alteração Quadro - Posto

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpOrc | Date | Não | Competência Orçamento |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do posto de trabalho |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| VerOrc | Number(004,0) | Não | Versão do orçamento |
| RevOrc | Number(004,0) | Não | Revisão da versão do orçamento |
| IteOrc | Number(003,0) | Não | Item de orçamento |
| CodCen | Number(004,0) | Sim | Código do cenário |
| IndCal | Number(001,0) | Sim | Tipo de cálculo(1-Base/2-Valor Mensal) |
| ValOrc | Number(011,2) | Sim | Valor do Orçamento |
| CodCon | String(030) | Sim | Código da conta contábil |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |

---

## Chave Primária

- NumEmp
- CmpOrc
- EstPos
- PosTra
- AnoBas
- VerOrc
- RevOrc
- IteOrc

---

## Índices

### R185VPOIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- AnoBas
- VerOrc
- RevOrc

---

## Relacionamentos

### IR_R185VPO_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R185VPO_006

**Tabela:** R185REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |
| RevOrc | RevOrc |

### IR_R185VPO_007

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

