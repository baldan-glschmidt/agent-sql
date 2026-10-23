# R165VAL

## Descrição

BS - Valores Trajetos

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
| CodTra | Number(006,0) | Não | Código do Trajeto |
| DatTra | Date | Não | Data de Valores de Trajetos |
| ValTra | Number(011,2) | Sim | Valor do Trajeto |

---

## Chave Primária

- CodTra
- DatTra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R165VAL_000

**Tabela:** R165TRA

| Origem | Destino |
|--------|---------|
| CodTra | CodTra |

