# R110MED

## Descrição

Medicamentos - Administração Ambulatório

---

## Resumo

- Campos: 24
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatAte | Date | Não | Data do Atendimento |
| HorAte | Number(005,0) | Não | Hora do Atendimento |
| CodRem | Number(006,0) | Não | Código do Medicamento |
| DatAdm | Date | Sim | Data da administração |
| HorAdm | Number(005,0) | Sim | Hora da Administração |
| CodAte | Number(006,0) | Sim | Código do atendente que receitou a medicação |
| NumRec | Number(006,0) | Sim | Número da Receita Médica |
| CodOco | Number(006,0) | Sim | Código da Ocorrência |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| CodCid | String(010) | Sim | Código da Classificação Internacional de Doenças |
| ObsAdm | String(500) | Sim | Recomendações para administração do medicamento |
| AnoAdm | String(500) | Sim | Anotações da administração do medicamento |
| AteAdm | Number(006,0) | Sim | Código do atendente que administrou o medicamento |
| QtdApl | Number(010,4) | Sim | Quantidade de medicação administrada |
| QtdDoa | Number(010,4) | Sim | Quantidade de medicação doada |
| CodApr | Number(003,0) | Sim | Cód. forma de apresentação medicamento administrado |
| CodApd | Number(003,0) | Sim | Cód. forma de apresentação medicamento doado |
| IndSol | String(001) | Sim | Solicitação atendida (Sim/Não) |
| CodPos | Number(007,0) | Sim | Código do posto  de atendimento |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID-10 |
| CodCia | String(010) | Sim | Código único do CIAP-2 |
| FusHor | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- NumEmp
- CodFic
- DatAte
- HorAte
- CodRem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110MED_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110MED_004

**Tabela:** R110REM

| Origem | Destino |
|--------|---------|
| CodRem | CodRem |

### IR_R110MED_007

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

