# R117QGP

## Descrição

Questionário - Grupo de Perguntas

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodQue | Number(002,0) | Não | Código do Questionário |
| CodPer | Number(002,0) | Não | Código da Pergunta |

---

## Chave Primária

- CodQue
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R117QGP_000

**Tabela:** R117QUE

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |

### IR_R117QGP_001

**Tabela:** R117PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

