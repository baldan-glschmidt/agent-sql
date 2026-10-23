# R005LIN

## Descrição

Linhas de ônibus

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodLin | Number(004,0) | Não | Linha de ônibus |
| DesLin | String(060) | Sim | Descrição da linha de ônibus |
| CodTrm | Number(002,0) | Sim | Código do Terminal |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Sim | Local do Organograma |

---

## Chave Primária

- NumEmp
- CodLin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005LIN_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R005LIN_004

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R005LIN_005

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

