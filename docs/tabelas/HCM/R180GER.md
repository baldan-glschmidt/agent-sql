# R180GER

## Descrição

Contas O. Empresa - Contas Gerenciais

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodOem | Number(008,0) | Não | Código da outra empresa |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| NatDes | Number(003,0) | Não | Natureza da despesa |
| CodGer | String(009) | Não | Código da conta gerencial |
| PerGer | Number(005,2) | Sim | Percentual da conta gerencial |

---

## Chave Primária

- NumEmp
- CodOem
- TabEve
- CodClc
- NatDes
- CodGer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R180GER_003

**Tabela:** R180COE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodOem | CodOem |
| TabEve | TabEve |
| CodClc | CodClc |

