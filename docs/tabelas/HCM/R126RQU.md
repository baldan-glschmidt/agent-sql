# R126RQU

## Descrição

Requisições - Definição

---

## Resumo

- Campos: 68
- Chave Primária: 1 campo(s)
- Índices: 5
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código Requisição |
| NumEmp | Number(004,0) | Sim | Empresa Requisitante |
| CodFil | Number(006,0) | Sim | Código da Filial |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Cargo Requisitado |
| CodTim | String(008) | Sim | Código do Time |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Sim | Local Requisitado |
| DatRqu | Date | Sim | Data da Requisição |
| TipRqu | Number(003,0) | Sim | Tipo Requisição |
| QtdRqu | Number(004,0) | Sim | Quantidade de Vagas da Requisição |
| TurRqu | Number(001,0) | Sim | Turno Requisição |
| DatLim | Date | Sim | Data Limite |
| DatPre | Date | Sim | Data Previsão |
| AnoRqu | String(1000) | Sim | Anotações na Requisição |
| CodOem | Number(008,0) | Sim | Código do Cliente |
| EmpSol | Number(004,0) | Sim | Empresa do Colabolador Solicitante |
| TipCol | Number(001,0) | Sim | Tipo do Colabolador Solicitante |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Solicitante |
| HorIni | Number(005,0) | Sim | Hora Início Disponibilidade para Entrevista |
| HorFim | Number(005,0) | Sim | Hora Fim Disponibilidade para Entrevista |
| DatIni | Date | Sim | Data Início para Triagem |
| DatFim | Date | Sim | Data Fim para Triagem |
| CodUsu | Number(010,0) | Sim | Código do Usuário da Aprovação Requisição |
| DatApr | Date | Sim | Data da Aprovação da Requisição |
| CodCcu | String(018) | Sim | Código do Centro de Custo |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| CodMot | Number(003,0) | Sim | Motivo do Salário |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| ValSal | Number(013,4) | Sim | Valor do Salário Efetivo |
| SitRqu | Number(001,0) | Sim | Situação da Requisição |
| DatEnc | Date | Sim | Data de Encerramento |
| CodMoc | Number(003,0) | Sim | Código do Motivo do Cancelamento |
| CodRes | Number(010,0) | Sim | Código do Usuário Responsável pelo Atendimento da Requisição |
| AnoCon | Number(004,0) | Sim | Ano Concurso |
| NumCon | Number(006,0) | Sim | Número do Concurso |
| TriSel | String(001) | Sim | Identifica p/as regras se o processo é de triagem ou seletiva |
| ConCan | String(001) | Sim | Define quais Candidatos devem ser considerados |
| DvgWEB | String(001) | Sim | Define se a Requisição deve ser divulgada na WEB |
| TipVag | Number(002,0) | Sim | Código do tipo de vaga |
| ReqEla | String(011) | Sim | Identificação da requisição (vaga) para a Elancers |
| DivEmp | String(001) | Sim | Indica para a Elancers se pode divulgar o nome da empresa da vaga |
| CodCid | Number(007,0) | Sim | Cidade para Trabalhar |
| UsuEla | String(020) | Sim | Usuário responsável pela requisição (vaga) na Elancers |
| CarVag | String(024) | Sim | Código do novo cargo para ocupação da vaga |
| OriRqu | Number(001,0) | Sim | Define de qual cargo deve considerar os requisitos |
| DatSus | Date | Sim | Data de Suspensão |
| MotSus | Number(003,0) | Sim | Código do Motivo da Suspensão da Requisição |
| CodTap | Number(003,0) | Sim | Tipo de atuação do Colaborador no Posto de trabalho |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Posto de Trabalho em que o Colaborador atua |
| HisEli | String(001) | Sim | Mantém histórico de eliminação dos candidatos com interesse na vaga |
| PtsMin | Number(005,0) | Sim | Pontuação mínima que o candidato deve obter |
| UsuRqu | Number(010,0) | Sim | Código do usuário que cadastrou a requisição |
| CodVag | String(010) | Sim | Código da vaga usado na publicação do anúncio |
| IdeExt | String(015) | Sim | Identificador Externo |
| USU_PreTri | Date | Sim | Data Previsão Triagem |
| USU_DatTri | Date | Sim | Data Conclusão Triagem |
| USU_TraInt | String(001) | Sim | Houve Transferência Interna? |
| USU_NomTra | String(030) | Sim | Nome do Transferido |
| USU_DesCar | String(9999) | Sim | Resumo do Cargo |
| USU_CurFor | String(9999) | Sim | Formação |
| USU_IntRqu | String(030) | Sim | Dados da Integração da Vaga |
| USU_IdGupy | Number(010,0) | Sim | ID da Vaga na Gupy |
| USU_SitRqu | String(001) | Sim | Situação Requisição (Integração Gupy) |

---

## Chave Primária

- CodRqu

---

## Índices

### R126RQUIndice2

**Tipo:** Não unico

Campos:
- SitRqu

### R126RQUIndice3

**Tipo:** Não unico

Campos:
- CodRes

### R126RQUIndice4

**Tipo:** Não unico

Campos:
- CodRqu
- SitRqu

### R126RQUIndice5

**Tipo:** Não unico

Campos:
- CodRqu
- CodRes

### R126RQUIndice6

**Tipo:** Não unico

Campos:
- CodRqu
- SitRqu
- CodRes

---

## Relacionamentos

### IR_R126RQU_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R126RQU_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R126RQU_007

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R126RQU_009

**Tabela:** R114RRQ

| Origem | Destino |
|--------|---------|
| TipRqu | CodRrq |

### IR_R126RQU_047

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CarVag | CodCar |

