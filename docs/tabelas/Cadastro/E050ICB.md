# E050ICB

## Descrição

Composição para estorno dos créditos ICMS Monofásico

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
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Sim | Código da transação |
| InsCbt | String(014) | Sim | Insumo para combustível |

---

## Chave Primária

- IdeUni

---

## Índices

### E050ICB_UK

**Tipo:** Unico

Campos:
- CodEmp
- CodTns
- InsCbt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
