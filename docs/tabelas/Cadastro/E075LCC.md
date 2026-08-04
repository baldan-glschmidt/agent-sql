# E075LCC

## Descrição

Tabelas - Produto - Ligação Contas para Preço de Custo por Produto

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeMes | Number(009,0) | Não | Sequencial registro Custo do Produto por Data |
| IdePcd | Number(009,0) | Não | Sequencial registro Preço Custo por produto e derivação |
| CodEmp | Number(004,0) | Não | Código da empresa |
| DatIni | Date | Não | Data Inicial do período |
| DatFim | Date | Não | Data final do período |
| CodCcu | String(009) | Sim | Centro de custo a classificar |
| CtaRed | Number(007,0) | Sim | Conta contábil a classificar |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
