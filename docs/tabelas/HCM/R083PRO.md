# R083PRO

## Descrição

PPRA - Produtos Químicos

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodGru | Number(007,0) | Não | Grupo de Atividades |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodPro | Number(006,0) | Não | Código do Produto Químico |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- CodAgt
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083PRO_004

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGru | CodAtv |

### IR_R083PRO_005

**Tabela:** R083AGT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpa | CmpPpa |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodGru | CodGru |
| CodAgt | CodAgt |

### IR_R083PRO_006

**Tabela:** R082PRO

| Origem | Destino |
|--------|---------|
| CodPro | CodPro |

