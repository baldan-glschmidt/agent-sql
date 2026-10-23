# R583CAD

## Descrição

GHE - Cadastro de PGR

---

## Resumo

- Campos: 22
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| DesCad | String(060) | Sim | Descrição do Cadastro de PGR |
| TabOrg | Number(004,0) | Sim | Código da tabela de organograma do local |
| EstCar | Number(004,0) | Sim | Código da estrutura de cargos |
| InfExa | String(001) | Sim | Indica se os GHEs do PGR permitirão informar exames |
| AtiGHE | String(001) | Sim | Indica que o sistema deve buscar as Atividades de Risco do GHE |
| AtiCar | String(001) | Sim | Indica que o sistema deve buscar as Atividades de Risco do Cargo |
| IDCAti | String(100) | Sim | Itens de descrição do Cargo que serão considerados para montar as Ativ. de Risco |
| AtiPos | String(001) | Sim | Indica que o sistema deve buscar as Atividades de Risco do Posto |
| EstPos | Number(003,0) | Sim | Estrutura de Postos de Trabalho usada para buscar os itens de descrição |
| IDPAti | String(100) | Sim | Itens de descrição do Posto que serão considerados para monta as Ativ. de Risco |
| CodPes | Number(009,0) | Sim | Código da Pessoa responsável por assinar o PPP |
| JusExa | String(200) | Sim | Permite definir uma justificativa para listar o PPP, quando não houver exames |
| JusCat | String(200) | Sim | Justificativa para constar no campo CAT do  PPP |
| JusAss | String(200) | Sim | Justificativa para uso de assinatura eletrônica no PPP |
| JusGer | String(3000) | Sim | Justificativa geral p/ constar antes data emissão do  PPP |
| AnoCad | String(2000) | Sim | Permite informar anotações referentes ao Cadastro de PGR |
| EstMet | String(20000) | Sim | Permite informar a estratégia e metodologia de ação do PGR |
| IntLau | String(500) | Sim | Texto com a Introdução a ser utilizado no modelo LTCAT |
| ConLau | String(500) | Sim | Texto com a Conclusão a ser utilizado no modelo LTCAT |
| MetErg | String(999) | Sim | Descrição da metodologia utilizada para o levantamento dos riscos ergonômicos. |
| ObsCom | String(999) | Sim | Observação(ões) complementar(es) referente(s) a registros ambientais. |

---

## Chave Primária

- CodPRA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583CAD_002

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R583CAD_003

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

