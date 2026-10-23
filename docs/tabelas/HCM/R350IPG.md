# R350IPG

## Descrição

Informações de Pagamentos

---

## Resumo

- Campos: 15
- Chave Primária: 9 campo(s)
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
| DatPag | Date | Não | Data de Pagamento |
| CmpRef | Date | Não | Competência de Referência |
| TipPag | Number(001,0) | Não | Tipo de Pagamento |
| IdeDem | String(030) | Não | Identificador para demonstrativo de pagamento |
| SeqIpg | Number(009,0) | Não | Sequência |
| CodCal | Number(005,0) | Sim | Código de Cálculo |
| QtdDep | Number(002,0) | Sim | Qtd. Dependentes |
| ValDep | Number(014,2) | Sim | Valor Dependente |
| TipIpg | Number(001,0) | Não | Tipo de Gravação do registro |
| ValLiq | Number(014,2) | Sim | Valor Líquido |
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

---

## Índices

### R350IPGIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
