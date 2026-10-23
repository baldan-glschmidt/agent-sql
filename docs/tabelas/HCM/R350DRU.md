# R350DRU

## Descrição

S-2299 - eSocial - Rubricas que compõe a remuneração do trabalhador no período de apuração

---

## Resumo

- Campos: 18
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqDes | Number(009,0) | Não | Sequência |
| SeqRec | Number(009,0) | Não | Sequência |
| SeqDlt | Number(009,0) | Não | Sequência |
| SeqDru | Number(009,0) | Não | Sequência |
| CodRub | String(030) | Sim | Código da rubrica |
| TabRub | String(008) | Sim | Tabela de Rubrica |
| IdeRub | Number(008,0) | Sim | Identificador da tabela de rubricas |
| RefRub | Number(014,2) | Sim | Referência da rubrica |
| ValUni | Number(014,2) | Sim | Valor unitário da rubrica |
| ValRub | Number(014,2) | Sim | Valor total da rubrica |
| ApuIrf | Number(001,0) | Sim | Indicativo de tipo de apuração de IR |
| FatRub | Number(005,2) | Sim | Fator, Percentual Entre Outros da Rubrica. |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| ConRef | String(001) | Sim | Considerar Referência |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqRec
- SeqDlt
- SeqDru

---

## Índices

### R350DRUIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
