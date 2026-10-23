# R577CND

## Descrição

Competência - Condições de medição

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCpt | Number(009,0) | Não | Código da Competência |
| RevCpt | String(010) | Não | Código da Revisão da Competência |
| PrfApl | Number(004,0) | Não | Indica a qual Perfil de aplicação a condição de medição pertence |
| SeqCnd | Number(003,0) | Não | Sequência da condição de medição da competência |
| TipApu | Number(001,0) | Sim | Tipo de apuração |
| NotCAd | Number(008,4) | Sim | Nota competência adquirida |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da competência |
| CodCAd | String(010) | Sim | Conceito adquirido |
| PerCAd | Number(007,4) | Sim | Percentual atingido adquirido |
| ConAva | Number(001,0) | Sim | Considerar o conceito da avaliação de desempenho se houver |
| TipRgP | Number(001,0) | Sim | Tipo de registro na apuração proporcional |
| PerMiP | Number(007,4) | Sim | Percentual mínimo atingido na apuração proporcional |

---

## Chave Primária

- CodCpt
- RevCpt
- PrfApl
- SeqCnd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R577CND_000

**Tabela:** R577CPT

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |

### IR_R577CND_001

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

### IR_R577CND_002

**Tabela:** R577PRF

| Origem | Destino |
|--------|---------|
| PrfApl | PrfApl |

