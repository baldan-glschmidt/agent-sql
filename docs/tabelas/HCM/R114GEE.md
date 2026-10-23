# R114GEE

## Descrição

Grupo Etapas Recrutamento/Seleção - Etapas

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGet | Number(003,0) | Não | Código Grupo |
| CodEta | Number(003,0) | Não | Código Etapa |
| TipAva | String(001) | Sim | Tipo de avaliação(N-Nota, P-Parecer) |
| PesEta | Number(002,0) | Sim | Peso da Etapa |
| NotApr | Number(006,2) | Sim | Nota mínima para aprovação(Nota de Corte) |
| IndEta | String(001) | Sim | Identifica se a avaliação é do candidato ou do processo |
| AbrPar | String(050) | Sim | Abrangência de parecer aceitável para aprovação |
| RegAva | Number(003,0) | Sim | Regra para avaliação dos candidatos |
| AbrSit | String(050) | Sim | Abrangência de Situações válidas para a etapa ser considerada |

---

## Chave Primária

- CodGet
- CodEta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R114GEE_000

**Tabela:** R114GET

| Origem | Destino |
|--------|---------|
| CodGet | CodGet |

### IR_R114GEE_001

**Tabela:** R114ETA

| Origem | Destino |
|--------|---------|
| CodEta | CodEta |

