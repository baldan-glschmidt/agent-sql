# R171DPF

## Descrição

Professores - Disciplinas

---

## Resumo

- Campos: 27
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatIni | Date | Não | Data de Início da Atividade |
| SeqDpf | Number(005,0) | Não | Sequência da Disciplina |
| DatFim | Date | Sim | Data de Término da Atividade |
| CodDpf | Number(007,0) | Sim | Código da Disciplina |
| CodRat | Number(009,0) | Sim | Código do Rateio |
| MarPto | String(001) | Sim | Marca Ponto (S,N) |
| HorMes | Number(010,0) | Sim | Horas Mensais p/ Fechamento na Folha |
| HorMno | Number(010,0) | Sim | Horas Mês Noturna do Professor |
| HorSem | Number(010,0) | Sim | Horas Semana do Professor |
| HorSno | Number(010,0) | Sim | Horas Semana Noturna do Professor |
| HorSeg | Number(004,0) | Sim | Código do Horário da Disciplina na Segunda-Feira |
| HorTer | Number(004,0) | Sim | Código do Horário da Disciplina na Terça-Feira |
| HorQua | Number(004,0) | Sim | Código do Horário da Disciplina na Quarta-Feira |
| HorQui | Number(004,0) | Sim | Código do Horário da Disciplina na Quinta-Feira |
| HorSex | Number(004,0) | Sim | Código do Horário da Disciplina na Sexta-Feira |
| HorSab | Number(004,0) | Sim | Código do Horário da Disciplina no Sábado |
| HorDom | Number(004,0) | Sim | Código do Horário da Disciplina no Domingo |
| EstSal | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| RefDpf | Number(011,2) | Sim | Referência da Disciplina p/ Folha |
| ValDpf | Number(011,2) | Sim | Valor da Disciplina p/ Folha |
| OriDpf | String(001) | Sim | Origem da Disciplina |
| ObsDpf | String(400) | Sim | Observação da Disciplina do Professor |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- SeqDpf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R171DPF_006

**Tabela:** R171DIS

| Origem | Destino |
|--------|---------|
| CodDpf | CodDpf |

