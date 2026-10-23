# R085OCC

## Descrição

Orçamento - Quantidade de Colaboradores - C.Custo

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| CmpOrc | Date | Não | Competência Orçamento |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| QtdCol | Number(004,0) | Sim | Quantidade Colaboradores |

---

## Chave Primária

- NumEmp
- CodCcu
- CmpOrc
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085OCC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085OCC_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R085OCC_003

**Tabela:** R048NAT

| Origem | Destino |
|--------|---------|
| NatDes | NatDes |

