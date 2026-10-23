# R134DCI

## Descrição

Calendário Cursos Treinamento - Instrutores

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| DatCua | Date | Não | Data do Curso |
| SeqCua | Number(002,0) | Não | Sequência |
| NumEmp | Number(004,0) | Não | Código da Empresa do Instrutor |
| TipCol | Number(001,0) | Não | Tipo de Instrutor |
| NumCad | Number(009,0) | Não | Cadastro do Instrutor |

---

## Chave Primária

- CodCua
- DatCua
- SeqCua
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134DCI_002

**Tabela:** R134DCL

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| DatCua | DatCua |
| SeqCua | SeqCua |

### IR_R134DCI_005

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

