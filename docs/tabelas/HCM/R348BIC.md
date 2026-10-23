# R348BIC

## Descrição

eSocial - Conferência INSS - Base Colaborador

---

## Resumo

- Campos: 32
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
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(015,0) | Não | Número de Inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de Inscrição do contribuinte |
| CodRat | Number(009,0) | Não | Código do Rateio |
| FilEst | Number(006,0) | Não | Código da Filial do Estabelecimento |
| CodLot | String(030) | Sim | Código atribuído pela empresa para a lotação |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| MatTra | String(030) | Sim | Matrícula do colaborador |
| RegPre | Number(002,0) | Sim | Regime Previdenciário |
| NomTra | String(200) | Sim | Nome do trabalhador |
| BasBea | Number(014,2) | Sim | Base Verde/Amarelo |
| BasIns | Number(014,2) | Sim | Base INSS |
| BaInSu | Number(014,2) | Sim | Base INSS Suspenso |
| BasCon | Number(014,2) | Sim | Base do INSS - Empresa concomitante |
| BasOne | Number(016,4) | Sim | Base do INSS - Onerada |
| BasDes | Number(016,4) | Sim | Base do INSS - Desonerada |
| BasN13 | Number(014,2) | Sim | Base do INSS - 13º salário - Lei 14.973/2024 |
| ValRet | Number(014,2) | Sim | Valor Retido |
| SalFam | Number(014,2) | Sim | Salário Família |
| SalMat | Number(014,2) | Sim | Salário Maternidade |
| ValSes | Number(014,2) | Sim | Valor SEST |
| ValSen | Number(014,2) | Sim | Valor SENAT |
| GraExp | Number(001,0) | Sim | Grau de Exposição  Agentes Nocivos |
| CodCal | String(200) | Sim | Códigos de Calculo |

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
