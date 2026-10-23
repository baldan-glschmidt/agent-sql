# R134INP

## Descrição

Turmas - Instrutores (Pessoas)

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| ObsIns | String(500) | Sim | Dados complementares do instrutor |
| TipIns | Number(001,0) | Sim | Indica se o colaborador é instrutor, avaliador ou ambos |

---

## Chave Primária

- CodCua
- TmaCua
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134INP_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134INP_002

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

