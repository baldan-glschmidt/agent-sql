# R047DEE

## Descrição

CIF - Cadastro de Empresas (Exceções)

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodDep | Number(002,0) | Não | Código do Dependente |
| CodTrs | String(005) | Sim | Código da Transação |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Sim | Conta Financeira |
| CodNtg | Number(004,0) | Sim | Natureza do Gasto |
| GruCon | String(003) | Sim | Código do grupo de contas a receber ou pagar |

---

## Chave Primária

- CodCif
- NumEmp
- TipCol
- NumCad
- CodDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
