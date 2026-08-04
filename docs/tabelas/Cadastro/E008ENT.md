# E008ENT

## Descrição

Tabelas - Cidades para RAIS - Valores de entrada dos relatórios municipais

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRai | Number(007,0) | Não | Código da cidade utilizada para RAIS |
| CodMod | String(020) | Não | Código do modelo |
| NomVar | String(030) | Não | Nome da variável |
| ValSeq | Number(002,0) | Não | Sequência do valor da variável de entrada do modelo de relatório |
| TipVar | Number(003,0) | Sim | Tipo da variável |
| ValNum | Number(021,6) | Sim | Valor numérico |
| ValStr | String(400) | Sim | Descrição das entradas dos relatórios |

---

## Chave Primária

- CodEmp
- CodRai
- CodMod
- NomVar
- ValSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
