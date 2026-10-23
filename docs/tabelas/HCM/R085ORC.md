# R085ORC

## Descrição

Orçamento - Quantidade de Colaboradores - Local

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CmpOrc | Date | Não | Competência Orçamento |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| QtdCol | Number(004,0) | Sim | Quantidade Colaboradores |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CmpOrc
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085ORC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085ORC_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R085ORC_004

**Tabela:** R048NAT

| Origem | Destino |
|--------|---------|
| NatDes | NatDes |

