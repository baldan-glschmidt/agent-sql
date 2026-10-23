# R101CIC

## Descrição

Ciclos

---

## Resumo

- Campos: 40
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| DesCic | String(030) | Sim | Descrição do ciclo de avaliação |
| IniCic | Date | Sim | Data de início do ciclo de avaliação |
| TerCic | Date | Sim | Data de término do ciclo de avaliação |
| IniObj | Date | Sim | Data de início da definição de objetivos |
| TerObj | Date | Sim | Data de término da definição de objetivos |
| IniRes | Date | Sim | Data de início da avaliação de resultados |
| TerRes | Date | Sim | Data de término da avaliação de resultados |
| DefCic | String(2000) | Sim | Descrição detalhada sobre o ciclo de avaliação |
| SitCic | Number(001,0) | Sim | Indica a situação do ciclo (1-Liberado, 2-Bloqueado) |
| IniAva | Date | Sim | Data de início do cadastro de avaliadores individuais |
| TerAva | Date | Sim | Data de término do cadastro de avaliadores individuais |
| IniApr | Date | Sim | Data de início da aprovação dos avaliadores individuais |
| TerApr | Date | Sim | Data de término da aprovação dos avaliadores individuais |
| MinInd | Number(003,0) | Sim | Define a quantidade mínima de avaliadores individuais. |
| MaxInd | Number(003,0) | Sim | Define a quantidade máxima de avaliadores individuais. |
| MaxAvl | Number(003,0) | Sim | Define a quantidade máxima que um colaborador pode estar como avaliador individual. |
| LimAdm | Date | Sim | Define a data de admissão limite para considerar os colaboradores avaliados. |
| IniPdo | Date | Sim | Data de início da definição de objetivos/planos de ação do plano de desenvolvimento |
| TerPdo | Date | Sim | Data de término da definição de objetivos do plano de desenvolvimento |
| IniPda | Date | Sim | Data de início do acompanhamento dos objetivos/planos de ação do plano de desenvolvimento |
| TerPda | Date | Sim | Data de término do acompanhamento dos objetivos/planos de ação do plano de desenvolvimento |
| ResMan | Number(001,0) | Sim | Define se tem restrição de manutenção das avaliações |
| ResCom | String(001) | Sim | Define se somente o avaliador poderá visualizar seus comentários. |
| CptOpc | String(001) | Sim | Indica se as competências desejáveis serão opcionais ao avaliar |
| AbrPrf | String(200) | Sim | Utilizações do grupo de requisitos que serão consideradas para avaliação |
| CalAvf | Number(001,0) | Sim | Determina como será o cálculo da nota da avaliação por foco |
| PesFoc | String(001) | Sim | Indica se o cálculo da avaliação considerará peso por foco de avaliação |
| PesTpC | String(001) | Sim | Indica se o cálculo da avaliação considerará peso por Tipo de competência |
| PesCpt | String(001) | Sim | Indica se o cálculo da avaliação considerará os pesos das Competências |
| IniGDE | Date | Sim | Data de início da realização da Gestão de Desempenho |
| TerGDE | Date | Sim | Data de término da realização da Gestão de Desempenho |
| CodPer | Number(004,0) | Sim | Perfil do Formulário de Matriz de Gestão |
| EixMat | Number(001,0) | Sim | Indica em qual eixo da Matriz de Gestão são apresentadas as avaliações |
| RegCpt | Number(003,0) | Sim | Regra para cálculo da Média/Percentual da Av. Competências na Gestão Desempenho |
| RegObj | Number(003,0) | Sim | Regra para cálculo da Média/Percentual da Av. Objetivos na Gestão Desempenho |
| TprCpt | Number(004,0) | Sim | Tabela de Proficiências usada para média de Competências na Gestão de Desempenho |
| TprObj | Number(004,0) | Sim | Tabela de Proficiências usada para média de Objetivos na Gestão de Desempenho |
| SitGDE | Number(001,0) | Sim | Situação inicial da Gestão de Desempenho |
| RegGDE | Number(003,0) | Sim | Informar a regra a ser executada após criar a Gestão de Desempenho |

---

## Chave Primária

- CodCic

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
