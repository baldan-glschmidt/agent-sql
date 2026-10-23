# R014DFP

## Descrição

Direito de férias por períodos trabalhados

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| QtdPer | Number(002,0) | Não | Quantidade de Períodos trabalhados |
| DiaFer | Number(002,0) | Sim | Dias de direito de férias |

---

## Chave Primária

- CodSin
- QtdPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014DFP_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

