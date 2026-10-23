# R090OAE

## Descrição

Alunos Envolvidos nas Ocorrências de Portaria

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Site da Ocorrência |
| DatOcP | Date | Não | Data da Ocorrência na Portaria |
| HorOcP | Number(005,0) | Não | Hora da Ocorrência na Portaria |
| SeqOcP | Number(002,0) | Não | Sequência da Ocorrência na Portaria |
| SeqEnv | Number(002,0) | Não | Sequência do Aluno Envolvido na Ocorrência na Portaria |
| NumMat | String(015) | Sim | Matrícula do Aluno |

---

## Chave Primária

- CodPlt
- DatOcP
- HorOcP
- SeqOcP
- SeqEnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090OAE_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R090OAE_005

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

