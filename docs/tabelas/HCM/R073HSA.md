# R073HSA

## Descrição

Histórico de Situações de Alunos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
| DatIni | Date | Não | Data Inicial do Histórico de Situações do Aluno |
| HorIni | Number(005,0) | Não | Hora Inicial do Histórico de Situações do Aluno |
| DatFim | Date | Sim | Data Final do Histórico de Situações do Aluno |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico de Situações do Aluno |
| CodSta | Number(002,0) | Sim | Código da Situação do Aluno |

---

## Chave Primária

- NumMat
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073HSA_000

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

### IR_R073HSA_005

**Tabela:** R073STA

| Origem | Destino |
|--------|---------|
| CodSta | CodSta |

