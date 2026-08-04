# E049SQL

## Descrição

Configurador de SQL

---

## Resumo

- Campos: 17
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodSql | Number(009,0) | Não | Código de geração do SQL |
| SeqSql | Number(004,0) | Não | Sequencial de montagem do SQL |
| TabBas | String(255) | Não | Tabela base para a montagem do SQL |
| DesSql | String(050) | Sim | Descrição do SQL |
| DocSql | String(999) | Sim | Documentação do SQL |
| DatSql | String(015) | Sim | Campo data a ser utilizado no filtro |
| MulCam | String(001) | Não | Múltiplos campos como retorno do SQL |
| RetSql | String(999) | Sim | Descritivo do retorno do SQL |
| OpeSql | String(001) | Sim | Operação sobre o retorno do SQL |
| ConSql | String(999) | Sim | Descritivo da expressão do condicional do SQL |
| AgrSql | String(999) | Sim | Descritivo do agrupamento do SQL |
| OrdSql | String(999) | Sim | Descritivo da ordenação do SQL |
| TipSql | String(001) | Sim | Tipo do SQL |
| SitSql | String(001) | Sim | Situação do SQL |
| CodReg | Number(004,0) | Sim | Código da regra do SQL |
| TxtSql | String(1999) | Sim | Select completo definido pelo configurador |

---

## Chave Primária

- CodEmp
- CodSql
- SeqSql

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E049SQL_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

