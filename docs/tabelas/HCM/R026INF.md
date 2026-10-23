# R026INF

## Descrição

Previdência - Faixas INSS

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PerRef | Date | Não | Competência |
| CodFai | Number(002,0) | Não | Faixa Desconto do INSS |
| TetFai | Number(011,2) | Sim | Teto da Faixa do INSS |
| PerFai | Number(004,2) | Sim | Percentual de desconto da faixa do INSS |
| ParDed | Number(011,2) | Sim | Parcela a Deduzir do INSS |

---

## Chave Primária

- PerRef
- CodFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026INF_000

**Tabela:** R026INS

| Origem | Destino |
|--------|---------|
| PerRef | PerRef |

