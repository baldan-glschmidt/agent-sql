# R050CMG

## Descrição

Compensações DARF

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRec | Number(004,0) | Não | Código da Receita |
| DatApu | Date | Não | Data da Apuração |
| NumPar | Number(002,0) | Não | Número da Parcela |
| DatRec | Date | Sim | Data Recolhimento |
| CmpOri | Number(011,2) | Sim | Valor a Compensar Original |
| ObsCmp | String(050) | Sim | Observações da Compensação |

---

## Chave Primária

- NumEmp
- CodFil
- CodRec
- DatApu
- NumPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R050CMG_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R050CMG_002

**Tabela:** R050REC

| Origem | Destino |
|--------|---------|
| CodRec | CodRec |

