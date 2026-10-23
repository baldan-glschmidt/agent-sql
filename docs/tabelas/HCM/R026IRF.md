# R026IRF

## Descrição

IRRF - Faixas

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PerRef | Date | Não | Competência |
| CodFai | Number(003,0) | Não | Faixa de Desconto do Imposto de Renda |
| LimFai | Number(011,2) | Sim | Limite da Faixa |
| PerFai | Number(004,2) | Sim | Percentual da Faixa |
| DesFai | Number(011,2) | Sim | Desconto da Faixa |
| VlrAu1 | Number(011,2) | Sim | Campo Auxiliar 1 |

---

## Chave Primária

- PerRef
- CodFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026IRF_000

**Tabela:** R026IRR

| Origem | Destino |
|--------|---------|
| PerRef | PerRef |

