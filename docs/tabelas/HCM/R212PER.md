# R212PER

## Descrição

Entrevista de Desligamento - Perguntas

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 4

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
| ResSub | String(2999) | Sim | Resposta subjetiva (Questão subjetiva) |
| ValRes | Number(011,2) | Sim | Valor respondido (Questão quantitativa) |
| ValPes | Number(011,2) | Sim | Valor respondido com peso aplicado (Questão quantitativa) |
| DatRes | Date | Sim | Data respondida (Questão do tipo data) |
| ObsRes | String(2499) | Sim | Observação respondida (Questões com observação) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCom
- SeqEtv
- CodQue
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R212PER_003

**Tabela:** R212COM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatCom | DatCom |

### IR_R212PER_004

**Tabela:** R212ENT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatCom | DatCom |
| SeqEtv | SeqEtv |

### IR_R212PER_005

**Tabela:** R210QUE

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |

### IR_R212PER_006

**Tabela:** R210PER

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |
| CodPer | CodPer |

