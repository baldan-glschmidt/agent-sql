# R102RBP

## Descrição

Reuniões da Brigada - Participantes

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodBri | Number(003,0) | Não | Código da Brigada |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora da Reunião |
| EmpPar | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| ParPre | String(001) | Sim | Participante Presente |
| ObsReu | String(500) | Sim | Observação sobre a participação |

---

## Chave Primária

- NumEmp
- CodBri
- DatReu
- HorReu
- EmpPar
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102RBP_003

**Tabela:** R102REB

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodBri | CodBri |
| DatReu | DatReu |
| HorReu | HorReu |

### IR_R102RBP_006

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpPar | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

