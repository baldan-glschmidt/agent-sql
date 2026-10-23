# R047SEE

## Descrição

CIF - Cadastro de Empresas (Sindicatos)

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| CodSin | Number(004,0) | Não | Código do Sindicato |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTrs | String(005) | Sim | Código da Transação |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Sim | Conta Financeira |
| CodNtg | Number(004,0) | Sim | Natureza do Gasto |
| GruCon | String(003) | Sim | Código do grupo de contas a receber ou pagar |

---

## Chave Primária

- CodCif
- CodSin
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
