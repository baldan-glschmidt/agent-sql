# R348BPC

## Descrição

eSocial - Conferência PIS - Base Colaborador

---

## Resumo

- Campos: 20
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| FilEst | Number(006,0) | Sim | Código da Filial do Estabelecimento |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(015,0) | Não | Número de Inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de Inscrição do contribuinte |
| CodLot | String(030) | Sim | Código atribuído pela empresa para a lotação |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| MatTra | String(030) | Sim | Matrícula do colaborador |
| NomTra | String(200) | Sim | Nome do trabalhador |
| CodCal | String(200) | Sim | Códigos de Calculo |
| BasPis | Number(014,2) | Sim | Base de cálculo da contribuição social devida ao PIS/PASEP |
| BaPiSu | Number(014,2) | Sim | Base Pis Suspenso |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CodFil
- CodRat
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
