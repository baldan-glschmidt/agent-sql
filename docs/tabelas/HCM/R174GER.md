# R174GER

## Descrição

Contas C. Custo - Contas Gerenciais

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
| CodCcu | String(018) | Não | Código do C.Custo Contábil |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| NatDes | Number(003,0) | Não | Natureza da despesa |
| ConGer | String(009) | Não | Conta gerencial |
| PerGer | Number(005,2) | Sim | Percentual da conta gerencial |

---

## Chave Primária

- NumEmp
- CodCcu
- TabEve
- CodClc
- NatDes
- ConGer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R174GER_003

**Tabela:** R174CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |
| TabEve | TabEve |
| CodClc | CodClc |

