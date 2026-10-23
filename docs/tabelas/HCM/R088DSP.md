# R088DSP

## Descrição

Cadastro de Despesas de Veículos

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatDsp | Date | Não | Data de Cadastro da Despesa do Veículos |
| HorDsp | Number(005,0) | Não | Hora de Cadastro da Despesa do Veículos |
| SeqDsp | Number(002,0) | Não | Sequência de Cadastro da Despesa do Veículos |
| NumNFS | String(044) | Sim | Número da Nota Fiscal |
| PlaVei | String(010) | Sim | Placa do Veículo |
| CodOem | Number(008,0) | Sim | Código do Fornecedor |
| ValDsp | Number(015,2) | Sim | Valor da Despesa do Veículo |
| ExpSap | String(001) | Sim | Exportado para o ERP |
| OriDsp | Number(001,0) | Sim | Origem Despesa |
| ObsDsp | String(080) | Sim | Observação de Despesa |

---

## Chave Primária

- DatDsp
- HorDsp
- SeqDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
