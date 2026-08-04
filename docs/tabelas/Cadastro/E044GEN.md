# E044GEN

## Descrição

Cadastros - Tabela auxiliar genérica para composição de calculo de distribuição

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CcuDis | String(009) | Sim | Código do centro de custos |
| CtaRed | Number(007,0) | Sim | Número Reduzido Conta Contábil |
| VlrRat | Number(014,2) | Sim | Valor do rateio para o centro de resultado |
| DatFim | Date | Não | Data de lançamento base do rateio |
| DscTab | String(300) | Sim | Descrição da Tabela |
| UsuAlt | Number(010,0) | Sim | Identificador do usuário |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
