# R122VET

## Descrição

Candidatos Externos - Vínculo de etapas

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| CodRqu | Number(009,0) | Não | Código Requisição |
| CodEta | Number(003,0) | Não | Código Etapa |
| SeqEta | Number(003,0) | Não | Sequência Etapa |
| TabVin | Number(001,0) | Sim | Nome da tabela vinculada com a etapa do candidato |
| DatCpa | Date | Sim | Data Parecer Candidato |
| SeqCsu | Number(002,0) | Sim | Sequência de entrevistas |
| DatCla | Date | Sim | Data do Laudo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodGav | Number(003,0) | Sim | Código do Grupo de Avaliação |
| DatGra | Date | Sim | Data da Avaliação do Grupo |
| CodGrq | Number(003,0) | Sim | Código do Grupo |
| DatCom | Date | Sim | Data da comunicação com o Candidato |
| HorCom | Number(005,0) | Sim | Hora da comunicação com o Candidato |

---

## Chave Primária

- NumCan
- CodRqu
- CodEta
- SeqEta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122VET_003

**Tabela:** R122CET

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |
| CodRqu | CodRqu |
| CodEta | CodEta |
| SeqEta | SeqEta |

