# R102RCO

## Descrição

Reuniões da Brigada - Colaboradores Convidados

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodBri | Number(003,0) | Não | Código da Brigada |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora da Reunião |
| EmpCon | Number(004,0) | Não | Código da empresa do convidado |
| TipCol | Number(001,0) | Não | Tipo colaborador convidado |
| NumCad | Number(009,0) | Não | Cadastro colaborador convidado |
| ObsReu | String(040) | Sim | Observação sobre a participação do convidado |

---

## Chave Primária

- NumEmp
- CodBri
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

### IR_R102RCO_001

**Tabela:** R102BRI

| Origem | Destino |
|--------|---------|
| CodBri | CodBri |

