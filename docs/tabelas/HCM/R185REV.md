# R185REV

## Descrição

Orçamento Individual - Definições da Revisão

---

## Resumo

- Campos: 35
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| VerOrc | Number(004,0) | Não | Versão do orçamento |
| RevOrc | Number(004,0) | Não | Revisão  da versão do orçamento |
| DesRed | String(030) | Sim | Descrição reduzida da revisão do orçamento |
| DesDet | String(500) | Sim | Descrição detalhada da revisão do orçamento |
| CmpIni | Date | Sim | Competência de início do cálculo |
| CmpBas | Date | Sim | Competência base do cálculo |
| SalAdm | Number(002,0) | Sim | Salário dos Admitidos |
| SalDem | Number(002,0) | Sim | Salários dos Demitidos |
| NivAdm | String(005) | Sim | Nível Salarial para Admissão |
| NivDem | String(005) | Sim | Nível Salarial para Demissão |
| PerAdm | Number(005,2) | Sim | % Salário Admissão |
| PerDem | Number(005,2) | Sim | % Salário Demissão |
| IndSin | String(001) | Sim | Respeita definições do 13° Salário do sindicato |
| Mes13s | Number(002,0) | Sim | Mês do adiantamento do 13° salário |
| Per13s | Number(005,2) | Sim | Percentual  do adiantamento do 13° salário |
| Adm13s | String(001) | Sim | Adm.no Ano - Projetar Adto 13° Salário Até Dezembro (S,N) |
| Mes13t | Number(002,0) | Sim | Mês do 13° salário |
| ConFer | Number(001,0) | Sim | Considera programação de férias |
| ConPrs | Number(001,0) | Sim | Considera propostas salariais |
| ConRat | String(001) | Sim | Considera Rateio |
| DefAdc | Number(001,0) | Sim | Comportamento na identificação de histórico de adicionais(insalubridade/periculosidade) |
| ConAbo | Number(001,0) | Sim | Considera Abono Férias |
| SitOrc | Number(001,0) | Sim | Situação do cálculo do orçamento(Simulado/Oficial) |
| CodCen | Number(004,0) | Sim | Código do cenário |
| CmpFim | Date | Sim | Competência final do cálculo |
| AdiFer | Number(004,2) | Sim | Percentual Acres.(1/3) Férias |
| RegCol | Number(003,0) | Sim | Regra para ser executada antes de calcular o colaborador |
| RegMes | Number(003,0) | Sim | Regra p/ ser executada antes de calcular cada mês do colaborador |
| RegAdm | Number(003,0) | Sim | Regra p/ calcular o salário de admitidos |
| RegDem | Number(003,0) | Sim | Regra p/ calcular o salário de demitidos |
| RevBlo | Number(001,0) | Sim | Define o bloqueio da revisão |
| BasIns | String(001) | Sim | Define a base de cálculo de adicional de insalubridade |
| CalSim | String(001) | Sim | Define se deve permitir cálculo simultâneo. |

---

## Chave Primária

- NumEmp
- AnoBas
- VerOrc
- RevOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185REV_002

**Tabela:** R185VER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |
| VerOrc | VerOrc |

