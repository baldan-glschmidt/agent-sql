# R108TAR

## Descrição

Atendentes - Área de Atendimento

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAte | Number(006,0) | Não | Código Atendente |
| AreAte | Number(004,0) | Não | Área Médica |
| DurAte | Number(003,0) | Sim | Duração do atendimento em Minutos |

---

## Chave Primária

- CodAte
- AreAte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R108TAR_000

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

### IR_R108TAR_001

**Tabela:** R108ARE

| Origem | Destino |
|--------|---------|
| AreAte | AreAte |

