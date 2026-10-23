# R126CMP

## Descrição

Requisições - Requisitos de Competências

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código da Requisição |
| CodCpt | Number(009,0) | Não | Determina a Competência adquirida na data informada |
| PrfApl | Number(004,0) | Sim | Indica qual foi o Perfil de aplicação adquirido para esta competência |
| RevCpt | String(010) | Sim | Determina qual Revisão da Competência foi adquirida na data informada |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da evidência da competência adquirida |
| CodCPr | String(010) | Sim | Determina qual Conceito foi percebido para a competência |
| NotCpt | Number(008,4) | Sim | Determina a nota adquirida para a Competência |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| PtsRca | Number(002,0) | Sim | Pontuação do Curso de Aperfeiçoamento |

---

## Chave Primária

- CodRqu
- CodCpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126CMP_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

