# E045CAG

## Descrição

Tabelas - Aglutinação Contábil - Composição

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAgl | Number(009,0) | Não | Código da aglutinação contábil |
| SeqCmp | Number(004,0) | Não | Sequência do registro de composição |
| CtaRed | Number(007,0) | Sim | Número da conta reduzida |
| CodCcu | String(009) | Sim | Código do centro de custo |
| VlrRef | String(001) | Sim | Valor de referência para composição |
| OpeAgl | String(001) | Sim | Tipo de operação |
| CmpAgl | Number(004,0) | Sim | Competência de referência |
| AglCag | Number(009,0) | Sim | Código da aglutinação contábil da composição |
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodSql | Number(009,0) | Sim | Código de geração do SQL |
| SeqSql | Number(004,0) | Sim | Sequencial de montagem do SQL |

---

## Chave Primária

- CodAgl
- SeqCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E045CAG_000

**Tabela:** E045AGL

| Origem | Destino |
|--------|---------|
| CodAgl | CodAgl |

