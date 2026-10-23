# R128CUN

## Descrição

Cursos Aperfeiçoamento - Notas

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso |
| CodTnt | Number(003,0) | Não | Item de Nota do Curso |
| SeqCua | Number(003,0) | Sim | Sequência para avaliação |
| PesNot | Number(002,0) | Sim | Peso da Nota do Curso |

---

## Chave Primária

- CodCua
- CodTnt

---

## Índices

### R128CUNIndice2

**Tipo:** Não unico

Campos:
- CodCua
- SeqCua
- CodTnt

---

## Relacionamentos

### IR_R128CUN_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128CUN_001

**Tabela:** R140NTR

| Origem | Destino |
|--------|---------|
| CodTnt | CodTnt |

