# R073DPF

## Descrição

Disciplinas do Curso por Fases

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CurAlu | Number(003,0) | Não | Código do Curso |
| CodFas | Number(003,0) | Não | Código da Fase |
| CodDpf | Number(007,0) | Não | Código da Disciplina |
| TmaAlu | Number(006,0) | Não | Turma de Alunos |
| DesDFC | String(030) | Sim | Descrição Detalhada da Disciplina do Curso por Fase |
| PerDpf | String(001) | Sim | Período da Disciplina |
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

- CurAlu
- CodFas
- CodDpf
- TmaAlu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073DPF_000

**Tabela:** R073CUR

| Origem | Destino |
|--------|---------|
| CurAlu | CurAlu |

### IR_R073DPF_001

**Tabela:** R073FCU

| Origem | Destino |
|--------|---------|
| CurAlu | CurAlu |
| CodFas | CodFas |

### IR_R073DPF_002

**Tabela:** R171DIS

| Origem | Destino |
|--------|---------|
| CodDpf | CodDpf |

### IR_R073DPF_003

**Tabela:** R073TMA

| Origem | Destino |
|--------|---------|
| TmaAlu | TmaAlu |

