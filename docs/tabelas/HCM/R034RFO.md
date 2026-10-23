# R034RFO

## Descrição

Requisitos Colaborador - Cursos Formação

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatRqu | Date | Não | Data de início do requisito |
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| SitCuf | Number(001,0) | Sim | Situação do Curso |
| DatTer | Date | Sim | Data de término do requisito |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatRqu
- CodCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034RFO_004

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

