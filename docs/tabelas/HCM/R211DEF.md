# R211DEF

## Descrição

Pesquisa - Definição

---

## Resumo

- Campos: 53
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPsq | Number(006,0) | Não | Código da Pesquisa |
| SeqPsq | Number(002,0) | Não | Sequência da pesquisa |
| DesDef | String(060) | Sim | Descrição da definição da pesquisa |
| DatIni | Date | Sim | Data inicial para responder a pesquisa |
| HorIni | Number(005,0) | Sim | Hora inicial para responder a pesquisa |
| DatTer | Date | Sim | Data limite para responder a pesquisa |
| HorTer | Number(005,0) | Sim | Hora limite para responder a pesquisa |
| SitPsq | String(001) | Sim | Situação da pesquisa |
| AltRes | String(001) | Sim | Define se o usuário pode alterar suas respostas dentro do prazo |
| EmpRes | Number(004,0) | Sim | Código da empresa do responsável pela pesquisa |
| TipRes | Number(001,0) | Sim | Tipo de colaborador responsável pela pesquisa |
| CadRes | Number(009,0) | Sim | Cadastro do responsável pela pesquisa |
| IdeEmp | Number(001,0) | Sim | Define se o participante deve identificar sua Empresa na pesquisa |
| IdeTip | Number(001,0) | Sim | Define se o participante deve identificar seu Tipo na pesquisa |
| IdeFil | Number(001,0) | Sim | Define se o participante deve identificar sua Filial na pesquisa |
| IdeLoc | Number(001,0) | Sim | Define se o participante deve identificar seu Local na pesquisa |
| TabOrg | Number(004,0) | Sim | Código da tabela de Organograma que deve ser considerada |
| NivLoc | Number(002,0) | Sim | Define o Nível do Local que será apresentado na identificação |
| IdeCar | Number(001,0) | Sim | Define se o participante deve identificar seu Cargo na pesquisa |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos que deve ser considerada |
| NivCar | Number(001,0) | Sim | Define o Nível do Cargo que será apresentado na identificação |
| IdeTur | Number(001,0) | Sim | Define se o participante deve identificar seu Turno na pesquisa |
| IdeCCu | Number(001,0) | Sim | Define se o participante deve identificar seu C. Custo na pesquisa |
| IdeHie | Number(001,0) | Sim | Define se o participante deve identificar sua Hierarquia na pesquisa |
| IdeSin | Number(001,0) | Sim | Define se o participante deve identificar seu Sindicato na pesquisa |
| IdeSex | Number(001,0) | Sim | Define se o participante deve identificar seu Sexo na pesquisa |
| IdeGin | Number(001,0) | Sim | Define se o participante deve identificar seu Grau de Instrução na pesquisa |
| IdeCla | Number(001,0) | Sim | Define se o participante deve identificar sua classificação na pesquisa |
| TabCla | Number(003,0) | Sim | Código da tabela de classificação dos participantes da pesquisa |
| AbrEmp | String(025) | Sim | Abrangência de Empresa |
| AbrTcl | String(025) | Sim | Abrangência de Tipo de Colaborador |
| AbrCad | String(100) | Sim | Abrangência de Colaboradores |
| AbrFil | String(025) | Sim | Abrangência de Filial |
| AbrLoc | String(1500) | Sim | Abrangência de Local |
| AbrCar | String(100) | Sim | Abrangência de Cargo |
| AbrTur | String(025) | Sim | Abrangência de Turno |
| AbrCCu | String(100) | Sim | Abrangência de Centro de custo |
| AbrHie | String(025) | Sim | Abrangência de Hierarquia |
| AbrSin | String(025) | Sim | Abrangência de Sindicato |
| AbrSex | String(025) | Sim | Abrangência de Sexo |
| NumEmp | Number(004,0) | Sim | Número da empresa do lote |
| CodLot | Number(004,0) | Sim | Código do Lote |
| RegFil | Number(003,0) | Sim | Regra de filtro para os Colaboradores |
| ResPsq | Number(001,0) | Sim | Define quem pode responder a pesquisa |
| ForApr | Number(001,0) | Sim | Forma de apresentação das perguntas na WEB |
| CodReg | Number(003,0) | Sim | Código da regra chamada ao gravar o questionário da pesquisa |
| PesVen | String(001) | Sim | Define se apresenta a pesquisa vencida como pendente |
| CabCpl | String(001) | Sim | Apresentar inf. complementares no cabeçalho do formulário único |
| InsCab | String(001) | Sim | Apresentar instruções de preenchimento no cabeçalho do formulário único |
| AceDem | String(001) | Sim | Aceitar participantes demitidos na formação da pesquisa |
| AbrSit | String(015) | Sim | Abrangência de Situação do afastamento |
| QtdPar | Number(005,0) | Sim | Quantidade de participantes da pesquisa |
| PerRea | Number(001,0) | Sim | Permite reabrir a pesquisa |

---

## Chave Primária

- CodPsq
- SeqPsq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R211DEF_000

**Tabela:** R211PSQ

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |

