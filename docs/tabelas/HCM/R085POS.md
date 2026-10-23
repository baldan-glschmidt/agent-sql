# R085POS

## Descrição

Param Orçamento - Percentuais - por Sindicato

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CodSin | Number(004,0) | Não | Código do Sindicato |
| CmpPer | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| IteOrc | Number(003,0) | Não | Código do Item de Resultado |
| PerIte | Number(008,5) | Sim | Percentual do Item no Local |
| QtdHor | Number(010,0) | Sim | Quantidade de  Horas Extras |
| PerInc | Number(007,4) | Sim | % Incremento |
| ValCal | Number(013,4) | Sim | Valor Cálculo |

---

## Chave Primária

- NumEmp
- CodCen
- CodSin
- CmpPer
- NatDes
- IteOrc

---

## Índices

### R085POSIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodCen
- IteOrc

---

## Relacionamentos

### IR_R085POS_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085POS_002

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

### IR_R085POS_005

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

