# R122CAN

## Descrição

Candidatos Externos - Candidaturas

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Número do candidato externo |
| CodVag | String(010) | Não | Código da vaga usado na publicação do anúncio |
| DatCan | Date | Sim | Data da candidatura ao anúncio |
| HorCan | Number(005,0) | Sim | Hora da candidatura ao anúncio |
| SitCnd | Number(001,0) | Sim | Situação da Candidatura |
| MotCan | String(040) | Sim | Motivo do cancelamento/desistência do candidato |
| OriCad | String(001) | Sim | Origem da Candidatura (W=Web, S=Sistema) |

---

## Chave Primária

- NumCan
- CodVag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CAN_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CAN_001

**Tabela:** R126ANU

| Origem | Destino |
|--------|---------|
| CodVag | CodVag |

