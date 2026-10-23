# R134DCP

## Descrição

Calendário Cursos Treinamento - Instrutores (Pessoas)

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| DatCua | Date | Não | Data do Curso |
| SeqCua | Number(002,0) | Não | Sequência |
| CodPes | Number(009,0) | Não | Código da Pessoa |

---

## Chave Primária

- CodCua
- DatCua
- SeqCua
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134DCP_002

**Tabela:** R134DCL

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| DatCua | DatCua |
| SeqCua | SeqCua |

### IR_R134DCP_003

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

