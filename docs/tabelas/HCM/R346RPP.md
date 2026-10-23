# R346RPP

## Descrição

eSocial JR - Processo Trabalhista - Informações da remuneração e periodicidade de pagamento

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| DatRem | Date | Não | Data a partir da qual as informações de remuneração e periodicidade de pagamento estão vigentes |
| ValSal | Number(015,2) | Sim | Salário base do trabalhador, correspondente à parte fixa da remuneração |
| UndSal | Number(001,0) | Sim | Unidade de pagamento da parte fixa da remuneração |
| DscSal | String(255) | Sim | Descrição do salário por tarefa ou variável e como este é calculado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- DatRem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
