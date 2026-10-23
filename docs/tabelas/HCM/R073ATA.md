# R073ATA

## Descrição

Atividades do Aluno

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
| CodApf | Number(004,0) | Não | Código da Atividade |
| TmaAlu | Number(006,0) | Não | Turma da Atividade |
| DatIni | Date | Não | Data Inicial da Atividade |
| DatFim | Date | Sim | Data Final da Atividade |
| PerApf | String(001) | Sim | Período da Atividade |
| HorSeg | Number(004,0) | Sim | Código do Horário da Disciplina na Segunda-Feira |
| HorTer | Number(004,0) | Sim | Código do Horário da Disciplina na Terça-Feira |
| HorQua | Number(004,0) | Sim | Código do Horário da Disciplina na Quarta-Feira |
| HorQui | Number(004,0) | Sim | Código do Horário da Disciplina na Quinta-Feira |
| HorSex | Number(004,0) | Sim | Código do Horário da Disciplina na Sexta-Feira |
| HorSab | Number(004,0) | Sim | Código do Horário da Disciplina no Sábado |
| HorDom | Number(004,0) | Sim | Código do Horário da Disciplina no Domingo |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso |

---

## Chave Primária

- NumMat
- CodApf
- TmaAlu
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073ATA_000

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

### IR_R073ATA_001

**Tabela:** R171ATI

| Origem | Destino |
|--------|---------|
| CodApf | CodApf |

### IR_R073ATA_002

**Tabela:** R073TMA

| Origem | Destino |
|--------|---------|
| TmaAlu | TmaAlu |

