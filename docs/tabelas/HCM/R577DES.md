# R577DES

## Descrição

Competência - Revisão - Itens de Desenvolvimento

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCpt | Number(009,0) | Não | Código da Competência |
| RevCpt | String(010) | Não | Código da Revisão da Competência |
| PrfApl | Number(004,0) | Não | Indica a qual Perfil de aplicação o item de desenvolvimento pertence |
| SeqIte | Number(003,0) | Não | Sequência do item de desenvolvimento da revisão da competência |
| TpIDes | Number(001,0) | Sim | Tipo do item de desenvolvimento da competência |
| DesIte | String(500) | Sim | Item para desenvolvimento da competência |
| CodCua | Number(009,0) | Sim | Curso de Aperfeiçoamento para desenvolvimento da competência |
| CodCuf | Number(004,0) | Sim | Curso de Formação para desenvolvimento da competência |

---

## Chave Primária

- CodCpt
- RevCpt
- PrfApl
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R577DES_001

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

### IR_R577DES_002

**Tabela:** R577PRF

| Origem | Destino |
|--------|---------|
| PrfApl | PrfApl |

