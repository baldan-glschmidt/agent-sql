# R104BPE

## Descrição

JR - Base Percentuais de Cálculo - Cenário

---

## Resumo

- Campos: 11
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatCen | Date | Não | Data do cenário |
| SeqCen | Number(002,0) | Não | Sequência do cenário |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CmpPer | Date | Não | Competência de referência do percentual |
| CodMtj | Number(003,0) | Não | Código do Motivo do Pedido |
| PerPed | Number(008,5) | Sim | Percentual para uso no cálculo do pedido |
| RecIrr | Number(006,0) | Sim | Código de Receita - CR relativo a Imposto de Renda Retido na Fonte |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad
- CmpPer
- CodMtj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104BPE_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

### IR_R104BPE_008

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

