# R172CND

## Descrição

Contas Colaborador - Contas p/ Nat. Despesa

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
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
| CodCon | String(030) | Sim | Código da conta contábil |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CodAux | Number(008,0) | Sim | Código da Conta Auxiliar da Conta Contábil Reduzida |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodClc
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R172CND_004

**Tabela:** R172CCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| TabEve | TabEve |
| CodClc | CodClc |

