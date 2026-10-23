# R085PEC

## Descrição

Param Orçamento - Percentuais -  por C.Custo

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| CmpPer | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| IteOrc | Number(003,0) | Não | Código do Item de Resultado |
| PerIte | Number(008,5) | Sim | Percentual do Item no Local |
| QtdHor | Number(010,0) | Sim | Quantidade de  Horas Extras |
| PerInc | Number(007,4) | Sim | % Incremento |
| ValCal | Number(013,4) | Sim | Valor Cálculo |
| QtdHra | Number(010,0) | Sim | Quantidade de  Horas Extras - rateadas entre as vagas |
| ValRat | Number(013,4) | Sim | Valor Rateado entre as vagas |

---

## Chave Primária

- NumEmp
- CodCen
- CodCcu
- CmpPer
- NatDes
- IteOrc

---

## Índices

### R085PECIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodCen
- IteOrc

---

## Relacionamentos

### IR_R085PEC_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R085PEC_005

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

