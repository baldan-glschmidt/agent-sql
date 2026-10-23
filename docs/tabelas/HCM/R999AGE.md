# R999AGE

## Descrição

Agendador - Programação de processos automáticos

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CODPRO | Number(009,0) | Não | Código do processo |
| TIPPER | Number(001,0) | Sim | Tipo de periodicidade |
| DATINI | Date | Sim | Data inicial |
| HORINI | Number(005,0) | Sim | Hora inicial |
| INTERV | Number(002,0) | Sim | Intervalo de execução |
| ENABLE | String(001) | Sim | Processo habilitado / desabilitado |
| DATVAL | Date | Sim | Data de validade do processo |
| EXEATR | String(001) | Sim | Executa atrasada |
| COMPLE | String(599) | Sim | Complemento - Armazena dados relativos ao tipo de periodicidade |
| DATULT | Date | Sim | Data da última execução |
| HORULT | Number(005,0) | Sim | Hora da última execução |
| FUSO | Number(003,0) | Sim | Fuso horário do processo |
| HORVER | String(001) | Sim | Utiliza horário de verão |
| EXEINI | Number(004,0) | Sim | Horário de início da Janela de Execução |
| EXEEND | Number(004,0) | Sim | Horário final da Janela de Execução |

---

## Chave Primária

- CODPRO

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
