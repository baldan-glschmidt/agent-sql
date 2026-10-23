# R085ORV

## Descrição

Orçamento - Valores Calculados - Local

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CmpOrc | Date | Não | Competência Orçamento |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| ResOrc | Number(003,0) | Não | Item do Resultado |
| ValOrc | Number(011,2) | Sim | Valor do Orçamento |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CmpOrc
- NatDes
- ResOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085ORV_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085ORV_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R085ORV_004

**Tabela:** R048NAT

| Origem | Destino |
|--------|---------|
| NatDes | NatDes |

### IR_R085ORV_005

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| ResOrc | IteOrc |

