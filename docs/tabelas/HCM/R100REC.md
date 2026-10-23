# R100REC

## Descrição

Reuniões Cipa - Outros Convidados

---

## Resumo

- Campos: 11
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodFil | Number(006,0) | Sim | Código da Filial |
| CodMan | Number(004,0) | Sim | Código do Mandato |
| DatReu | Date | Sim | Data da Reunião |
| HorReu | Number(005,0) | Sim | Hora da Reunião |
| NomCov | String(040) | Sim | Nome do Convidado |
| FunCov | String(020) | Sim | Função do Convidado |
| EmpCov | String(030) | Sim | Empresa do Convidado |
| ObsReu | String(210) | Sim | Observação sobre a participação do convidado |
| CipTpr | String(001) | Sim | Tipo Presença (P,J,F) |
| TipPar | String(001) | Sim | Define se a participação é necessária/opcional |

---

## Chave Primária

Não possui.

---

## Índices

### R100RECIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- CodFil
- CodMan
- DatReu
- HorReu

---

## Relacionamentos

### IR_R100REC_004

**Tabela:** R100REU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |
| DatReu | DatReu |
| HorReu | HorReu |

