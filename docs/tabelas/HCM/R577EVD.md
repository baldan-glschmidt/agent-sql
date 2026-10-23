# R577EVD

## Descrição

Competência - Revisão - Evidências

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCpt | Number(009,0) | Não | Código da Competência |
| RevCpt | String(010) | Não | Código da Revisão da Competência |
| PrfApl | Number(004,0) | Não | Indica a qual Perfil de aplicação a evidência pertence |
| SeqEvd | Number(004,0) | Não | Sequência da evidência da revisão da competência |
| DesEvd | String(1600) | Sim | Descrição da evidência da revisão da competência |
| PesEvd | Number(007,4) | Sim | Peso da evidência em relação as demais evidências do perfil |
| CodTpr | Number(004,0) | Sim | Indica a Tabela de proficiências válida para a evidência |
| ConAut | String(001) | Sim | Indica se a evidência será considerada nas autoavaliações |
| ConSup | String(001) | Sim | Indica se a evidência será considerada nas avaliações feitas pelo Superior |
| ConSub | String(001) | Sim | Indica se a evidência será considerada nas avaliações feitas pelo Subordinado |
| ConPar | String(001) | Sim | Indica se a evidência será considerada nas avaliações feitas pelos Pares |
| ConCli | String(001) | Sim | Indica se a evidência será considerada nas avaliações feitas pelos Clientes |
| ConFor | String(001) | Sim | Indica se a evidência será considerada nas avaliações feitas pelos Fornecedores |
| ConIns | String(001) | Sim | Indica se a evidência será considerada nas avaliações feitas pelos Instrutores |
| ConCon | String(001) | Sim | Indica se a evidência será considerada nas avaliações de Consenso |

---

## Chave Primária

- CodCpt
- RevCpt
- PrfApl
- SeqEvd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R577EVD_001

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

### IR_R577EVD_002

**Tabela:** R577PRF

| Origem | Destino |
|--------|---------|
| PrfApl | PrfApl |

### IR_R577EVD_006

**Tabela:** R577PRO

| Origem | Destino |
|--------|---------|
| CodTpr | CodTpr |

