# R174CND

## Descrição

Contas C. Custo - Contas p/ Nat. Despesa

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código do C.Custo Contábil |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| NatDes | Number(003,0) | Não | Natureza de despesa |
| CodCon | String(030) | Sim | Código da conta contábil |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |

---

## Chave Primária

- NumEmp
- CodCcu
- TabEve
- CodClc
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R174CND_003

**Tabela:** R174CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |
| TabEve | TabEve |
| CodClc | CodClc |

