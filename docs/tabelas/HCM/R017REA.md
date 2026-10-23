# R017REA

## Descrição

Reestruturação dos Postos de trabalho - Atuação dos colaboradores

---

## Resumo

- Campos: 29
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRee | Number(004,0) | Não | Código da reestruturação dos Postos de trabalho |
| NumEmp | Number(004,0) | Não | Empresa do Colaborador |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador envolvido na reestruturação |
| CodTap | Number(003,0) | Sim | Indica a atuação que o Colaborador exercerá no Posto |
| PosTra | String(024) | Sim | Determina o posto que o colaborador assumirá na reestruturação |
| SeqReg | Number(009,0) | Sim | Determina o posto que o colaborador assumirá na reestruturação |
| MotAlt | Number(003,0) | Sim | Motivo de alteração do Posto de Trabalho |
| ObsHpo | String(700) | Sim | Observação do histórico de posto de trabalho |
| TipAdm | Number(002,0) | Sim | Indica o Tipo de Admissão, quando houver troca de filial |
| ConTov | String(001) | Sim | Indica se existe Turn-Over na Entrada quando há troca de Local na reestruturação |
| ConTos | String(001) | Sim | Indica se existe Turn-Over na Saída quando há troca de Local na reestruturação |
| LocTra | Number(007,0) | Sim | Indica o município do Local de Trabalho RAIS, quando há troca de Local |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CarVag | String(024) | Sim | Indica o cargo para ocupação da vaga, quando houver troca de cargo |
| CodCrr | Number(003,0) | Sim | Código da Carreira |
| ConFin | Number(007,0) | Sim | Conta Financeira |
| CodEsc | Number(009,0) | Sim | Indica a Escala que o colaborador assumirá no posto |
| CodTma | Number(001,0) | Sim | Indica a Turma da Escala que o colaborador assumirá no posto |
| TurInt | Number(009,0) | Sim | Indica a Turma de intervalo que o colaborador assumirá no posto |
| HorBas | Number(004,0) | Sim | Horário Base (Segunda a Sexta-Feira) |
| HorSab | Number(004,0) | Sim | Horário de Sábado |
| HorSem | Number(010,0) | Sim | Horas Semanais |
| HorDsr | Number(010,0) | Sim | Horas de DSR |
| CodEqp | Number(004,0) | Sim | Indica a Equipe que o colaborador assumirá no posto |
| CodCat | Number(003,0) | Sim | Indica a Categoria que o colaborador assumirá no posto |
| CodVin | Number(002,0) | Sim | Indica o Vínculo que o colaborador assumirá no posto |
| CamRes | String(700) | Sim | Campo reserva |
| NatDes | Number(003,0) | Sim | Indica a Natureza da Despesa que o colaborador assumirá no posto |

---

## Chave Primária

- CodRee
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017REA_000

**Tabela:** R017REE

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |

### IR_R017REA_004

**Tabela:** R017TAP

| Origem | Destino |
|--------|---------|
| CodTap | CodTap |

### IR_R017REA_006

**Tabela:** R017REP

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |
| SeqReg | SeqReg |

### IR_R017REA_007

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| MotAlt | CodMot |

