# R400PRO

## Descrição

Processos de Replicação

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
| CodPro | Number(003,0) | Não | Código do Processo |
| DesPro | String(040) | Sim | Descrição do Processo de Replicação |
| NivPri | Number(001,0) | Sim | Nível de Prioridade do Processo |
| DatIni | Date | Sim | Data de Início da Replicação |
| HorIni | Number(005,0) | Sim | Hora de Início da Replicação |
| DiaUti | String(001) | Sim | Executar o Processo Somente em Dias Úteis |
| PerExe | Number(001,0) | Sim | Periodicidade de Execução da Replicação |
| IntGer | Number(004,0) | Sim | Intervalo de Execução da Replicação |
| DatExe | Date | Sim | Data da Execução da Replicação |
| HorExe | Number(005,0) | Sim | Hora da Próxima Execução |
| DinExe | Date | Sim | Data de Início da Replicação |
| HinExe | Number(005,0) | Sim | Hora de Início da Execução da Replicação |
| StaPro | Number(001,0) | Sim | Status do Processo de Replicação |
| EmaRes | String(050) | Sim | E-mail do Responsável pelo Processo |
| CodAge | Number(009,0) | Sim | Código Processo Agendador |

---

## Chave Primária

- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
