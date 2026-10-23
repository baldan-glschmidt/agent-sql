# R234ARN

## Descrição

Evento - Avaliação de Reação - Notas do Curso

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| SeqARe | Number(004,0) | Não | Sequência da avaliação de reação |
| CodTnt | Number(003,0) | Não | Item de Nota do Evento |
| NotCur | Number(005,2) | Sim | Nota do item |
| ObsCur | String(500) | Sim | Observação sobre a nota do item |

---

## Chave Primária

- CodEvn
- SeqARe
- CodTnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234ARN_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234ARN_002

**Tabela:** R140NTR

| Origem | Destino |
|--------|---------|
| CodTnt | CodTnt |

