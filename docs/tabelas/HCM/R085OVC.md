# R085OVC

## Descrição

Orçamento - Valores Calculados - C.Custo

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| CmpOrc | Date | Não | Competência Orçamento |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| ResOrc | Number(003,0) | Não | Item do Resultado |
| ValOrc | Number(011,2) | Sim | Valor do Orçamento |

---

## Chave Primária

- NumEmp
- CodCcu
- CmpOrc
- NatDes
- ResOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085OVC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R085OVC_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R085OVC_003

**Tabela:** R048NAT

| Origem | Destino |
|--------|---------|
| NatDes | NatDes |

### IR_R085OVC_004

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| ResOrc | IteOrc |

