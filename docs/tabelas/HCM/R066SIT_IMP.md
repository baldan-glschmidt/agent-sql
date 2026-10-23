# R066SIT_IMP

## Descrição

Situações Apuração Colaborador - Importação Eventos Sistema Legado

---

## Resumo

- Campos: 11
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
| DatApu | Date | Não | Data da Apuração |
| CodSit | Number(003,0) | Não | Código da Situação Apurada |
| CodRat | Number(009,0) | Não | Código de Rateio da Situação |
| QtdHor | Number(010,0) | Sim | Qtde de Horas Apuradas p/ a Situação |
| MotSit | Number(003,0) | Sim | Motivo da Situação |
| CodUsu | Number(010,0) | Sim | Código do Usuário do Último Acerto na Situação |
| QtdHNC | Number(010,0) | Sim | Qtde. Horas Situação s/Conversão de Noturnas |
| Obs | String(050) | Sim | Observação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu
- CodSit
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
