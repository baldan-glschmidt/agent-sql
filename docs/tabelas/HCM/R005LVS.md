# R005LVS

## Descrição

Linhas/Veículos do Serviço

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSrv | Number(004,0) | Não | Código do Serviço |
| CodTSe | Number(002,0) | Não | Turno de Serviço |
| DatAlt | Date | Não |  |
| DiaSem | Number(001,0) | Não | Dia Semana |
| CodSeq | Number(002,0) | Não | Sequência |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodLin | Number(004,0) | Sim | Código da Linha |
| PlaVei | String(010) | Sim | Inutilizado |
| HorIni | Number(005,0) | Sim | Hora Inicial |
| NumVei | Number(006,0) | Sim | Número do Veículo |

---

## Chave Primária

- CodSrv
- CodTSe
- DatAlt
- DiaSem
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005LVS_000

**Tabela:** R005SRV

| Origem | Destino |
|--------|---------|
| CodSrv | CodSrv |

### IR_R005LVS_001

**Tabela:** R005TSE

| Origem | Destino |
|--------|---------|
| CodTSe | CodTSe |

### IR_R005LVS_006

**Tabela:** R005LIN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodLin | CodLin |

