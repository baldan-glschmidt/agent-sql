# R134DCH

## Descrição

Calendário Cursos Treinamento - Horário

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
| CodCua | Number(009,0) | Não | Código do Curso |
| DatCua | Date | Não | Data do Curso |
| SeqCua | Number(002,0) | Não | Sequência do Curso p/ Mesma Data |
| CodHcu | Number(006,0) | Não | Código do Horário Cursos |

---

## Chave Primária

- CodCua
- DatCua
- SeqCua
- CodHcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134DCH_002

**Tabela:** R134DCL

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| DatCua | DatCua |
| SeqCua | SeqCua |

### IR_R134DCH_003

**Tabela:** R133HCU

| Origem | Destino |
|--------|---------|
| CodHcu | CodHcu |

