# R073DIA

## Descrição

Disciplinas do Aluno

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
| CurAlu | Number(003,0) | Não | Código do Curso |
| CodFas | Number(003,0) | Não | Código da Fase |
| CodDpf | Number(007,0) | Não | Código da Disciplina |
| TmaAlu | Number(006,0) | Não | Turma da Disciplina |
| DatIni | Date | Não | Data Inicial do Estudo na Disciplina |
| DatFim | Date | Sim | Data Final de Estudo na Disciplina |

---

## Chave Primária

- NumMat
- CurAlu
- CodFas
- CodDpf
- TmaAlu
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073DIA_000

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

### IR_R073DIA_001

**Tabela:** R073CUR

| Origem | Destino |
|--------|---------|
| CurAlu | CurAlu |

### IR_R073DIA_002

**Tabela:** R073FCU

| Origem | Destino |
|--------|---------|
| CurAlu | CurAlu |
| CodFas | CodFas |

### IR_R073DIA_003

**Tabela:** R171DIS

| Origem | Destino |
|--------|---------|
| CodDpf | CodDpf |

### IR_R073DIA_004

**Tabela:** R073DPF

| Origem | Destino |
|--------|---------|
| CurAlu | CurAlu |
| CodFas | CodFas |
| CodDpf | CodDpf |
| TmaAlu | TmaAlu |

