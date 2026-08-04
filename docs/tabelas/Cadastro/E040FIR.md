# E040FIR

## Descrição

Tabelas - Tabelas IRRF - Faixas

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CptIrf | Date | Não | Mês e ano de competência dos valores do IRRF |
| LimFai | Number(015,2) | Não | Maior valor limite da faixa do IRRF |
| PerFai | Number(004,2) | Sim | Percentual de desconto da faixa do IRRF |
| AbtFai | Number(015,2) | Sim | Valor do abatimento da faixa do IRRF |

---

## Chave Primária

- CptIrf
- LimFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E040FIR_000

**Tabela:** E040IRF

| Origem | Destino |
|--------|---------|
| CptIrf | CptIrf |

