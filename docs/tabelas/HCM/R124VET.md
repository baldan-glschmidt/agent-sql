# R124VET

## Descrição

Colaborador - Vínculo de etapas

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Candidato |
| CodRqu | Number(009,0) | Não | Código Requisição |
| CodEta | Number(003,0) | Não | Código Etapa |
| SeqEta | Number(003,0) | Não | Sequência Etapa |
| TabVin | Number(001,0) | Sim | Nome da tabela vinculada com a etapa do candidato |
| DatHpa | Date | Sim | Data do Parecer |
| SeqHsu | Number(002,0) | Sim | Sequência de entrevistas |
| DatHla | Date | Sim | Data do Laudo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodGav | Number(003,0) | Sim | Código do Grupo de Avaliação |
| DatGra | Date | Sim | Data Resultado Avaliação |
| CodGrq | Number(003,0) | Sim | Código do Grupo Questionário |
| DatGrq | Date | Sim | Data da Resposta Questionário |
| DatCom | Date | Sim | Data da comunicação com o Candidato |
| HorCom | Number(005,0) | Sim | Hora da comunicação com o Candidato |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodRqu
- CodEta
- SeqEta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124VET_005

**Tabela:** R124HET

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodRqu | CodRqu |
| CodEta | CodEta |
| SeqEta | SeqEta |

