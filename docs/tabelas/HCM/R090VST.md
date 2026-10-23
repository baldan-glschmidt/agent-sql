# R090VST

## Descrição

Vistoria de ocorrências na portaria

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Site da Ocorrência |
| DatOcP | Date | Não | Data da Ocorrência na Portaria |
| HorOcP | Number(005,0) | Não | Hora da Ocorrência na Portaria |
| SeqOcP | Number(002,0) | Não | Sequência da Ocorrência na Portaria |
| NumAmb | Number(009,0) | Sim | Ambiente de Ocorrência |
| BltOco | String(021) | Sim | Boletim de ocorrência |
| DelPol | String(021) | Sim | Delegacia de polícia |
| CodVst | String(021) | Sim | Código do termo de vistoria |
| DatVst | Date | Sim | Data da vistoria |
| HorVst | Number(005,0) | Sim | Hora da vistoria |
| CodAgt | String(021) | Sim | Código agente vistoria |
| NomAgt | String(021) | Sim | Nome agente vistoria |
| ObsVst | String(080) | Sim | Observação da vistoria |

---

## Chave Primária

- CodPlt
- DatOcP
- HorOcP
- SeqOcP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
