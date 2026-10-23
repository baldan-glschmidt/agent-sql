# R100REP

## Descrição

Reuniões Cipa - Participantes

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodMan | Number(004,0) | Não | Código do Mandato |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora da Reunião |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Presente |
| CipTpr | String(001) | Sim | Tipo Presença (P,J,F) |
| ObsReu | String(210) | Sim | Observação sobre a Participação |
| PreReu | String(001) | Sim | Indica se o participante presidiu a reunião |
| TipPar | String(001) | Sim | Define se a participação é N-necessária ou 0-opcional |

---

## Chave Primária

- NumEmp
- CodFil
- CodMan
- DatReu
- HorReu
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R100REP_004

**Tabela:** R100REU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |
| DatReu | DatReu |
| HorReu | HorReu |

### IR_R100REP_006

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

