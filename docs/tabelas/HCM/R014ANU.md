# R014ANU

## Descrição

Anuidades

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| CmpNor | Date | Não | Competência Sal.Normativo |
| NumAnu | Number(002,0) | Não | Número de anos da anuidade |
| ValAnu | Number(011,2) | Sim | Valor da Anuidade |

---

## Chave Primária

- CodSin
- CmpNor
- NumAnu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014ANU_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

