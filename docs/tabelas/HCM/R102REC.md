# R102REC

## Descrição

Reuniões da Brigada - Outros Convidados

---

## Resumo

- Campos: 6
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodBri | Number(003,0) | Sim | Código da Brigada |
| DatReu | Date | Sim | Data da Reunião |
| HorReu | Number(005,0) | Sim | Hora da Reunião |
| NomCon | String(040) | Sim | Nome do Convidado |
| ObsReu | String(040) | Sim | Observação sobre a participação do convidado |

---

## Chave Primária

Não possui.

---

## Índices

### R102RECIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- CodBri
- DatReu
- HorReu

---

## Relacionamentos

### IR_R102REC_001

**Tabela:** R102BRI

| Origem | Destino |
|--------|---------|
| CodBri | CodBri |

