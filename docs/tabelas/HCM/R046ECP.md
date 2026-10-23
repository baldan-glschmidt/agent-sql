# R046ECP

## Descrição

Empréstimo Consignado - Parcelas

---

## Resumo

- Campos: 27
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpIni | Date | Não | Competência de início |
| TabEve | Number(003,0) | Não | Código Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| PerRef | Date | Não | Competência |
| ValPar | Number(011,2) | Sim | Valor da parcela |
| ValEmp | Number(011,2) | Sim | Valor do empréstimo |
| ValLib | Number(011,2) | Sim | Valor liberado |
| QtdPar | Number(003,0) | Sim | Quantidade de parcelas |
| IniDes | Date | Sim | Competência do início do desconto |
| FimDes | Date | Sim | Competência do fim do desconto |
| QtdPag | Number(003,0) | Sim | Quantidade de pagamentos |
| QtdEsc | Number(003,0) | Sim | Quantidade de escriturações |
| IniCon | Date | Sim | Início do contrato |
| FimCon | Date | Sim | Fim do contrato |
| OriLan | Number(001,0) | Sim | Origem do movimento |
| CmpAu1 | Date | Sim | Campo auxiliar 1 |
| CmpAu2 | Date | Sim | Campo auxiliar 2 |
| CmpAu3 | String(001) | Sim | Campo auxiliar 3 |
| CmpAu4 | Number(009,0) | Sim | Campo auxiliar 4 |
| CmpAu5 | Number(011,2) | Sim | Campo auxiliar 5 |
| CmpAu6 | Number(009,0) | Sim | Campo auxiliar 6 |
| CmpAu7 | String(050) | Sim | Campo auxiliar 7 |
| CmpAu8 | String(100) | Sim | Campo auxiliar 8 |
| CmpAu9 | Number(011,2) | Sim | Campo auxiliar 9 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpIni
- TabEve
- CodEve
- PerRef

---

## Índices

### R046ECPIndice1

**Tipo:** Não unico

Campos:
- TabEve
- CodEve

---

## Relacionamentos

### IR_R046ECP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R046ECP_005

**Tabela:** R046ECO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpIni | CmpIni |
| TabEve | TabEve |
| CodEve | CodEve |

