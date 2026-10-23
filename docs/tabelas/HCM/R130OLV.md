# R130OLV

## Descrição

Orçamento Local - Vagas p/ Mês

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
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| AnoBas | Number(004,0) | Não | Ano Base do Orçamento |
| MesBas | Number(002,0) | Não | Mês Base do Orçamento |
| QtdVag | Number(006,0) | Sim | Quantidade de Vagas |
| ValOrc | Number(011,2) | Sim | Valor do Orçamento |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- AnoBas
- MesBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130OLV_003

**Tabela:** R130OLO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| AnoBas | AnoBas |

