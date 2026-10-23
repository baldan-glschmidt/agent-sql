# R084PLN

## Descrição

Plano de Ação

---

## Resumo

- Campos: 57
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |
| RedPln | String(040) | Sim | Nome Reduzido do Plano de Ação |
| TipPln | Number(003,0) | Sim | Código Tipo do Plano de Ação |
| DatPln | Date | Sim | Data do Plano de Ação |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| OriPln | Number(002,0) | Sim | Código da origem do plano de ação |
| CodAgt | Number(006,0) | Sim | Código do Perigo/Fator de Risco |
| AgtCau | Number(003,0) | Sim | Código do Agente causador |
| PlnCol | String(250) | Sim | Descrição do Plano de Ação (Carácter Coletivo) |
| PlaAdm | String(250) | Sim | Descrição do Plano de Ação (Carácter Administrativo) |
| ObsPln | String(1000) | Sim | Observação do Plano de Ação |
| CodFil | Number(006,0) | Sim | Código da Filial |
| EmpRes | Number(004,0) | Não | Empresa do Colaborador Responsável pelo Plano de Ação |
| TipRes | Number(001,0) | Sim | Tipo de Colaborador Responsável pelo Plano Ação |
| CadRes | Number(009,0) | Sim | Cadastro Responsável pelo Plano Ação |
| ResCip | String(001) | Sim | Resumo da Cipa (S,N) |
| IniExe | Date | Sim | Data Início da Execução - Conforme Execução |
| FimExe | Date | Sim | Data Fim da Execução - Conforme Execução |
| EmpApr | Number(004,0) | Não | Empresa do Colaborador Responsável pela Aprovação |
| TipApr | Number(001,0) | Sim | Tipo de Colaborador Responsável Aprovação |
| CadApr | Number(009,0) | Sim | Cadastro Responsável Aprovação |
| DatApr | Date | Sim | Data da Aprovação |
| EmpExe | Number(004,0) | Não | Empresa do Colaborador Responsável pela Execução |
| TipExe | Number(001,0) | Sim | Tipo de Colaborador  Responsável Execução |
| CadExe | Number(009,0) | Sim | Cadastro Responsável Execução |
| DscSol | String(1000) | Sim | Descrição da Solução |
| LocApr | Number(009,0) | Sim | Local de Aprovação |
| LocExe | Number(009,0) | Sim | Local de Execução |
| IniApr | Date | Sim | Data Início da Execução - Conforme Aprovação |
| FimApr | Date | Sim | Data Fim da Execução - Conforme Aprovação |
| DatIni | Date | Sim | Data Início da Execução - Conforme Sugestão Inicial |
| DatFim | Date | Sim | Data Fim da Execução - Conforme Sugestão Inicial |
| SitPln | Number(001,0) | Sim | Situação da Etapa |
| IndEfi | String(001) | Sim | Identificação de eficácia do plano |
| DscApr | String(1000) | Sim | Observação sobre a aprovação |
| DatCon | Date | Sim | Data de conclusão do plano |
| NomArq | String(250) | Sim | Arquivo |
| CodUsu | Number(010,0) | Sim | Código do usuário que criou o Plano de Ação |
| PriPln | Number(001,0) | Sim | Prioridade do Plano de ação |
| ObjPln | String(250) | Sim | Objetivos do Plano de Ação |
| MetQua | String(050) | Sim | Informar uma meta para o plano de ação |
| IndRes | String(100) | Sim | Informar os indicadores de resultado para o plano de ação |
| EstPos | Number(003,0) | Sim | Código da Estrutura de Postos de Trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho |
| CodPRA | Number(009,0) | Sim | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Sim | Código do GHE - Grupo Homogêneo de Exposição |
| CodInv | Number(007,0) | Sim | Código do Inventário de Riscos |
| NumAmb | Number(007,0) | Sim | Código do Ambiente de Trabalho |
| DatInv | Date | Sim | Data do Inventário de Riscos |
| SeqPln | String(020) | Sim | Sequência de Execução do Plano de Ação |
| CusPln | Number(015,2) | Sim | Valor do Custo do Plano de Ação |
| CusApr | Number(015,2) | Sim | Valor do Custo do Plano de Ação - Conforme Aprovação |
| CusExe | Number(015,2) | Sim | Valor do Custo do Plano de Ação - Conforme Execução |
| USU_OcoAct | Number(006,0) | Sim | Código Ocorrência |
| USU_TipOco | Number(001,0) | Sim | Tipo Ocorrência |

---

## Chave Primária

- NumEmp
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R084PLN_003

**Tabela:** R084TPN

| Origem | Destino |
|--------|---------|
| TipPln | TipPln |

### IR_R084PLN_006

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

