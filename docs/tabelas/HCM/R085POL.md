# R085POL

## Descrição

Param Orçamento - Percentuais - por Local

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CmpPer | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| IteOrc | Number(003,0) | Não | Código do Item de Resultado |
| PerIte | Number(008,5) | Sim | Percentual do Item no Local |
| QtdHor | Number(010,0) | Sim | Quantidade de  Horas Extras |
| ValCal | Number(013,4) | Sim | Valor Cálculo |
| PerInc | Number(007,4) | Sim | % Incremento |
| QtdHra | Number(010,0) | Sim | Quantidade de  Horas Extras - rateadas entre as vagas |
| ValRat | Number(013,4) | Sim | Valor Rateado entre as vagas |

---

## Chave Primária

- NumEmp
- CodCen
- TabOrg
- NumLoc
- CmpPer
- NatDes
- IteOrc

---

## Índices

### R085POLIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodCen
- IteOrc

---

## Relacionamentos

### IR_R085POL_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085POL_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R085POL_006

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

