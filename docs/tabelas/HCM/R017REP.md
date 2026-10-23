# R017REP

## Descrição

Reestruturação dos Postos de trabalho - Postos

---

## Resumo

- Campos: 41
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRee | Number(004,0) | Não | Código da reestruturação dos Postos de trabalho |
| SeqReg | Number(009,0) | Não | Sequencia do posto |
| AcaPos | Number(001,0) | Sim | Indica a ação que deve ser realizada com o posto |
| PosNov | String(001) | Sim | Indica se o posto em questão é um posto novo |
| PosTra | String(024) | Sim | Indica qual será o código do posto a ser criado |
| DesRed | String(070) | Sim | Determina a descrição reduzida do Posto de Trabalho que será criado |
| DesPos | String(150) | Sim | Determina a descrição do Posto de Trabalho que será criado |
| DatCri | Date | Sim | Determina a data de criação do Posto de Trabalho que será criado |
| DatExt | Date | Sim | Determina a data de extinção do Posto de Trabalho que será criado |
| PerPos | Number(002,0) | Sim | Determina o perfil do Posto de Trabalho que será criado |
| ObsPos | String(2000) | Sim | Determina a observação do Posto de Trabalho que será criado |
| NumEmp | Number(004,0) | Sim | Determina a empresa do Posto de Trabalho que será criado |
| CodFil | Number(006,0) | Sim | Determina a filial do Posto de Trabalho que será criado |
| TabOrg | Number(004,0) | Sim | Determina o Organograma do Posto de Trabalho que será criado |
| NumLoc | Number(009,0) | Sim | Determina o Local do Posto de Trabalho que será criado |
| CodCcu | String(018) | Sim | Determina o Centro de custo do Posto de Trabalho que será criado |
| VarCar | String(001) | Sim | Define se o Posto de trabalho criado permitirá atuação em vários cargos |
| EstCar | Number(004,0) | Sim | Determina a Est. de cargos do Posto de Trabalho que será criado |
| CodCar | String(024) | Sim | Determina o Cargo do Posto de Trabalho que será criado |
| CodSin | Number(004,0) | Sim | Código do Sindicato |
| CodHie | Number(003,0) | Sim | Determina a hierarquia do Posto de Trabalho que será criado |
| TipCol | Number(001,0) | Sim | Determina para qual Tipo de colaborador o Posto de Trabalho será criado |
| TurPos | Number(001,0) | Sim | Determina o Turno do Posto de Trabalho que será criado |
| CodVin | Number(002,0) | Sim | Determina o Vínculo do Posto de Trabalho que será criado |
| TipVag | Number(002,0) | Sim | Determina o tipo da vaga do Posto de Trabalho que será criado |
| TipCon | Number(002,0) | Sim | Determina o tipo de contrato do Posto de Trabalho que será criado |
| PerPNE | Number(001,0) | Sim | Define se o posto permite ou não Pessoas com Deficiência |
| SitPos | Number(001,0) | Sim | Indica se o posto foi processado ou não |
| CamRes | String(700) | Sim | Campo reserva |
| CodEsc | Number(009,0) | Sim | Determina a Escala do Posto de Trabalho que será criado |
| CodTma | Number(001,0) | Sim | Determina a Turma do Posto de Trabalho que será criado |
| TurInt | Number(009,0) | Sim | Determina a Turma Intervalo do Posto de Trabalho que será criado |
| CodEqp | Number(004,0) | Sim | Determina a Equipe do Posto de Trabalho que será criado |
| CodCat | Number(003,0) | Sim | Determina a Categoria do Posto de Trabalho que será criado |
| HorBas | Number(004,0) | Sim | Determina o Horário Base do Posto de Trabalho que será criado |
| HorSab | Number(004,0) | Sim | Determina o Horário de Sábado do Posto de Trabalho que será criado |
| HorSem | Number(010,0) | Sim | Determina as Horas Semanais do Posto de Trabalho que será criado |
| HorDsr | Number(010,0) | Sim | Determina as Horas de DSR do Posto de Trabalho que será criado |
| NatDes | Number(003,0) | Sim | Determina a Natureza da Despesa do Posto de Trabalho que será criado |
| CodTom | Number(008,0) | Sim | Determina o tomador do Posto de trabalho que será criado |
| CodRat | Number(009,0) | Sim | Determina o rateio do Posto de trabalho que será criado |

---

## Chave Primária

- CodRee
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017REP_000

**Tabela:** R017REE

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |

### IR_R017REP_009

**Tabela:** R017PER

| Origem | Destino |
|--------|---------|
| PerPos | PerPos |

