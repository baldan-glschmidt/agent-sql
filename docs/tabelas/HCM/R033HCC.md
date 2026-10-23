# R033HCC

## Descrição

Histórico de Competências da Pessoa - Itens calculados

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| SeqHis | Number(008,0) | Não | Sequencia para identificar o histórico |
| SeqHcc | Number(004,0) | Não | Sequência do item |
| TpIMed | Number(001,0) | Sim | Tipo de item |
| CodCua | Number(009,0) | Sim | Curso de aperfeiçoamento |
| CodCuf | Number(004,0) | Sim | Curso de formação |
| TipExp | String(001) | Sim | Tipo Experiência (anos/meses) |
| ExpCar | Number(002,0) | Sim | Experiência |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Cargo |
| NumEmp | Number(004,0) | Sim | Empresa do colaborador |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Colaborador |
| CodCic | Number(003,0) | Sim | Ciclo de avaliação |
| IdeAva | Number(005,0) | Sim | Identificador da avaliação de competências |
| NomTag | String(1000) | Sim | Tag |

---

## Chave Primária

- CodPes
- SeqHis
- SeqHcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033HCC_001

**Tabela:** R033HCP

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |
| SeqHis | SeqHis |

