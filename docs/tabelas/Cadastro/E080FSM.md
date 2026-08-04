# E080FSM

## Descrição

Cadastros - Serviços - Ligação Fornecedor X Serviço X Município

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFor | Number(009,0) | Não | Código do fornecedor |
| CodSer | String(014) | Não | Código do serviço |
| RaiFor | Number(007,0) | Não | Código da cidade do fornecedor |
| RaiPrt | Number(007,0) | Não | Código da cidade da prestação do serviço |
| DatIni | Date | Não | Data de início da vigência |
| TnsOcp | String(005) | Sim | Código da transação de serviço da ordem de compra |
| TnsNfc | String(005) | Sim | Código da transação de serviço da nota fiscal de entrada |
| ChvRot | String(250) | Sim | Nomes e valores de chave do registro |

---

## Chave Primária

- CodEmp
- CodFor
- CodSer
- RaiFor
- RaiPrt
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
