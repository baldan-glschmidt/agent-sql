# E025FER

## Descrição

Tabelas - Feriados Nacionais

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DiaFer | Number(002,0) | Não | Dia do Feriado |
| MesFer | Number(002,0) | Não | Mês do Feriado |
| AnoFer | Number(004,0) | Não | Ano do feriado (caso ele ocorra uma única vez) |
| CepIni | Number(008,0) | Não | Faixa inicial do CEP da cidade |
| CepFim | Number(008,0) | Sim | Faixa final do CEP da cidade |
| DesFer | String(030) | Não | Descrição do feriado |
| FerBan | String(001) | Sim | Indicativo se o feriado é apenas bancário |

---

## Chave Primária

- DiaFer
- MesFer
- AnoFer
- CepIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
