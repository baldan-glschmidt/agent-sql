# E019RET

## Descrição

Tabelas - Controle de Retenção de Impostos

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor |
| CodCli | Number(009,0) | Não | Código do cliente |
| TipImp | Number(002,0) | Não | Tipo de imposto |
| MesAno | Date | Não | Mês / Ano da retenção do imposto |
| VlrBas | Number(015,2) | Sim | Valor base do imposto retido |
| VlrRet | Number(015,2) | Sim | Valor do imposto retido |
| CgcCpf | Number(008,0) | Sim | Número do CNPJ ou CPF do cliente/fornecedor |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do cliente/fornecedor |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- CodCli
- TipImp
- MesAno

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
