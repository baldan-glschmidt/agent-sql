# R046FEE

## Descrição

Ficha Financeira - Eventos Férias - eSocial

---

## Resumo

- Campos: 17
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| IniPer | Date | Não | Data Início do Período |
| IniFer | Date | Não | Data Início das Férias |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| RefEve | Number(011,2) | Sim | Referência do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| OriEve | String(001) | Sim | Origem do Evento |
| CodRub | Number(009,0) | Sim | Código da rubrica |
| FatRub | Number(005,2) | Sim | Fator, Percentual Entre Outros da Rubrica. |
| CmpAu1 | Number(011,2) | Sim | Campo Auxiliar 1 |
| CmpAu2 | Number(009,0) | Sim | Campo Auxiliar 2 |
| CmpAu3 | Date | Sim | Campo Auxiliar 3 |
| CmpAu4 | String(100) | Sim | Campo Auxiliar 4 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- IniPer
- IniFer
- TabEve
- CodEve

---

## Índices

### R046FEEIndice2

**Tipo:** Não unico

Campos:
- CodRub
- NumEmp

---

## Relacionamentos

### IR_R046FEE_007

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

