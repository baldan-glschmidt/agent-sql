# R096EAT

## Descrição

EPI por Atividade

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodAtv | Number(007,0) | Não | Código da Atividade |
| CodEpi | Number(008,0) | Não | Código do EPI |
| DiaVal | Number(004,0) | Sim | Dias de validade do Epi |
| DiaRev | Number(004,0) | Sim | Dias de revisão do Epi |

---

## Chave Primária

- NumEmp
- CodAtv
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096EAT_001

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodAtv | CodAtv |

### IR_R096EAT_002

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

