# R110MHQ

## Descrição

Histórico de Grupos de Questionário

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFic | Number(009,0) | Não | Código da Ficha Médica |
| CodGrq | Number(003,0) | Não | Código do Grupo Questionário |
| DatGrq | Date | Não | Data Respostas |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| CodExa | Number(004,0) | Sim | Código do exame relacionado a este questionário |
| DatSol | Date | Sim | Data solicitação do exame relacionado a este questionário |
| DatAte | Date | Sim | Data do atendimento relacionado a este questionário |
| HorAte | Number(005,0) | Sim | Hora do atendimento relacionado a este questionário |
| DatIni | Date | Sim | Data início da subnormalidade |
| CodSun | Number(006,0) | Sim | Código da subnormalidade |
| DatAco | Date | Sim | Data do último acompanhamento |

---

## Chave Primária

- NumEmp
- CodFic
- CodGrq
- DatGrq

---

## Índices

### R110MHQIndice2

**Tipo:** Não unico

Campos:
- CodGrq

---

## Relacionamentos

### IR_R110MHQ_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

