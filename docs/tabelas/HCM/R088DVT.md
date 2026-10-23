# R088DVT

## Descrição

Despesas de Movimentação de Táxis

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatSol | Date | Não | Data da Movimentação do Veículo |
| HorSol | Number(005,0) | Não | Hora da Movimentação do Veículo |
| SeqSol | Number(002,0) | Não | Sequência da Movimentação |
| PlaVei | String(010) | Sim | Placa do Veículo |
| CodTax | Number(004,0) | Sim | Código Taxista |
| TipTdp | Number(004,0) | Não | Item de Despesa do Veículo |
| ValDsp | Number(011,2) | Sim | Valor Despesa de Táxi |

---

## Chave Primária

- NumEmp
- CodFil
- DatSol
- HorSol
- SeqSol
- TipTdp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088DVT_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R088DVT_004

**Tabela:** R088MTX

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| DatSol | DatSol |
| HorSol | HorSol |
| SeqSol | SeqSol |

### IR_R088DVT_007

**Tabela:** R088TDP

| Origem | Destino |
|--------|---------|
| TipTdp | TipTdp |

