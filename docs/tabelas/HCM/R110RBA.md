# R110RBA

## Descrição

Medicamentos - Baixa de estoque

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRem | Number(006,0) | Não | Código do Medicamento |
| CodPos | Number(007,0) | Não | Código do posto de atendimento |
| DatBai | Date | Não | Data da baixa de medicamento em estoque |
| SeqBai | Number(002,0) | Não | Sequência da baixa de medicamento em estoque |
| QtdBai | Number(010,4) | Sim | Quantidade de medicamento |
| CodJus | Number(003,0) | Sim | Código da justificativa |
| FusHor | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- CodRem
- CodPos
- DatBai
- SeqBai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110RBA_000

**Tabela:** R110REM

| Origem | Destino |
|--------|---------|
| CodRem | CodRem |

