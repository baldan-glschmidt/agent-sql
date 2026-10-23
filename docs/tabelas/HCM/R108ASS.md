# R108ASS

## Descrição

Exames - Documentos

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| CodExa | Number(004,0) | Não | Código do exame |
| DatSol | Date | Não | Data Solicitação do Exame |
| SeqDoc | Number(002,0) | Não | Sequência do documento |
| DesDoc | String(250) | Sim | Descrição do documento |
| DocuId | String(050) | Sim | Identificador único do documento no GED (DocumentId) |
| EnveId | String(050) | Sim | Identificador único do envelope no GED (EnvelopeId) |
| SitAss | Number(001,0) | Sim | Status da assinatura do documento no GED/SIGN |

---

## Chave Primária

- NumEmp
- CodFic
- CodExa
- DatSol
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
