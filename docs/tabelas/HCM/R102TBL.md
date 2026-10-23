# R102TBL

## Descrição

Trabalhos do SESMT - Áreas Relacionadas Organograma

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTbr | Number(006,0) | Não | Código do Trabalho |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |

---

## Chave Primária

- NumEmp
- CodTbr
- TabOrg
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102TBL_001

**Tabela:** R102TBR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodTbr | CodTbr |

### IR_R102TBL_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

