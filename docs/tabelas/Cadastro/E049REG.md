# E049REG

## Descrição

Tabelas - Registro

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDec | Number(009,0) | Não | Código da declaração |
| CodReg | String(010) | Não | Código do registro da declaração |
| DesReg | String(250) | Sim | Descrição do registro da declaração |
| RegPai | String(010) | Sim | Código do registro de nível superior |
| NivReg | Number(004,0) | Sim | Nível de hierarquia do registro dentro da declaração |
| RefReg | String(250) | Sim | Referência de entrada/saída do registro |
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodSql | Number(009,0) | Sim | Código de geração do SQL |
| SeqSql | Number(004,0) | Sim | Sequencial de montagem do SQL |
| CodRgr | Number(004,0) | Sim | Código da Regra |
| SqlUsu | String(999) | Sim | SQL a nível de usuário para carga da massa de dados |

---

## Chave Primária

- CodDec
- CodReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
