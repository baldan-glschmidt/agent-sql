# R134DTN

## Descrição

Turmas - Notas

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodTnt | Number(003,0) | Não | Item de Nota do Curso |
| SeqCua | Number(003,0) | Sim | Sequência para avaliação |
| PesNot | Number(002,0) | Sim | Peso da Nota do Curso |

---

## Chave Primária

- CodCua
- TmaCua
- CodTnt

---

## Índices

### R134DTNIndice2

**Tipo:** Não unico

Campos:
- CodCua
- TmaCua
- SeqCua
- CodTnt

---

## Relacionamentos

### IR_R134DTN_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134DTN_002

**Tabela:** R140NTR

| Origem | Destino |
|--------|---------|
| CodTnt | CodTnt |

