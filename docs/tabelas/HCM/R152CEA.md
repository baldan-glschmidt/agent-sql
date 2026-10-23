# R152CEA

## Descrição

Tabela de Cabeçalho de Envio para Evento Aduaneiro

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código da Pendência de Recintos Aduaneiros |
| TipOpe | String(001) | Não | Tipo da operação |
| IdEvto | String(050) | Sim | Identificador do evento no sistema do recinto |
| DthOco | Date | Não | Data e hora da ocorrência do evento |
| DthReg | Date | Não | Data e hora do registro de evento |
| CPFOco | Number(011,0) | Sim | CPF do operador da ocorrência |
| CPFReg | Number(011,0) | Sim | CPF do operador do registro no sistema |
| Protcl | String(036) | Sim | Protocolo do Evento que está sendo Cancelado/Retificado |
| Contgc | String(001) | Não | Indicativo de contingência |
| CodRec | Number(015,0) | Não | Código do recinto aduaneiro |

---

## Chave Primária

- CodPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
