# R092PRO

## Descrição

Proposta de quadro de vagas p/ posto

---

## Resumo

- Campos: 47
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| CodPlv | Number(004,0) | Não | Código do Plano de Vagas |
| SeqPro | Number(009,0) | Não | Sequência da proposta de alteração do quadro de vagas por posto |
| IniPro | Date | Sim | Define a data de início da alteração proposta para o quadro |
| TerPro | Date | Sim | Define a data de término da proposta de alteração do quadro |
| TipPaq | Number(001,0) | Sim | Define o tipo de proposta de alteração do quadro |
| PosTra | String(024) | Sim | Código do posto de trabalho envolvido na proposta de alteração do quadro |
| DesRed | String(070) | Sim | Descrição reduzida do posto de trabalho que está sendo proposto |
| DesPos | String(150) | Sim | Descrição do posto de trabalho que está sendo proposto |
| ObsPos | String(2000) | Sim | Observação sobre o posto de trabalho que está sendo proposto |
| QtdPro | Number(004,0) | Sim | Quantidade de vagas proposta |
| ObsPql | String(250) | Sim | Observação sobre a proposta |
| SitPqv | Number(001,0) | Sim | Situação da proposta |
| NumEmp | Number(004,0) | Sim | Define a Empresa do posto de trabalho que está sendo proposto |
| CodFil | Number(006,0) | Sim | Define a Filial do posto de trabalho que está sendo proposto |
| TabOrg | Number(004,0) | Sim | Define o organograma do posto de trabalho que está sendo proposto |
| NumLoc | Number(009,0) | Sim | Define o local do posto de trabalho que está sendo proposto |
| CodCcu | String(018) | Sim | Define o centro de custo do posto de trabalho que está sendo proposto |
| EstCar | Number(004,0) | Sim | Define a estrutura de cargos do posto de trabalho que está sendo proposto |
| CodCar | String(024) | Sim | Define o cargo do posto de trabalho que está sendo proposto |
| CodSin | Number(004,0) | Sim | Define o sindicato do posto de trabalho que está sendo proposto |
| CodHie | Number(003,0) | Sim | Define o nível de hierarquia do posto de trabalho que está sendo proposto |
| TipCol | Number(001,0) | Sim | Define o tipo de colaborador que pode atuar no posto que está sendo proposto |
| TurPos | Number(001,0) | Sim | Define o turno do posto de trabalho que está sendo proposto |
| CodVin | Number(002,0) | Sim | Define o vínculo do posto de trabalho que está sendo proposto |
| TipVag | Number(002,0) | Sim | Define o tipo de vaga do posto de trabalho que está sendo proposto |
| TipCon | Number(002,0) | Sim | Define o tipo de contrato do posto de trabalho que está sendo proposto |
| PerPNE | Number(001,0) | Sim | Define se o posto permite ou não Pessoas com Deficiência |
| PosPai | String(024) | Sim | Indica o posto-pai do posto que está sendo proposto nas hierarquias de postos |
| DthPro | Number(014,6) | Sim | Data/Hora de criação da proposta |
| UsuPro | Number(009,0) | Sim | Usuário que criou a proposta |
| UsuRes | Number(009,0) | Sim | Usuário responsável pela proposta |
| DthEfe | Number(014,6) | Sim | Data/Hora de efetivação da proposta (atualização quadro/criação do posto) |
| CodEsc | Number(009,0) | Sim | Define a Escala do posto de trabalho que está sendo proposto |
| CodTma | Number(001,0) | Sim | Define a Turma do posto de trabalho que está sendo proposto |
| TurInt | Number(009,0) | Sim | Define a Turma Intervalo do posto de trabalho que está sendo proposto |
| CodEqp | Number(004,0) | Sim | Define a Equipe do posto de trabalho que está sendo proposto |
| CodCat | Number(003,0) | Sim | Define a Categoria do posto de trabalho que está sendo proposto |
| HorBas | Number(004,0) | Sim | Define o Horário Base do posto de trabalho que está sendo proposto |
| HorSab | Number(004,0) | Sim | Define o Horário de Sábado do posto de trabalho que está sendo proposto |
| HorSem | Number(010,0) | Sim | Define as Horas Semanais do posto de trabalho que está sendo proposto |
| HorDsr | Number(010,0) | Sim | Define as Horas de DSR do posto de trabalho que está sendo proposto |
| NatDes | Number(003,0) | Sim | Define a Natureza da Despesa do posto de trabalho que está sendo proposto |
| CodPrj | Number(008,0) | Sim | Código do Projeto |
| CodFas | Number(004,0) | Sim | Código da Fase do Projeto |
| CodOem | Number(008,0) | Sim | Define o Tomador do Posto de Trabalho |
| CodRat | Number(009,0) | Sim | Código de Rateio do C.Custo |

---

## Chave Primária

- EstPos
- CodPlv
- SeqPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R092PRO_001

**Tabela:** R017PLV

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodPlv | CodPlv |

