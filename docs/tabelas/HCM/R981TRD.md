# R981TRD

## Descrição

G6 - Detalhes de transações de negócios

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da transação |
| CodTraDet | Number(009,0) | Não | Código do detalhe da transação |
| DesTraDet | String(030) | Sim | Descrição da transação detalhe |
| BinTraDet | Image | Sim | Binário da transação detalhe |
| StaTraDet | Number(004,0) | Sim | Status da transação detalhe |
| UrlTraDet | String(255) | Sim | URL da transação detalhe |
| MetTraDet | String(128) | Sim |  |

---

## Chave Primária

- CodTra
- CodTraDet

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
