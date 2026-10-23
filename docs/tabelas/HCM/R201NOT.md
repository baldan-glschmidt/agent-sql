# R201NOT

## Descrição

Notas e Conceitos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTbn | Number(003,0) | Não | Código da Tabela de Notas |
| DatNot | Date | Não | Data da Tabela de Notas e Conceitos |
| CodNot | Number(005,2) | Não | Código da Nota |
| CctNot | String(040) | Sim | Conceito da Nota |
| PesNot | Number(002,0) | Sim | Define o peso da nota (rotina de Pesquisa) |
| ObsNot | String(750) | Sim | Conceituação detalhada sobre a nota |

---

## Chave Primária

- CodTbn
- DatNot
- CodNot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R201NOT_000

**Tabela:** R201TBN

| Origem | Destino |
|--------|---------|
| CodTbn | CodTbn |

