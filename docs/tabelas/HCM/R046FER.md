# R046FER

## Descrição

Ficha Financeira - Eventos Férias por Rateio - eSocial

---

## Resumo

- Campos: 15
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| IniPer | Date | Não | Data Início do Período |
| IniFer | Date | Não | Data Início das Férias |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodRat | Number(009,0) | Não | Código do Rateio |
| RefEve | Number(011,2) | Sim | Referência Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
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
- CodRat

---

## Índices

### R046FERIndice2

**Tipo:** Não unico

Campos:
- CodCal
- CodEve

---

## Relacionamentos

### IR_R046FER_008

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

