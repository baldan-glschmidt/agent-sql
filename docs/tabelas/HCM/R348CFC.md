# R348CFC

## Descrição

eSocial - Conferência FGTS - Colaborador

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
| NumEmp | Number(004,0) | Não | Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipIns | Number(001,0) | Sim | Tipo de inscrição da filial |
| CfjIns | String(014) | Sim | Número de inscrição da filial |
| CodLot | String(030) | Sim | Código atribuído para a lotação no eSocial |
| NomFun | String(080) | Sim | Nome do colaborador |
| NumCpf | Number(011,0) | Sim | Número do CPF do colaborador |
| MatEso | String(030) | Sim | Matrícula eSocial do colaborador |
| CatEso | Number(004,0) | Sim | Código da categoria eSocial do trabalhador |
| TipReg | Number(001,0) | Sim | Tipo de regime trabalhista |
| RemSuc | String(001) | Sim | Remuneração relativa a verbas devidas pela empresa sucessora |
| DatDem | Date | Sim | Data de demissão do colaborador |
| FgtRec | String(001) | Sim | FGTS deve ser recolhido na rescisão |
| MotDes | Number(002,0) | Sim | Código do motivo do desligamento eSocial |
| TerTsv | Number(002,0) | Sim | Motivo do término do trabalhador sem vínculo empregatício |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- PerApu
- IndApu
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
