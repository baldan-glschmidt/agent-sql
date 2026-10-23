# R083NLE

## Descrição

PPRA - Possíveis Danos

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodGru | Number(007,0) | Não | Grupo de Atividades |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodNle | Number(003,0) | Não | Possível Dano à Saúde |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- CodAgt
- CodNle

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083NLE_004

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGru | CodAtv |

### IR_R083NLE_005

**Tabela:** R083AGT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpa | CmpPpa |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodGru | CodGru |
| CodAgt | CodAgt |

### IR_R083NLE_006

**Tabela:** R086NLE

| Origem | Destino |
|--------|---------|
| CodNle | CodNle |

