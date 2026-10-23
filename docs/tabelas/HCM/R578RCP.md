# R578RCP

## Descrição

Avaliação de Competências - Resultado por Competência

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colaborador avaliado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador avaliado |
| NumCad | Number(009,0) | Não | Colaborador avaliado |
| CodCic | Number(003,0) | Não | Indica a qual Ciclo esta Avaliação pertence |
| IdeAva | Number(005,0) | Não | Identificador da avaliação de competências |
| SeqCpt | Number(005,0) | Não | Sequência do item avaliado |
| CodCpt | Number(009,0) | Sim | Competência avaliada |
| RevCpt | String(010) | Sim | Revisão da competência avaliada |
| PrfApl | Number(004,0) | Sim | Perfil de aplicação da competência que foi avaliado |
| NotRcp | Number(008,4) | Sim | Nota da avaliação para o Tipo da competência |
| PerRcp | Number(007,4) | Sim | Percentual de atingimento da avaliação para o Tipo da competência |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- IdeAva
- SeqCpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578RCP_004

**Tabela:** R578AVA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| IdeAva | IdeAva |

### IR_R578RCP_007

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

