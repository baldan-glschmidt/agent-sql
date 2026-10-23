# R578AVD

## Descrição

Avaliação de Competências - Avaliação por foco - Itens avaliados - Evidências

---

## Resumo

- Campos: 17
- Chave Primária: 11 campo(s)
- Índices: 0
- Relacionamentos: 4

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
| CodCpt | Number(009,0) | Não | Competência avaliada |
| RevCpt | String(010) | Não | Revisão da competência avaliada |
| PrfApl | Number(004,0) | Não | Perfil de aplicação da competência que foi avaliado |
| SeqEvd | Number(004,0) | Não | Evidência avaliada para a competência |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da evidência da competência |
| NotEvd | Number(008,4) | Sim | Nota avaliada para a evidência da competência |
| CodCPr | String(010) | Sim | Conceito avaliado para a evidência da competência |
| PerEvd | Number(007,4) | Sim | Percentual atingido para a evidência em relação a tabela de proficiências |
| PesEvd | Number(007,4) | Sim | Peso da evidência em relação as demais evidências do perfil |
| MetEvd | Number(008,4) | Sim | Meta para a evidência |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- IdeAva
- SeqAvf
- SeqCpt
- CodCpt
- RevCpt
- PrfApl
- SeqEvd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578AVD_006

**Tabela:** R578AVI

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| IdeAva | IdeAva |
| SeqAvf | SeqAvf |
| SeqCpt | SeqCpt |

### IR_R578AVD_008

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

### IR_R578AVD_010

**Tabela:** R577EVD

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |
| PrfApl | PrfApl |
| SeqEvd | SeqEvd |

### IR_R578AVD_011

**Tabela:** R577PRO

| Origem | Destino |
|--------|---------|
| CodTpr | CodTpr |

