# R348RRA

## Descrição

eSocial - Conferência IRRF - Informações RRA

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| DatPag | Date | Não | Data de pagamento |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipOri | Number(002,0) | Não | Tipo de origem do pagamento do IRRF |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| TipPro | Number(001,0) | Sim | Tipo processo - RRA |
| ProRra | String(021) | Sim | Número do processo - RRA |
| DesRra | String(050) | Sim | Descrição dos rendimentos recebidos acumuladamente - RRA |
| QmeRra | Number(004,0) | Sim | Número de meses relativo aos rendimentos recebidos acumuladamente - RRA |
| ValCus | Number(014,2) | Sim | Valor das despesas com custas judiciais |
| ValAdv | Number(014,2) | Sim | Valor total das despesas com advogado(s) |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- DatPag
- TipCol
- NumCad
- TipOri
- CodCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
