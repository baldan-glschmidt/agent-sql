# R234RIN

## Descrição

Evento - Recorrência Instrutores

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
| CodPes | Number(009,0) | Não | Código da Pessoa |
| ObsIns | String(500) | Sim | Dados complementares do instrutor |

---

## Chave Primária

- CodEvn
- RecHor
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234RIN_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234RIN_001

**Tabela:** R234RHO

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |
| RecHor | RecHor |

### IR_R234RIN_002

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

