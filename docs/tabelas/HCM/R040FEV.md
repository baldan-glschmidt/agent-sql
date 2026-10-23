# R040FEV

## Descrição

Recibo de Férias - Eventos

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| IniPer | Date | Não | Data Início do Período |
| IniFer | Date | Não | Data Início das Férias |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| RefEve | Number(011,2) | Sim | Referência do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| OriEve | String(001) | Sim | Origem do Evento |
| CodRub | Number(009,0) | Sim | Código da rubrica |
| FatRub | Number(005,2) | Sim | Fator, Percentual Entre Outros da Rubrica. |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- IniFer
- TabEve
- CodEve

---

## Índices

### R040FEVIndice2

**Tipo:** Não unico

Campos:
- CodRub
- NumEmp

---

## Relacionamentos

### IR_R040FEV_003

**Tabela:** R040PER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |

### IR_R040FEV_004

**Tabela:** R040FEM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |
| IniFer | IniFer |

### IR_R040FEV_006

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

