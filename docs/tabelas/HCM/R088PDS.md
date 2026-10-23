# R088PDS

## Descrição

Cadastro de Pagamentos da Despesa

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatDsp | Date | Não | Data Despesa |
| HorDsp | Number(005,0) | Não | Hora Despesa |
| SeqDsp | Number(002,0) | Não | Sequência Despesa |
| DatVen | Date | Não | Data de Vencimento |
| ValPar | Number(011,2) | Sim | Valor da Prestação |

---

## Chave Primária

- DatDsp
- HorDsp
- SeqDsp
- DatVen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088PDS_002

**Tabela:** R088DSP

| Origem | Destino |
|--------|---------|
| DatDsp | DatDsp |
| HorDsp | HorDsp |
| SeqDsp | SeqDsp |

