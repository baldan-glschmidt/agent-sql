# R083CAR

## Descrição

PPRA - Cargos

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodGru | Number(007,0) | Não | Grupo de Atividades |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- EstCar
- CodCar

---

## Índices

### R083CARIndice2

**Tipo:** Unico

Campos:
- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- EstCar
- CodCar
- CodGru

---

## Relacionamentos

### IR_R083CAR_003

**Tabela:** R083ARI

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpa | CmpPpa |
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R083CAR_004

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGru | CodAtv |

