# R130DPA

## Descrição

Despesas da Turma - Participante

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Participante |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Participante |
| CodIdm | Number(003,0) | Sim | Código do Índice |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130DPA_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

