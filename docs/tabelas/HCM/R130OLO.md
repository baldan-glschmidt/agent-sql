# R130OLO

## Descrição

Orçamento Local

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Não | Código do Local |
| AnoBas | Number(004,0) | Não | Ano Base do Orçamento |
| CodIdm | Number(003,0) | Sim | Código do Índice Conversão |
| TipOrc | Number(001,0) | Sim | Tipo de Orçamento |
| CodUsu | Number(010,0) | Sim | Código do Usuário que gerou o Orçamento |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Responsável |
| ObsCur | String(200) | Sim | Observações |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- AnoBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130OLO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R130OLO_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

