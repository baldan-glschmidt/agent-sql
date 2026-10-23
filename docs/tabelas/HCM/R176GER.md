# R176GER

## Descrição

Contas Local - Contas Gerenciais

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| NatDes | Number(003,0) | Não | Natureza da despesa |
| ConGer | String(009) | Não | Código da conta gerencial |
| PerGer | Number(005,2) | Sim | Percentual da conta gerencial |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- TabEve
- CodClc
- NatDes
- ConGer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R176GER_004

**Tabela:** R176CLO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| TabEve | TabEve |
| CodClc | CodClc |

