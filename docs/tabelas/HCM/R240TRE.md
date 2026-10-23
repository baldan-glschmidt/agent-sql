# R240TRE

## Descrição

Analytics SeniorX - Treinamentos

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCua | Number(009,0) | Não | Código do Curso |
| PerIni | Date | Não | Data Inicial |
| PerFim | Date | Sim | Data Final |
| SeqHcr | Number(004,0) | Sim | Sequência do Curso Aperfeiçoamento |
| TmaCua | Number(006,0) | Sim | Código da Turma relacionada ao histórico |
| TipTre | Number(001,0) | Sim | Tipo Treinamento |
| NomRed | String(060) | Sim | Nome Treinamento |
| MedCua | Number(005,2) | Sim | Média |
| FreCua | Number(005,2) | Sim | Frequência |
| CarHor | Number(010,0) | Sim | Carga Horária |
| SitCua | Number(002,0) | Sim | Situação |
| SitIns | Number(001,0) | Sim | Situação da Inscrição |
| CodEvn | Number(009,0) | Sim | Código do Evento |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última geração |
| DthAlt | Number(014,6) | Sim | Data/Hora em que foi realizada a última geração |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCua
- PerIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R240TRE_003

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

