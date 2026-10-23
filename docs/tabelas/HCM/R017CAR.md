# R017CAR

## Descrição

Postos de Trabalho - Características

---

## Resumo

- Campos: 34
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatIni | Date | Não | Define o início da validade das Características do posto |
| NumEmp | Number(004,0) | Sim | Define a Empresa do Posto de Trabalho |
| CodFil | Number(006,0) | Sim | Define a Filial do Posto de Trabalho |
| TabOrg | Number(004,0) | Sim | Define o Organograma dos Locais do Posto de Trabalho |
| NumLoc | Number(009,0) | Sim | Define o Local do Posto de Trabalho |
| CodCcu | String(018) | Sim | Define o Centro de custo do Posto de Trabalho |
| VarCar | String(001) | Sim | Define se o Posto de trabalho permitirá atuação em vários cargos |
| EstCar | Number(004,0) | Sim | Define a Estrutura de Cargos do Posto de Trabalho |
| CodCar | String(024) | Sim | Define o Cargo do Posto de Trabalho |
| CodSin | Number(004,0) | Sim | Código do Sindicato |
| CodHie | Number(003,0) | Sim | Define o Nível de hierarquia do Posto de trabalho |
| TipCol | Number(001,0) | Sim | Define os Tipos de Colaborador que podem atuar neste Posto de Trabalho |
| TurPos | Number(001,0) | Sim | Define o Turno do Posto de Trabalho |
| CodVin | Number(002,0) | Sim | Define o código do vínculo do Posto de Trabalho |
| TipVag | Number(002,0) | Sim | Define o tipo de vaga do Posto de Trabalho |
| TipCon | Number(002,0) | Sim | Define o tipo de contrato do Posto de Trabalho |
| PerPNE | Number(001,0) | Sim | Define se o posto permite ou não Pessoas com Deficiência |
| DatFim | Date | Sim | Final da validade das características do Posto de Trabalho |
| CodEsc | Number(009,0) | Sim | Define a Escala do Posto de Trabalho |
| CodTma | Number(001,0) | Sim | Define a Turma do Posto de Trabalho |
| TurInt | Number(009,0) | Sim | Define a Turma Intervalo do Posto de Trabalho |
| CodEqp | Number(004,0) | Sim | Define a Equipe do Posto de Trabalho |
| CodCat | Number(003,0) | Sim | Define a Categoria do Posto de Trabalho |
| HorBas | Number(004,0) | Sim | Define o Horário Base do Posto de Trabalho |
| HorSab | Number(004,0) | Sim | Define o Horário de Sábado do Posto de Trabalho |
| HorSem | Number(010,0) | Sim | Define as Horas Semanais do Posto de Trabalho |
| HorDsr | Number(010,0) | Sim | Define as Horas de DSR do Posto de Trabalho |
| NatDes | Number(003,0) | Sim | Define a Natureza da Despesa do Posto de Trabalho |
| CodPrj | Number(008,0) | Sim | Código do Projeto |
| CodFas | Number(004,0) | Sim | Código da Fase do Projeto |
| CodOem | Number(008,0) | Sim | Define o Tomador do Posto de Trabalho |
| CodRat | Number(009,0) | Sim | Código de Rateio do C.Custo |

---

## Chave Primária

- EstPos
- PosTra
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017CAR_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

