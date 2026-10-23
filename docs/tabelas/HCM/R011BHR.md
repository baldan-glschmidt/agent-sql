# R011BHR

## Descrição

Banco de Horas

---

## Resumo

- Campos: 17
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBHr | Number(005,0) | Não | Código do Banco de Horas |
| DesBHr | String(030) | Sim | Descrição do Banco de Horas |
| DiaCre | Number(005,0) | Sim | Máximo Diário de Crédito em Dias de Trabalho |
| SemCre | Number(010,0) | Sim | Máximo de Crédito Semanal do Banco |
| MesCre | Number(010,0) | Sim | Máximo de Crédito Mensal do Banco |
| SalCre | Number(010,0) | Sim | Máximo de Saldo de Crédito para o Colaborador |
| DiaDeb | Number(005,0) | Sim | Máximo de Débito Diário do Banco |
| SemDeb | Number(010,0) | Sim | Máximo de Débito Semanal do Banco |
| MesDeb | Number(010,0) | Sim | Máximo de Débito Mensal do Banco |
| SalDeb | Number(010,0) | Sim | Máximo de Saldo de Débito do Colaborador |
| SepFec | String(001) | Sim | Separar Fechamentos em Períodos |
| PrrAfa | String(001) | Sim | Prorrogar Banco de Horas nos Afastamentos |
| DiaCrF | Number(005,0) | Sim | Máximo Diário de Crédito em Dias de Folga |
| DiaTCr | Number(005,0) | Sim | Máximo Diário de Trabalho + Crédito |
| PerCre | Number(010,0) | Sim | Máximo de Crédito no Período |
| PerDeb | Number(010,0) | Sim | Máximo de Débito no Período |
| ConPme | String(001) | Sim | Considerar primeiro fechamento na prorrogação |

---

## Chave Primária

- CodBHr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
