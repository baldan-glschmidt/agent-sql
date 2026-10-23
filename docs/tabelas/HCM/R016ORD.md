# R016ORD

## Descrição

Descrição do Local

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código da Tabela do Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| IteDes | Number(002,0) | Não | Código do Item |
| TexIte | String(1000) | Sim | Texto do Item |

---

## Chave Primária

- TabOrg
- NumLoc
- IteDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016ORD_001

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R016ORD_002

**Tabela:** R016IDL

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| IteDes | IteDes |

