# R348BIM

## Descrição

eSocial - Conferência INSS - Base Comercialização

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
| IndCom | Number(001,0) | Não | Indicativo de Comercialização |
| CodRat | Number(009,0) | Não | Código do Rateio |
| FilEst | Number(006,0) | Sim | Código da filial do estabelecimento |
| ValBru | Number(014,2) | Sim | Valor Bruto |
| ConPre | Number(014,2) | Sim | Contribuição Previdenciária |
| CoPrSu | Number(014,2) | Sim | Contribuição Previdenciária Suspensa |
| PerRat | Number(005,2) | Sim | Percentual RAT |
| PeRaSu | Number(005,2) | Sim | Percentual RAT Suspenso |
| ConSen | Number(014,2) | Sim | Contribução SENAR |
| CoSeSu | Number(014,2) | Sim | Contribução SENAR Suspenso |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CodFil
- IndCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
