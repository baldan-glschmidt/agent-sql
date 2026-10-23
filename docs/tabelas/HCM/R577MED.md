# R577MED

## Descrição

Competência - Revisão - Itens de Medição

---

## Resumo

- Campos: 22
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCpt | Number(009,0) | Não | Código da Competência |
| RevCpt | String(010) | Não | Código da Revisão da Competência |
| PrfApl | Number(004,0) | Não | Indica a qual Perfil de aplicação o item de desenvolvimento pertence |
| SeqCnd | Number(003,0) | Não | Sequência da condição de medição |
| SeqIte | Number(003,0) | Não | Sequência do item de desenvolvimento da competência |
| TpIMed | Number(001,0) | Sim | Tipo de item de medição da competência |
| CodCua | Number(009,0) | Sim | Curso de aperfeiçoamento para medir a competência |
| AbrSit | String(100) | Sim | Situações dos cursos de aperfeiçoamento/formação |
| NotMiC | Number(008,4) | Sim | Nota mínima no curso de aperfeiçoamento |
| NotMaC | Number(008,4) | Sim | Nota máxima no curso de aperfeiçoamento |
| CodCuf | Number(004,0) | Sim | Curso de formação para medir a competência |
| CodTpr | Number(004,0) | Sim | Tabela de proficiência da competência |
| NotMin | Number(008,4) | Sim | Nota mínima da avaliação de desempenho |
| CodCPr | String(010) | Sim | Conceito mínimo da avaliação de desempenho |
| PerIte | Number(007,4) | Sim | Percentual mínimo da avaliação de desempenho |
| NomTag | String(1000) | Sim | Tag |
| TipExp | String(001) | Sim | Tipo Experiência (anos/meses) |
| ExpCar | Number(002,0) | Sim | Experiência |
| ExpDes | Number(002,0) | Sim | Experiência desejada |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Cargo |
| GruEqe | Number(003,0) | Sim | Grupo de Equivalência |

---

## Chave Primária

- CodCpt
- RevCpt
- PrfApl
- SeqCnd
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R577MED_001

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

### IR_R577MED_002

**Tabela:** R577PRF

| Origem | Destino |
|--------|---------|
| PrfApl | PrfApl |

### IR_R577MED_003

**Tabela:** R577CND

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |
| PrfApl | PrfApl |
| SeqCnd | SeqCnd |

