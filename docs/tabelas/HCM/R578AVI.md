# R578AVI

## Descrição

Avaliação de Competências - Avaliação por foco - Itens avaliados

---

## Resumo

- Campos: 21
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colaborador avaliado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador avaliado |
| NumCad | Number(009,0) | Não | Colaborador avaliado |
| CodCic | Number(003,0) | Não | Indica a qual Ciclo esta Avaliação pertence |
| IdeAva | Number(005,0) | Não | Identificador da avaliação de competências |
| SeqAvf | Number(007,0) | Não | Sequência da avaliação por foco, dentro da avaliação do colaborador |
| SeqCpt | Number(005,0) | Não | Sequência do item avaliado |
| CodCpt | Number(009,0) | Sim | Competência avaliada |
| RevCpt | String(010) | Sim | Revisão da competência avaliada |
| PrfApl | Number(004,0) | Sim | Perfil de aplicação da competência que foi avaliado |
| CptAva | String(001) | Sim | Indica se a competência foi escolhida para ser avaliada |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da revisão da competência |
| NotCpt | Number(008,4) | Sim | Nota avaliada para a competência |
| CodCPr | String(010) | Sim | Conceito avaliado para a competência |
| PerCpt | Number(007,4) | Sim | Percentual atingido para a Competência em relação a tabela de proficiências |
| MetCpt | Number(008,4) | Sim | Meta para o próximo ciclo de avaliação da competência |
| ComAvl | String(8001) | Sim | Comentário do avaliador para a competência |
| GruReq | String(010) | Sim | Código do grupo de requisitos que deu origem a competência |
| RevGRq | String(010) | Sim | Revisão do grupo de requisitos |
| ExiRqu | String(001) | Sim | Exigência do requisito |
| PtsReq | Number(008,4) | Sim | Pontuação do requisito |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- IdeAva
- SeqAvf
- SeqCpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578AVI_005

**Tabela:** R578AVF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| IdeAva | IdeAva |
| SeqAvf | SeqAvf |

### IR_R578AVI_008

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

### IR_R578AVI_011

**Tabela:** R577PRO

| Origem | Destino |
|--------|---------|
| CodTpr | CodTpr |

