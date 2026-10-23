# R073RES

## Descrição

Responsáveis do Aluno

---

## Resumo

- Campos: 20
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento do Responsável |
| NumDoc | String(020) | Não | Número do Documento do Responsável |
| NomRes | String(050) | Sim | Nome do Responsável |
| FonRes | String(020) | Sim | Telefone do Responsável do Aluno |
| EmaRes | String(050) | Sim | E-mail Responsável Aluno |
| CodPrm | Number(005,0) | Sim | Permissão Dias Normais do Responsável |
| PrmFer | Number(005,0) | Sim | Permissão Feriado Responsável |
| PrmSab | Number(005,0) | Sim | Permissão Sábado Responsável |
| PrmDom | Number(005,0) | Sim | Permissão Domingo Responsável |
| CodHor | Number(004,0) | Sim | Horário Dias Normais Responsável |
| HorSab | Number(004,0) | Sim | Horário Sábado Responsável |
| HorDom | Number(004,0) | Sim | Horário Domingo Responsável |
| ConTpm | String(001) | Sim | Controla tempo de permanência |
| ConRee | String(001) | Sim | Controla Tempo Mínimo de Reentrada |
| UsaBio | Number(001,0) | Sim | Utiliza Controle Biométrico |
| GraCon | Number(003,0) | Sim | Grau de Conferência na Biometria |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| ConAdp | String(001) | Sim | Controla Nível e  Anti-Dupla |
| UsaRFa | String(001) | Sim | Utiliza Reconhecimento Facial |

---

## Chave Primária

- TipDoc
- NumDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
