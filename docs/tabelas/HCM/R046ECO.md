# R046ECO

## Descrição

Empréstimo Consignado

---

## Resumo

- Campos: 21
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpIni | Date | Não | Competência início |
| TabEve | Number(003,0) | Não | Código Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| InsFin | Number(003,0) | Sim | Instituição financeira |
| NomIns | String(100) | Sim | Nome da instituição financeira |
| NumCon | Number(015,0) | Sim | Número do contrato |
| NumCtr | String(050) | Sim | Número do contrato alfanumérico |
| CmpFim | Date | Sim | Competência fim |
| OriEco | Number(001,0) | Sim | Origem crédito do trabalhador |
| ObsErv | String(255) | Sim | Observação |
| CmpAu1 | Date | Sim | Campo auxiliar 1 |
| CmpAu2 | Date | Sim | Campo auxiliar 2 |
| CmpAu3 | String(001) | Sim | Campo auxiliar 3 |
| CmpAu4 | Number(009,0) | Sim | Campo auxiliar 4 |
| CmpAu5 | Number(011,2) | Sim | Campo auxiliar 5 |
| CmpAu6 | Number(009,0) | Sim | Campo auxiliar 6 |
| CmpAu7 | String(050) | Sim | Campo auxiliar 7 |
| CmpAu8 | Number(011,2) | Sim | Campo auxiliar 8 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpIni
- TabEve
- CodEve

---

## Índices

### R046ECOIndice1

**Tipo:** Não unico

Campos:
- TabEve
- CodEve

---

## Relacionamentos

### IR_R046ECO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R046ECO_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

