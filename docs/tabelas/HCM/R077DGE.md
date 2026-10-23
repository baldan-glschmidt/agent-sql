# R077DGE

## Descrição

Avaliação - Definição Geral

---

## Resumo

- Campos: 49
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ResMan | String(001) | Sim | Define se tem restrição de manutenção das avaliações |
| ModAva | String(011) | Sim | Modelo de Relatório Default para emissão da avaliação |
| AprIte | String(001) | Sim | Define como serão apresentados os itens da avaliação |
| DefPer | Number(001,0) | Sim | Define permissão de acesso ao registro de anotações |
| NumLot | Number(009,0) | Sim | Último nr. de lote gerado, alimentado pela geração coletiva |
| AprFam | String(001) | Sim | Define se avaliação será apresentado a família de conhecimento |
| ModAno | String(011) | Sim | Modelo de Relatório default para listar as anotações |
| ModCon | String(011) | Sim | Mod. Rel. default p/ listar o comparativo de notas conhecimento |
| ModPer | String(011) | Sim | Mod. Rel. default p/ listar o comparativo de notas performance |
| ModExc | String(011) | Sim | Mod. Rel. default p/ listar o comparativo de notas excelência |
| UtiFin | String(001) | Sim | Define se o sistema deve utilizar o % Final da Avaliação |
| PesCnc | Number(002,0) | Sim | Peso para as Avaliações de Conhecimentos |
| PesPer | Number(002,0) | Sim | Peso para as Avaliações de Performance |
| PesExc | Number(002,0) | Sim | Peso para as Avaliações de Excelência |
| PesApf | Number(002,0) | Sim | Peso para o resultado de Aperfeiçoamento nas Avaliações |
| PesFor | Number(002,0) | Sim | Peso para o resultado de Formação nas Avaliações |
| LotRes | Number(009,0) | Sim | Último nr. de lote da rotina de Apurar Resultados |
| ApuCnc | String(001) | Sim | Define quais Conhecimentos devem ser considerados na apuração |
| SelTAv | String(001) | Sim | Permite selecionar o Foco da Avaliação na WEB |
| ForAva | String(001) | Sim | Forma de Avaliação na WEB (por Colaborador e/ou por Item) |
| VisAno | Number(001,0) | Sim | Interfere na visualização das anotações |
| MosLeg | String(001) | Sim | Define se mostra a legenda na tela de requisitos na avaliação WEB |
| ModPdi | String(011) | Sim | Mod. Rel default do PDI (Plano de desenvolvimento Individual) |
| ResAva | Number(001,0) | Sim | Define restrição de manutenção das avaliações de resultado |
| IdeCic | String(001) | Sim | Exige identificação do ciclo nos processos de avaliações |
| DifIte | String(001) | Sim | Define itens diferentes conforme o foco da avaliação |
| PerRea | String(001) | Sim | Define se o avaliador pode reabrir avaliações de resultado |
| FasPDI | Number(001,0) | Sim | Fase do PDI |
| CodReg | Number(003,0) | Sim | Regra para gerenciamento do PDI na avaliação |
| OriPDI | Number(001,0) | Sim | Indica a origem do PDI por habilidade técnica na avaliação de performance |
| PDICur | String(001) | Sim | Define se considera cursos no PDI das avaliações |
| PDICon | String(001) | Sim | Define se considera conhecimentos no PDI das avaliações |
| ReqCar | Number(001,0) | Sim | Define se apresenta requisitos do cargo no PDI |
| AprPDe | String(001) | Sim | Apresentar o plano de desenvolvimento na Avaliação de Desempenho e Competência |
| AprEmp | String(001) | Sim | Define se apresenta a empresa do avaliador no Cadastro de Avaliadores Individuais do CSWEB |
| AprPDR | String(001) | Sim | Apresentar o plano de desenvolvimento na Avaliação de Resultados |
| ModAvR | String(011) | Sim | Modelo Avaliação de Resultado (Histórico Avaliações) |
| ResCom | String(001) | Sim | Torna a visualização do Comentário do Avaliador restrita a ele mesmo. |
| AprMed | Number(001,0) | Sim | Indica se apresenta média na avaliação de desempenho e competência. |
| HabCom | String(001) | Sim | Indica se utiliza o conceito de habilidades essenciais e complementares. |
| AprCer | String(001) | Sim | Indica se apresenta a coluna de certificação na avaliação |
| AprFot | String(001) | Sim | Define se apresenta foto do avaliado no cabeçalho da avaliação WEB |
| FotAvl | String(001) | Sim | Define se apresenta foto do colaborador no cadastro de Avaliadores Individuais na WEB |
| AprPer | String(001) | Sim | Apresenta período no cadastro de avaliadores na WEB quando utiliza Ciclo |
| DefMut | Number(001,0) | Sim | Define um padrão para o campo Definição Mútua do cadastro de avaliadores. |
| ResInd | Number(001,0) | Sim | Define restrição de aprovação do cadastro de avaliadores individuais. |
| RegApr | Number(003,0) | Sim | Regra para identificar os aprovadores do cadastro de avaliadores individuais. |
| ColNot | Number(001,0) | Sim | Define como será apresentada a coluna nota na avaliação de desempenho e competência. |
| OriPDR | Number(001,0) | Sim | Indica a origem do PDI na avaliação de resultados |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
