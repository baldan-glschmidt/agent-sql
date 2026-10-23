# R234NPA

## Descrição

Evento - Notas dos Participantes

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| CodTnt | Number(003,0) | Não | Item de Nota do Participante |
| NotPar | Number(005,2) | Sim | Nota do Participante |
| ObsPar | String(500) | Sim | Observação sobre a nota do participante |
| DatNpa | Date | Sim | Data de lançamento da nota |

---

## Chave Primária

- CodEvn
- CodPes
- CodTnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234NPA_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234NPA_001

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R234NPA_002

**Tabela:** R140NTR

| Origem | Destino |
|--------|---------|
| CodTnt | CodTnt |

