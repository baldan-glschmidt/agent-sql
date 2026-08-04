# E070TES

## Descrição

Cadastros - Filiais - Parâmetros Tesouraria

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CxbCmj | String(005) | Sim | Transação padrão de crédito para correção monetária de juros da prestação de empréstimos |
| CxbDmj | String(005) | Sim | Transação padrão de débito para correção monetária de juros das prestações de empréstimos |
| CxbCcj | String(005) | Sim | Transação estorno crédito de correção monetária de juros das prestações de empréstimos |
| CxbCdj | String(005) | Sim | Transação estorno débito de correção monetária de juros das prestações de empréstimos |
| CxbPcj | String(005) | Sim | Transação pagamento crédito correção monetária de juros das prestações de empréstimos |
| CxbPdj | String(005) | Sim | Transação pagamento débito correção monetária de juros das prestações de empréstimos |
| CxbCej | String(005) | Sim | Transação estorno pgto. crédito correção monetária de juros das prestações de empréstimos |
| CxbDej | String(005) | Sim | Transação estorno pgto. débito correção monetária de juros das prestações de empréstimos |
| CxbDmf | String(005) | Sim | Transação débito mercado derivativo futuro |
| CxbCmf | String(005) | Sim | Transação crédito mercado derivativo futuro |
| CxbPrd | String(005) | Sim | Transação de provisão de IRRF para contratos derivativos |
| CxbPid | String(005) | Sim | Transação de provisão de IOF para contratos derivativos |
| CxbErd | String(005) | Sim | Transação de estorno de provisão de IRRF para contratos derivativos |
| CxbEid | String(005) | Sim | Transação de estorno de provisão de IOF para contratos derivativos |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070TES_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

