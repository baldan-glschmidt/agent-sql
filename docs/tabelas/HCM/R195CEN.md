# R195CEN

## Descrição

Cenário - Cadastro

---

## Resumo

- Campos: 47
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| DesRed | String(030) | Sim | Descrição reduzida para identificação do cenário |
| DesDet | String(500) | Sim | Descrição mais completa para identificação do cenário |
| CmpBas | Date | Sim | Competência de referência, considerada base para geração do cenário |
| SitOrg | String(001) | Sim | Utiliza organograma oficial(S/N) |
| TabOrg | Number(004,0) | Sim | Código da tabela de organograma para uso no cenário |
| MovCol | String(001) | Sim | Permite movimentações coletivas(S/N) |
| TipTrf | Number(001,0) | Sim | Para transferência de empresa, indica se haverá cálculo de rescisão |
| CauTrf | Number(002,0) | Sim | Causa padrão de transferência de empresa sem ônus |
| CauTro | Number(002,0) | Sim | Causa padrão de transferência de empresa com ônus |
| CauInE | Number(002,0) | Sim | Causa padrão de demissão - iniciativa empregador |
| CauInC | Number(002,0) | Sim | Causa padrão de demissão - iniciativa colaborador |
| CodMot | Number(003,0) | Sim | Motivo da alteração de cargo em admissões e transferências de empresa |
| BotQu1 | String(020) | Sim | Nome do 1º Botão para uso na manutenção do quadro |
| BotQu2 | String(020) | Sim | Nome do 2º Botão para uso na manutenção do quadro |
| BotQu3 | String(020) | Sim | Nome do 3º Botão para uso na manutenção do quadro |
| MBoQu1 | String(011) | Sim | Modelo gerador relatórios do 1º botão para uso na manutenção do quadro |
| MBoQu2 | String(011) | Sim | Modelo gerador relatórios do 2º botão para uso na manutenção do quadro |
| MBoQu3 | String(011) | Sim | Modelo gerador relatórios do 3º botão para uso na manutenção do quadro |
| RBoQu1 | Number(003,0) | Sim | Código da regra do 1º botão para uso na manutenção do quadro |
| RBoQu2 | Number(003,0) | Sim | Código da regra do 2º botão para uso na manutenção do quadro |
| RBoQu3 | Number(003,0) | Sim | Código da regra do 3º botão para uso na manutenção do quadro |
| CodFil | Number(006,0) | Sim | Código filial padrão para admissões |
| CodSin | Number(004,0) | Sim | Código do sindicato padrão para admissões |
| NumLoc | Number(009,0) | Sim | Local padrão do organograma para admissões |
| CodEsc | Number(009,0) | Sim | Código padrão da escala para admissões |
| TipCon | Number(002,0) | Sim | Tipo de Contrato padrão para admissões |
| CodVin | Number(002,0) | Sim | Tipo de Vínculo padrão para admissões |
| DefCen | String(001) | Sim | Indica se as definições de percentuais serão por cenário |
| AbrSit | String(500) | Sim | Situações para considerar no cenário |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| TipOrc | Number(001,0) | Sim | Identificar se o cenário para orçamento anual ou mensal |
| BotInt | String(020) | Sim | Nome do botão para uso na integração dos valores do orçamento com o Financeiro |
| ModInt | String(013) | Sim | Modelo gerador relatórios de exportação dos valores de orçamento |
| ArqSai | String(100) | Sim | Nome do Arquivo de Saída para integração dos valores do orçamento |
| InfSal | String(001) | Sim | Apresenta informações salariais nas admissões e promoções coletivas (S/N) |
| ComSal | String(001) | Sim | Utiliza a composição salarial no histórico salarial do cenário (S/N) |
| SalVar | Number(001,0) | Sim | Define se o salário da variação deve ser proporcional a data do quadro de vagas diário |
| ConSal | Number(001,0) | Sim | Define se deve consistir o salário nas transferências coletivas |
| SalTrf | String(001) | Sim | Define se deve permitir informar o salário de destino de uma transferência |
| CenPos | String(001) | Sim | Define se o cenário utilizará definições por posto de trabalho |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho para uso no cenário. |
| BusCen | Number(001,0) | Sim | Define a forma de buscar o cenário de destino de uma transferência de empresa. |
| OriCon | Number(001,0) | Sim | Origem das Contas Contábeis |
| OrdAdi | Number(001,0) | Sim | Ordem de busca dos adicionais |
| SalCar | String(001) | Sim | Carregar as informações salariais configuradas no cargo (S/N) |

---

## Chave Primária

- NumEmp
- CodCen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195CEN_006

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

