# R024RCA

## Descrição

Requisitos Cargo - Cursos Aperfeiçoamento

---

## Resumo

- Campos: 13
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
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| PesCua | Number(002,0) | Sim | OBSOLETO - Peso do curso |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| ConRec | String(001) | Sim | Considera este requisito para recrutamento |
| ConPpp | String(001) | Sim | Considera requisito p/perfil profissiográfico previdenciário |
| EqvLnt | Number(004,0) | Sim | Grupo de Equivalência Específica para LNT |
| EqvTri | Number(004,0) | Sim | Grupo de Equivalência Específica para Triagem/Seletiva |
| PtsRca | Number(002,0) | Sim | Pontuação do Curso de Aperfeiçoamento |

---

## Chave Primária

- EstCar
- CodCar
- DatRqu
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024RCA_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024RCA_003

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

