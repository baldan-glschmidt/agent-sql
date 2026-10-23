# R164DES

## Descrição

BS - Despesas Assistência Médica

---

## Resumo

- Campos: 35
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpEmi | Date | Não | Competência da Despesa |
| SeqUni | Number(004,0) | Não | Sequência |
| CodOem | Number(008,0) | Sim | Código da Seguradora |
| CodPla | Number(003,0) | Sim | Código Plano |
| NumCon | Number(007,0) | Sim | Número do Contrato |
| NumMat | Number(008,0) | Sim | Número da Matrícula |
| DocDes | Number(012,0) | Sim | Número do Documento |
| CodSrv | Number(008,0) | Sim | Código do Serviço |
| DatEmi | Date | Sim | Data Atendimento |
| TipPse | Number(002,0) | Sim | Tipo do Prestador de Serviço |
| QtdSer | Number(002,0) | Sim | Quantidade de Serviços |
| HorMin | Number(005,0) | Sim | Hora e Minuto da Guia |
| CodEsp | Number(003,0) | Sim | Código Especialidade |
| DatInt | Date | Sim | Data Internação |
| DatAlt | Date | Sim | Data Alta |
| NroPar | Number(002,0) | Sim | Número de Parcelas |
| CmpIni | Date | Sim | Competência Início Desconto |
| CodDep | Number(002,0) | Sim | Sequência Dependente |
| NumFat | String(020) | Sim | Número da Fatura |
| NomPsv | String(040) | Sim | Nome do Prestador do Serviço |
| NomEsp | String(012) | Sim | Nome da Especialidade |
| SrvMed | String(080) | Sim | Descrição do Serviço de Assistência Médica |
| NomSol | String(030) | Sim | Nome do Solicitante |
| ParMed | String(001) | Sim | Participação Médica |
| AtoIex | String(001) | Sim | Atos Internos e Externos |
| TipDes | String(001) | Sim | Tipo Desconto Despesa |
| VlrChe | Number(011,2) | Sim | Valor C.H. |
| VlrSer | Number(011,2) | Sim | Valor do Serviço |
| VlrFil | Number(011,2) | Sim | Valor do Filme |
| ParEmp | Number(011,2) | Sim | Parte do Colaborador |
| ValSeg | Number(011,2) | Sim | Valor Segunda Via |
| ComRes | Date | Sim | Competência Cálculo Rescisão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpEmi
- SeqUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R164DES_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R164DES_006

**Tabela:** R164PLA

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |
| CodPla | CodPla |

