# R530RCP

## Descrição

Grupo de Requisitos - Competência

---

## Resumo

- Campos: 19
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruReq | String(010) | Não | Código do grupo de requisitos |
| RevGRq | String(010) | Não | Revisão do grupo de requisitos |
| SeqCpt | Number(003,0) | Não | Numero sequencial que identifica o requisito de competência |
| CodCpt | Number(009,0) | Sim | Competência que é requisito para esta revisão |
| RevCpt | String(010) | Sim | Revisão da competência requisitada |
| PrfApl | Number(004,0) | Sim | Código do perfil de aplicação da competência |
| NotCpt | Number(008,4) | Sim | Determina a nota mínima para o atendimento do requisito |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da revisão da competência do requisito |
| CodCPr | String(010) | Sim | Determina o conceito mínimo para o atendimento do requisito |
| ExiRqu | String(001) | Sim | Exigência do requisito |
| PtsReq | Number(008,4) | Sim | Pontuação do requisito |
| ConAut | String(001) | Sim | Considera requisito nas avaliações com foco Autoavaliação |
| ConSup | String(001) | Sim | Considera requisito nas avaliações com foco Superior |
| ConSub | String(001) | Sim | Considera requisito nas avaliações com foco Subordinado |
| ConPar | String(001) | Sim | Considera requisito nas avaliações com foco Cargo par |
| ConCli | String(001) | Sim | Considera requisito nas avaliações com foco Cliente |
| ConFor | String(001) | Sim | Considera requisito nas avaliações com foco Fornecedor |
| ConIns | String(001) | Sim | Considera requisito nas avaliações com foco Instrutor |
| ConCon | String(001) | Sim | Considera requisito nas avaliações com foco Consenso |

---

## Chave Primária

- GruReq
- RevGRq
- SeqCpt

---

## Índices

### R530RCPIndice1

**Tipo:** Não unico

Campos:
- GruReq
- RevGRq
- CodCpt
- RevCpt
- PrfApl

---

## Relacionamentos

### IR_R530RCP_001

**Tabela:** R530REV

| Origem | Destino |
|--------|---------|
| GruReq | GruReq |
| RevGRq | RevGRq |

### IR_R530RCP_004

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

