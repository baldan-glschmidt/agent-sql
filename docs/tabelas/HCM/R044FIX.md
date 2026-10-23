# R044FIX

## Descrição

Eventos fixos

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código Evento Fixo |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ValEve | Number(011,2) | Sim | Valor Evento Fixo |
| ValEmp | Number(011,2) | Sim | Valor do Empréstimo |
| DatIni | Date | Não | Data de Início da Validade do Evento |
| DatFim | Date | Sim | Data de Fim de Validade do Evento |
| USU_QtdPar | Number(002,0) | Sim | Quantidade de Parcelas |
| USU_ObsInt | String(200) | Sim | Observação da Interrupção |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodEve
- CodRat
- DatIni

---

## Índices

### R044FIXIndice2

**Tipo:** Não unico

Campos:
- TabEve
- CodEve

---

## Relacionamentos

### IR_R044FIX_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R044FIX_004

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

