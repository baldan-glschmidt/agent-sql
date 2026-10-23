# R234RRE

## Descrição

Evento - Recorrência Recursos Instrucionais

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| RecHor | Number(004,0) | Não | Recorrência do Horário |
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| QtdRei | Number(004,0) | Sim | Quantidade de Recursos Instrucionais |

---

## Chave Primária

- CodEvn
- RecHor
- CodRei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234RRE_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234RRE_001

**Tabela:** R234RHO

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |
| RecHor | RecHor |

### IR_R234RRE_002

**Tabela:** R140REI

| Origem | Destino |
|--------|---------|
| CodRei | CodRei |

