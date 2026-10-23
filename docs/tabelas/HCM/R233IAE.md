# R233IAE

## Descrição

Categoria - Itens de Avaliação do Evento

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CatEvn | Number(003,0) | Não | Categoria do Evento |
| CodTnt | Number(003,0) | Não | Item de Nota do Curso |
| SeqEvn | Number(003,0) | Sim | Sequência para avaliação |
| PesNot | Number(002,0) | Sim | Peso da Nota do Curso |

---

## Chave Primária

- CatEvn
- CodTnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R233IAE_000

**Tabela:** R233CAT

| Origem | Destino |
|--------|---------|
| CatEvn | CatEvn |

### IR_R233IAE_001

**Tabela:** R140NTR

| Origem | Destino |
|--------|---------|
| CodTnt | CodTnt |

