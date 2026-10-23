# R085POF

## Descrição

Param Orçamento - Percentuais - por Filial

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPer | Date | Não | Competência |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| IteOrc | Number(003,0) | Não | Código do Item de Resultado |
| PerIte | Number(008,5) | Sim | Percentual do Item no Local |
| QtdHor | Number(010,0) | Sim | Quantidade de  Horas Extras |
| ValCal | Number(013,4) | Sim | Valor Cálculo |
| PerInc | Number(007,4) | Sim | % Incremento |

---

## Chave Primária

- NumEmp
- CodCen
- CodFil
- CmpPer
- NatDes
- IteOrc

---

## Índices

### R085POFIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodCen
- IteOrc

---

## Relacionamentos

### IR_R085POF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085POF_005

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

