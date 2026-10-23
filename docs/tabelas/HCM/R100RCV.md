# R100RCV

## Descrição

Reuniões Cipa - Colaboradores Convidados

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa do mandato |
| CodFil | Number(006,0) | Não | Código da filial do mandato |
| CodMan | Number(004,0) | Não | Código do mandato |
| DatReu | Date | Não | Data da reunião |
| HorReu | Number(005,0) | Não | Hora da reunião |
| EmpCon | Number(004,0) | Não | Código da empresa do convidado |
| TipCol | Number(001,0) | Não | Tipo colaborador convidado |
| NumCad | Number(009,0) | Não | Cadastro colaborador convidado |
| ObsReu | String(210) | Sim | Observação sobre a participação |
| CipTpr | String(001) | Sim | Tipo Presença (P,J,F) |
| TipPar | String(001) | Sim | Define se a participação é N-necessária ou 0-opcional |

---

## Chave Primária

- NumEmp
- CodFil
- CodMan
- DatReu
- HorReu
- EmpCon
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R100RCV_004

**Tabela:** R100REU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |
| DatReu | DatReu |
| HorReu | HorReu |

