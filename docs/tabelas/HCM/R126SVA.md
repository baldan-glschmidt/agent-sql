# R126SVA

## Descrição

Solicitação de abertura de vaga

---

## Resumo

- Campos: 32
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSVa | Number(009,0) | Não | Código da solicitação de vaga |
| DesSVa | String(200) | Sim | Descrição da solicitação de vaga |
| TipSVa | Number(003,0) | Sim | Tipo de Solicitação |
| DatSVa | Date | Sim | Data base da solicitação de abertura de vaga |
| NumEmp | Number(004,0) | Sim | Empresa Requisitante |
| CodTap | Number(003,0) | Sim | Tipo de atuação do Colaborador no Posto de trabalho |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Posto de Trabalho em que o Colaborador atua |
| CodFil | Number(006,0) | Sim | Código da Filial |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Cargo Requisitado |
| CarVag | String(024) | Sim | Código do novo cargo para ocupação da vaga |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Sim | Local Requisitado |
| CodCcu | String(018) | Sim | Código do Centro de Custo |
| TurRqu | Number(001,0) | Sim | Turno Requisitado |
| TipVag | Number(002,0) | Sim | Código do tipo de vaga |
| QtdVag | Number(004,0) | Sim | Quantidade de vagas da solicitação |
| ObsSVa | String(5000) | Sim | Observações da Solicitação de abertura de vaga |
| SitSVa | Number(001,0) | Sim | Situação da Solicitação de abertura de vaga |
| DthSVa | Number(014,6) | Sim | Data/Hora de criação da Solicitação de abertura de vaga |
| UsuSVa | Number(009,0) | Sim | Usuário que criou a Solicitação de abertura de vaga |
| UsuRes | Number(009,0) | Sim | Código do usuário responsável no momento pela solicitação de vaga |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| CodMot | Number(003,0) | Sim | Motivo do Salário |
| ValSal | Number(013,4) | Sim | Valor do Salário Efetivo |
| DthRqu | Number(014,6) | Sim | Data/Hora de efetivação da solicitação (criação da Requisição) |
| CodRqu | Number(009,0) | Sim | Código da Requisição criada a partir desta solicitação |

---

## Chave Primária

- CodSVa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126SVA_002

**Tabela:** R114RRQ

| Origem | Destino |
|--------|---------|
| TipSVa | CodRrq |

### IR_R126SVA_010

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R126SVA_013

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

