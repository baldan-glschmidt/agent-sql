# E000EPS

## Descrição

Estados de passagem do percurso do MDF-e

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
| IdePer | Number(009,0) | Não | Identificador do percurso do MDF-e |
| SeqEps | Number(009,0) | Não | Sequencial de passagem do estado do MDF-e |
| UfsPss | String(002) | Não | Estado de passagem do MDF-e |

---

## Chave Primária

- IdePer
- SeqEps

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E000EPS_000

**Tabela:** E000PER

| Origem | Destino |
|--------|---------|
| IdePer | IdeUni |

