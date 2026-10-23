# R016RFO

## Descrição

Requisitos por Local - Formação

---

## Resumo

- Campos: 10
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
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| PesCuf | Number(002,0) | Sim | OBSOLETO - Peso do Curso |
| SitCuf | Number(001,0) | Sim | Situação do Curso |
| ConRec | String(001) | Sim | Considera este requisito para recrutamento |
| ConPpp | String(001) | Sim | Considera requisito p/perfil profissiográfico previdenciário |
| EqvLnt | Number(004,0) | Sim | Grupo de Equivalência Específica para LNT |

---

## Chave Primária

- NumEmp
- DatRqu
- TabOrg
- NumLoc
- CodCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016RFO_004

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

