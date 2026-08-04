# E000ITM

## Descrição

Intermediadores da Transação (NF-e/NFC-e)

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
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodItm | Number(004,0) | Não | Código do intermediador da Transação |
| NomItm | String(100) | Sim | Nome do intermediador da Transação |
| CgcItm | Number(014,0) | Sim | CNPJ do intermediador da Transação |
| DocIdeItm | String(014) | Sim | CNPJ do intermediador da Transação |
| CadItm | String(060) | Sim | Identificador cadastrado no intermediador |

---

## Chave Primária

- CodEmp
- CodItm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
