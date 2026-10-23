# R212ENT

## Descrição

Entrevista de Desligamento - Entrevistas

---

## Resumo

- Campos: 19
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa do Colaborador Desligado |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatCom | Date | Não | Data da Comunicação de Desligamento |
| SeqEtv | Number(002,0) | Não | Sequência da Entrevista |
| DatEtv | Date | Sim | Data da Entrevista |
| DatLim | Date | Sim | Data Limite para responder o questionário |
| TpoEtv | Number(002,0) | Sim | Tipo da Entrevista |
| EmpEtv | Number(004,0) | Sim | Código da empresa do colaborador entrevistado |
| TipEtv | Number(001,0) | Sim | Tipo de colaborador entrevistado |
| CadEtv | Number(009,0) | Sim | Cadastro do colaborador entrevistado |
| CodQue | Number(003,0) | Sim | Código do Questionário |
| EmpRes | Number(004,0) | Sim | Código da empresa do responsável pela entrevista |
| TipRes | Number(001,0) | Sim | Tipo de colaborador responsável pela entrevista |
| CadRes | Number(009,0) | Sim | Cadastro do responsável pela entrevista |
| SitEtv | Number(001,0) | Sim | Situação da entrevista |
| CodRmd | Number(003,0) | Sim | Código do Motivo da Demissão |
| CauDem | Number(002,0) | Sim | Causa da Demissão |
| EtvWeb | String(001) | Sim | Entrevistado responde via WEB |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCom
- SeqEtv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R212ENT_003

**Tabela:** R212COM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatCom | DatCom |

### IR_R212ENT_011

**Tabela:** R210QUE

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |

