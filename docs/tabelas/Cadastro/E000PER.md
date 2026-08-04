# E000PER

## Descrição

Percursos do MDF-e

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador do percurso do MDF-e |
| UfsOri | String(002) | Não | Estado de origem do MDF-e |
| UfsDes | String(002) | Não | Estado de destino do MDF-e |
| PerPdr | String(001) | Não | Indicativo se é o percurso padrão para esta origem/destino |

---

## Chave Primária

- IdeUni

---

## Índices

### E000PERIndice1

**Tipo:** Não unico

Campos:
- UfsOri
- UfsDes

---

## Relacionamentos

Nenhum relacionamento cadastrado.
