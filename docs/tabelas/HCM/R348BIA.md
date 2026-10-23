# R348BIA

## Descrição

eSocial - Conferência INSS - Base Avulsos

---

## Resumo

- Campos: 18
- Chave Primária: 6 campo(s)
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
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(015,0) | Não | Número de Inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de Inscrição do contribuinte |
| CodRat | Number(009,0) | Não | Código do Rateio |
| FilEst | Number(006,0) | Sim | Código da Filial do Estabelecimento |
| CodLot | String(030) | Não | Código atribuído pela empresa para a lotação |
| BasIns | Number(014,2) | Sim | Base INSS |
| B13Ins | Number(014,2) | Sim | Base INSS 13º salário |
| ValRet | Number(014,2) | Sim | Valor Retido |
| Sat15A | Number(014,2) | Sim | Base Contribuição SAT 15 Anos |
| Sat20A | Number(014,2) | Sim | Base Contribuição SAT 20 Anos |
| Sat25A | Number(014,2) | Sim | Base Contribuição SAT 25 Anos |
| BasFgt | Number(014,2) | Sim | Base FGTS |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CodFil
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
