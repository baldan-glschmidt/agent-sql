# R900IMC

## Descrição

Descreve as alterações realizadas nos registros das tabelas monitoradas.

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqTran | Number(010,0) | Não | Número seqüêncial que identifica a transação que afetou o registro |
| SeqOp | Number(010,0) | Não | identificador da operação, dentro da transação, que afetou o registro. |
| CodOp | Number(001,0) | Não | Identificador da operação que afetou o registro |
| TblNam | String(018) | Não | Nome da tabela na qual o registro afetado pertence |
| ChvIte | String(255) | Não | Valores separados por ";" da chave do item afetado |
| AplMob | Number(005,0) | Não | Identificador do aplicativo interessado na alteração do registro |

---

## Chave Primária

- SeqTran
- SeqOp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
