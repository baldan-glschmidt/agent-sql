# R172GER

## Descrição

Contas Colaborador - Contas Gerenciais

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo do colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código de lançamento contábil |
| NatDes | Number(003,0) | Não | Natureza da despesa |
| ConGer | String(009) | Não | Código da conta gerencial |
| PerGer | Number(005,2) | Sim | Percentual da conta gerencial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodClc
- NatDes
- ConGer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R172GER_004

**Tabela:** R172CCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| TabEve | TabEve |
| CodClc | CodClc |

