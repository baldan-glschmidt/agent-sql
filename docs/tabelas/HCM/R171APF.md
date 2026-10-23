# R171APF

## Descrição

Professores - Atividades

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
| SeqApf | Number(005,0) | Não | Sequência da Atividade |
| DatFim | Date | Sim | Data de Término da Atividade |
| CodApf | Number(004,0) | Sim | Código da Atividade |
| CodRat | Number(009,0) | Sim | Código do Rateio |
| MarPto | String(001) | Sim | Marca Ponto (S,N) |
| HorMes | Number(010,0) | Sim | Horas Mensais p/ Fechamento na Folha |
| HorMno | Number(010,0) | Sim | Horas Mês Noturna do Professor |
| HorSem | Number(010,0) | Sim | Horas Semana do Professor |
| HorSno | Number(010,0) | Sim | Horas Semana Noturna do Professor |
| HorSeg | Number(004,0) | Sim | Código do Horário da Atividade na Segunda-Feira |
| HorTer | Number(004,0) | Sim | Código do Horário da Atividade na Terça-Feira |
| HorQua | Number(004,0) | Sim | Código do Horário da Atividade na Quarta-Feira |
| HorQui | Number(004,0) | Sim | Código do Horário da Atividade na Quinta-Feira |
| HorSex | Number(004,0) | Sim | Código do Horário da Atividade na Sexta-Feira |
| HorSab | Number(004,0) | Sim | Código do Horário da Atividade no Sábado |
| HorDom | Number(004,0) | Sim | Código do Horário no Domingo |
| EstSal | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| RefApf | Number(011,2) | Sim | Referência da Atividade p/ Folha |
| ValApf | Number(011,2) | Sim | Valor da Atividade p/ Folha |
| OriApf | String(001) | Sim | Origem da Atividade |
| ObsApf | String(400) | Sim | Observação da Atividade do Professor |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- SeqApf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R171APF_006

**Tabela:** R171ATI

| Origem | Destino |
|--------|---------|
| CodApf | CodApf |

