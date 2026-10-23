# R024ERA

## Descrição

Exceções de Requisitos Aperfeiçoamento de Cargo por Local

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| PesCua | Number(002,0) | Sim | OBSOLETO - Peso do Curso |
| ConRec | String(001) | Sim | Considera este requisito para recrutamento |
| ConPpp | String(001) | Sim | Considera requisito p/perfil profissiográfico previdenciário |
| EqvLnt | Number(004,0) | Sim | Grupo de Equivalência Específica para LNT |

---

## Chave Primária

- TabOrg
- NumLoc
- EstCar
- CodCar
- DatRqu
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024ERA_003

**Tabela:** R024ERL

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024ERA_005

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

