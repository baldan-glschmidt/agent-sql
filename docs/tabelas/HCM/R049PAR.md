# R049PAR

## Descrição

Empréstimo Consignado - Parcelas

---

## Resumo

- Campos: 20
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodBan | Number(004,0) | Não | Código do Banco |
| DatEmp | Date | Não | Data do Empréstimo |
| SeqEmp | Number(002,0) | Não | Sequência do Empréstimo |
| NumPar | Number(003,0) | Não | Número da Parcela |
| ValPar | Number(011,2) | Sim | Valor da Parcela |
| ValBa1 | Number(011,2) | Sim | Valor da Taxa do Banco |
| ValBa2 | Number(011,2) | Sim | Valor da Taxa do Banco |
| ValBa3 | Number(011,2) | Sim | Valor da Taxa do Banco |
| ValBa4 | Number(011,2) | Sim | Valor da Taxa do Banco |
| ValBa5 | Number(011,2) | Sim | Valor da Taxa do Banco |
| ValEm1 | Number(011,2) | Sim | Valor da Taxa da Empresa |
| ValEm2 | Number(011,2) | Sim | Valor da Taxa da Empresa |
| OriPar | String(001) | Sim | Origem da Parcela |
| CodCal | Number(005,0) | Sim | Código do Cálculo |
| CodOco | String(005) | Sim | Código - Ocorrências |
| DatVct | Date | Sim | Data do Vencimento da Parcela |
| TipEmc | String(001) | Sim | Tipo de Pagamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBan
- DatEmp
- SeqEmp
- NumPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
