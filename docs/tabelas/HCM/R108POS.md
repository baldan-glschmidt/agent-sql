# R108POS

## Descrição

Atendentes - Pós-Atendentes

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAte | Number(006,0) | Não | Código Atendente |
| AtePos | Number(006,0) | Não | Código do atendente do pós atendimento |
| CodAgd | Number(003,0) | Sim | Motivo do agendamento utilizado para geração do pós-atendimento |

---

## Chave Primária

- CodAte
- AtePos

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R108POS_000

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

### IR_R108POS_001

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| AtePos | CodAte |

### IR_R108POS_002

**Tabela:** R110MAG

| Origem | Destino |
|--------|---------|
| CodAgd | CodAgd |

