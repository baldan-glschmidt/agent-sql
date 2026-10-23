# R088IDS

## Descrição

Cadastro de Itens da Despesa do Veículo

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatDsp | Date | Não | Data da Despesa do Veículo |
| HorDsp | Number(005,0) | Não | Hora Despesa |
| SeqDsp | Number(002,0) | Não | Sequência Despesa |
| TipTdp | Number(004,0) | Não | Item de Despesa do Veículo |
| ValDsp | Number(011,2) | Sim | Valor da Despesa do Veículo |
| NumEmp | Number(004,0) | Sim | Empresa do C.Custo |
| CodCcu | String(018) | Sim | Código Centro Custo Contábil |
| ObsDsp | String(100) | Sim | Observação da Despesa do Veículo |

---

## Chave Primária

- DatDsp
- HorDsp
- SeqDsp
- TipTdp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088IDS_002

**Tabela:** R088DSP

| Origem | Destino |
|--------|---------|
| DatDsp | DatDsp |
| HorDsp | HorDsp |
| SeqDsp | SeqDsp |

### IR_R088IDS_003

**Tabela:** R088TDP

| Origem | Destino |
|--------|---------|
| TipTdp | TipTdp |

