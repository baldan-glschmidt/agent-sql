# R034RAP

## Descrição

Requisitos Colaborador - Cursos Aperfeiçoamento

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatRqu | Date | Não | Data de início do requisito |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| DatTer | Date | Sim | Data de término do requisito |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatRqu
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034RAP_004

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

