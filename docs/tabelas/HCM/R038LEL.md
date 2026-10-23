# R038LEL

## Descrição

Local de Entrega por Local

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| DatAlt | Date | Não | Data da Alteração |
| CodLen | Number(004,0) | Sim | Novo Local Entrega |
| DatExc | Date | Sim | Data da Exclusão |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038LEL_001

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

