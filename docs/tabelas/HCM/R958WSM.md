# R958WSM

## Descrição

WebService Comunicados - Controle Mensagens Enviadas

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NamIde | String(050) | Não | Identificador único da pendência |
| DatPub | Number(014,6) | Sim | Data e hora da publicação do comunicado |
| VerHTM | String(010) | Sim | Versão de publicação do HTML |
| RanVer | String(200) | Sim | Série de versões dos produtos que devem exibir o comunicado |
| TagPro | String(200) | Sim | Rótulos para validação dos produtos para exibir o comunicado |
| DatVal | Number(014,6) | Sim | Data e hora de validade para exibição do comunicado |
| TxtHTM | String(5999) | Sim | Conteúdo do HTML do comunicado |

---

## Chave Primária

- NamIde

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
