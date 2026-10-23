# R049EMP

## Descrição

Empréstimo Consignado - Empréstimos

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
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
| SeqEmp | Number(002,0) | Não | Sequência do Empréstimo |
| DatEmp | Date | Não | Data do Empréstimo |
| ValEmp | Number(011,2) | Sim | Teto da parcela para concessão do empréstimo |
| QtdPar | Number(003,0) | Sim | Número de Parcelas |
| CmpIni | Date | Sim | Competência Início do Desconto |
| OriEmp | String(001) | Sim | Origem do registro de empréstimo |
| SitEmp | String(001) | Sim | Situação do Empréstimo |
| IdeCon | String(020) | Sim | Identificador do Contrato |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBan
- DatEmp
- SeqEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
