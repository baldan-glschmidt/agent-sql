# R110CBH

## Descrição

Atendimentos - Procedimentos CBHPM

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatAte | Date | Não | Data do Atendimento |
| HorAte | Number(005,0) | Não | Hora do Atendimento |
| CodCBH | Number(008,0) | Não | Classificação Hierarquizada de Procedimentos Médicos |
| CodAte | Number(006,0) | Sim | Código do atendente responsável pelo procedimento |
| AtePos | Number(006,0) | Sim | Código do atendente do Pós-Atendimemto |
| IndRea | String(001) | Sim | Indica se o procedimento foi realizado |
| ObsPro | String(1000) | Sim | Observação/Recomendação sobre  o procedimento |
| ObsRea | String(1000) | Sim | Observação sobre a realização do procedimento |

---

## Chave Primária

- NumEmp
- CodFic
- DatAte
- HorAte
- CodCBH

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110CBH_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110CBH_004

**Tabela:** R190CBH

| Origem | Destino |
|--------|---------|
| CodCBH | CodCBH |

