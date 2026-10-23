# R904LMC

## Descrição

Restrições aplicadadas no sistema

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ID | String(255) | Não | Identificador da restrição aplicada |
| KND | Number(004,0) | Não | Tipo da restrição aplicada |
| VALDAD | Date | Sim | Validade da restrição aplicada |
| CURINT | Date | Sim | Instante da restrição aplicada |
| CURVAL | Number(015,0) | Não | Valor corrente da restrição aplicada |
| LMTVAL | Number(015,0) | Não | Limite da restrição aplicada |
| WBSERR | Number(001,0) | Não | Número do erro webservice da restrição aplicada |
| SISERR | Number(001,0) | Não | Número do erro de sistema da restrição aplicada |
| ERRMSG | String(255) | Não | Mensagem de erro relativa a restrição aplicada |

---

## Chave Primária

- ID

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
