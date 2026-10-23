# R041EAP

## Descrição

Aposentadoria - Eventos

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatApo | Date | Sim | Data Aposentadoria |
| TabEve | Number(003,0) | Não | Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| PerEve | Number(007,3) | Sim | Percentual do Evento |
| ProEve | Number(006,2) | Sim | Avos de Proporcionalidade Aposentadoria |
| AvoEve | Number(006,2) | Sim | Avos do Evento |
| CasEve | String(001) | Sim | Aplicar Percentual em Cascata |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R041EAP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

