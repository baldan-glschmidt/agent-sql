# R104SEP

## Descrição

JR - Sentença - Trabalhista - Pagamentos

---

## Resumo

- Campos: 13
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CmpPag | Date | Não | Competência de pagamento da parcela |
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| PerIni | Date | Não | Período de início do direito |
| PerFim | Date | Sim | Período de fim de direito |
| ValEve | Number(011,2) | Sim | Valor do evento |
| CodCal | Number(005,0) | Sim | Código do cálculo em que foi efetuado a integração |
| OriPar | Number(001,0) | Sim | Origem da parcela(1-Digitada, 2-Rateada) |

---

## Chave Primária

- NumEmp
- CodPrc
- EmpAut
- TipCol
- NumCad
- CmpPag
- CodTab
- CodEve
- PerIni

---

## Índices

### R104SEPIndice2

**Tipo:** Não unico

Campos:
- EmpAut
- CodCal

---

## Relacionamentos

### IR_R104SEP_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

### IR_R104SEP_007

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

