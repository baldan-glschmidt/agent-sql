# R017REE

## Descrição

Reestruturação dos Postos de trabalho

---

## Resumo

- Campos: 39
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRee | Number(004,0) | Não | Código da reestruturação dos Postos de trabalho |
| DesRee | String(060) | Sim | Descrição da reestruturação |
| EstNov | String(001) | Sim | Indica se a reestruturação é para uma estrutura nova ou não |
| EstPos | Number(003,0) | Sim | Estrutura de Postos de trabalho a ser reestruturada |
| AbrEmp | String(200) | Sim | Determina quais empresas terão a nova estrutura aplicada |
| DatRee | Date | Sim | Indica qual será a data da reestruturação |
| CodTap | Number(003,0) | Sim | Define o Tipo de atuação padrão para gerar os históricos dos colaboradores |
| MotAlt | Number(003,0) | Sim | Define o Motivo de alteração padrão para gerar os históricos dos colaboradores |
| SitRee | Number(001,0) | Sim | Situação da reestruturação |
| ObsRee | String(4000) | Sim | Observações da reestruturação |
| CodUsu | Number(009,0) | Sim | Usuário responsável pela última alteração na reestruturação |
| DthAlt | Number(014,6) | Sim | Data/Hora da última alteração na reestruturação |
| ComCod | String(100) | Sim | Determina como será composto o código do posto de trabalho |
| ComDes | String(150) | Sim | Determina como será composta a descrição do posto de trabalho |
| ComRed | String(150) | Sim | Determina como será composta a desc. reduzida do posto de trabalho |
| PerPos | Number(002,0) | Sim | Indica qual será o perfil dos postos que serão criados |
| ConEmp | String(001) | Sim | Indica que a empresa é um critério para a criação dos postos |
| ConFil | String(001) | Sim | Indica que a filial é um critério para a criação dos postos |
| ConLoc | String(001) | Sim | Indica que o Local é um critério para a criação dos postos |
| NivLoc | Number(002,0) | Sim | Indica qual nível do local será considerado para a criação dos postos |
| ConCcu | String(001) | Sim | Indica que o C. Custo é um critério para a criação dos postos |
| ConCar | String(001) | Sim | Indica que o Cargo é um critério para a criação dos postos |
| ConSin | String(001) | Sim | Indica que o Sindicato é um critério para a criação dos postos |
| NivCar | Number(002,0) | Sim | Indica qual nível do cargo será considerado para a criação dos postos |
| ConHie | String(001) | Sim | Indica que a hierarquia é um critério para a criação dos postos |
| ConTcl | String(001) | Sim | Indica que o tipo do colaborador é um critério para a criação dos postos |
| ConTur | String(001) | Sim | Indica que o turno é um critério para a criação dos postos |
| ConVin | String(001) | Sim | Indica que o vínculo é um critério para a criação dos postos |
| ConTVa | String(001) | Sim | Indica que o Tipo de vaga é um critério para a criação dos postos |
| ConTco | String(001) | Sim | Indica que o tipo de contrato é um critério para a criação dos postos |
| RegPro | Number(003,0) | Sim | Indica regra que permite customizar a criação dos postos |
| CriCar | String(001) | Sim | Indica se as características dos postos devem ser criadas ou não |
| VinCol | String(001) | Sim | Indica se os postos deverão ser criados com os colaboradores vinculados |
| CamRes | String(700) | Sim | Campo reserva |
| ConEsc | String(001) | Sim | Indica que a Escala é um critério para a criação dos postos |
| ConNat | String(001) | Sim | Indica que a Natureza de Despesa é um critério para a criação dos postos |
| ConCad | String(001) | Sim | Indica que o cadastro do colaborador é um critério para a criação dos postos |
| ConHor | String(001) | Sim | Indica que o Horário é um critério para a criação dos postos |
| CodReg | Number(003,0) | Sim | Regra para composição do código e/ou descrição do posto na reestruturação |

---

## Chave Primária

- CodRee

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017REE_003

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R017REE_006

**Tabela:** R017TAP

| Origem | Destino |
|--------|---------|
| CodTap | CodTap |

### IR_R017REE_007

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| MotAlt | CodMot |

