# R350IPD

## Descrição

Informações de Pagamentos - Detalhamento

---

## Resumo

- Campos: 18
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| CpfTra | Number(011,0) | Não | CPF do Trabalhador |
| TipFol | Number(001,0) | Não | Tipo Folha |
| CmpRef | Date | Não | Competência de Referência |
| DatPag | Date | Não | Data de Pagamento |
| TipPag | Number(001,0) | Não | Tipo de Pagamento |
| IdeDem | String(030) | Não | Identificador para demonstrativo de pagamento |
| SeqIpg | Number(009,0) | Não | Sequência |
| CodRub | Number(009,0) | Não | Código da Rubrica |
| TabRub | String(008) | Sim | Tabela de Rubrica |
| RefRub | Number(011,2) | Sim | Referência da rubrica |
| ValUni | Number(014,2) | Sim | Valor unitário da rubrica |
| ValRub | Number(014,2) | Sim | Valor total da rubrica |
| FatRub | Number(005,2) | Sim | Fator, Percentual Entre Outros da Rubrica. |
| IncIrr | Number(004,0) | Sim | Código de incidência tributária da rubrica para o IRRF |
| RubEso | String(030) | Sim | Código da rubrica |
| PidExc | String(050) | Sim | Identificador da execução da pendência |

---

## Chave Primária

- NumEmp
- FilEmp
- CpfTra
- TipFol
- DatPag
- CmpRef
- TipPag
- IdeDem
- SeqIpg
- CodRub

---

## Índices

### R350IPDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
