# R350IPB

## Descrição

Informações de Pagamentos - Pensão Judicial

---

## Resumo

- Campos: 15
- Chave Primária: 11 campo(s)
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
| CpfDep | Number(011,0) | Não | CPF do Dependente |
| NomDep | String(070) | Não | Nome do Dependente |
| DatNas | Date | Sim | Data de Nascimento do Dependente |
| ValPen | Number(014,2) | Sim | Valor da pensão |
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
- CpfDep

---

## Índices

### R350IPBIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
