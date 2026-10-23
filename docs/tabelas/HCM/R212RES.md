# R212RES

## Descrição

Entrevista de Desligamento - Respostas

---

## Resumo

- Campos: 11
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa do Colaborador Desligado |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatCom | Date | Não | Data da Comunicação de Desligamento |
| SeqEtv | Number(002,0) | Não | Sequência da Entrevista |
| CodQue | Number(003,0) | Não | Código do Questionário respondido |
| CodPer | Number(003,0) | Não | Código da Pergunta respondida |
| CodRes | Number(002,0) | Não | Código da Resposta respondida |
| ResAss | String(001) | Sim | Identifica se a resposta foi assinalada |
| ValRes | Number(011,2) | Sim | Valor respondido (Questão do tipo prioridade) |
| ValPes | Number(011,2) | Sim | Valor respondido com peso aplicado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCom
- SeqEtv
- CodQue
- CodPer
- CodRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R212RES_003

**Tabela:** R212COM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatCom | DatCom |

### IR_R212RES_004

**Tabela:** R212ENT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatCom | DatCom |
| SeqEtv | SeqEtv |

### IR_R212RES_005

**Tabela:** R210QUE

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |

### IR_R212RES_006

**Tabela:** R210PER

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |
| CodPer | CodPer |

### IR_R212RES_007

**Tabela:** R210RES

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |
| CodPer | CodPer |
| CodRes | CodRes |

