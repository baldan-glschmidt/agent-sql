# R178GER

## Descrição

Contas Totais - Contas Gerenciais

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
| FilCtb | Number(006,0) | Não | Filial Contábil |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| NatDes | Number(003,0) | Não | Natureza da despesa |
| ConGer | String(009) | Não | Conta gerencial |
| PerGer | Number(005,2) | Sim | Percentual |

---

## Chave Primária

- NumEmp
- FilCtb
- TabEve
- CodClc
- NatDes
- ConGer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R178GER_003

**Tabela:** R178CTO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| FilCtb | FilCtb |
| TabEve | TabEve |
| CodClc | CodClc |

