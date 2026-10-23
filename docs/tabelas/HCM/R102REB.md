# R102REB

## Descrição

Reuniões da Brigada

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
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
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| DesReu | String(12000) | Sim | Descrição da Reunião |
| LocPos | String(060) | Sim | Descrição do local da reunião |
| NomArq | String(250) | Sim | Arquivo |
| HorTer | Number(005,0) | Sim | Hora do Término da Reunião |
| NroReu | Number(009,0) | Sim | Número de Ordem da Reunião |
| TipReu | Number(002,0) | Sim | Tipo de Reunião |
| SitReu | Number(001,0) | Sim | Situação da Reunião |

---

## Chave Primária

- NumEmp
- CodBri
- DatReu
- HorReu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102REB_001

**Tabela:** R102BRI

| Origem | Destino |
|--------|---------|
| CodBri | CodBri |

