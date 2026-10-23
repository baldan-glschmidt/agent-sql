# R016RAP

## Descrição

Requisitos por Local - Aperfeiçoamento

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número Empresa |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| PesCua | Number(002,0) | Sim | OBSOLETO - Peso do Curso |
| ConRec | String(001) | Sim | Considera este requisito para recrutamento |
| ConPpp | String(001) | Sim | Considera requisito p/perfil profissiográfico previdenciário |
| EqvLnt | Number(004,0) | Sim | Grupo de Equivalência Específica para LNT |

---

## Chave Primária

- NumEmp
- DatRqu
- TabOrg
- NumLoc
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016RAP_004

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

