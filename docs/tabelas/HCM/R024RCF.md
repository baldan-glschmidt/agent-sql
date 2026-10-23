# R024RCF

## Descrição

Requisitos Cargo - Cursos Formação

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| PesCuf | Number(002,0) | Sim | OBSOLETO - Peso do Curso |
| SitCuf | Number(001,0) | Sim | Situação do Curso |
| ConRec | String(001) | Sim | Considera este requisito para recrutamento |
| ConPpp | String(001) | Sim | Considera requisito p/perfil profissiográfico previdenciário |
| EqvLnt | Number(004,0) | Sim | Grupo de Equivalência Específica para LNT |
| EqvTri | Number(004,0) | Sim | Grupo de Equivalência Específica para Triagem/Seletiva |
| PtsRcf | Number(002,0) | Sim | Pontuação do Curso de Formação |

---

## Chave Primária

- EstCar
- CodCar
- DatRqu
- CodCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024RCF_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024RCF_003

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

