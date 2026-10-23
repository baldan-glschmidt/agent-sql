# R124CAN

## Descrição

Colaborador - Candidaturas

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| CodVag | String(010) | Não | Código da vaga usado na publicação do anúncio |
| DatCan | Date | Sim | Data da candidatura ao anúncio |
| HorCan | Number(005,0) | Sim | Hora da candidatura ao anúncio |
| SitCnd | Number(001,0) | Sim | Situação da Candidatura |
| MotCan | String(040) | Sim | Motivo do cancelamento/desistência do candidato |
| OriCad | String(001) | Sim | Origem da Candidatura (W=Web, S=Sistema) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodVag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124CAN_003

**Tabela:** R126ANU

| Origem | Destino |
|--------|---------|
| CodVag | CodVag |

