# R111VAC

## Descrição

Vacinação - Aplicação da vacina

---

## Resumo

- Campos: 21
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| CodRem | Number(006,0) | Não | Código da vacina |
| DatSol | Date | Não | Data Solicitação do Exame |
| SeqDos | Number(004,0) | Não | Identificação da Dose |
| DatApl | Date | Sim | Data da aplicação da vacina |
| DatVen | Date | Sim | Data vencimento da vacina |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| ObsVac | String(800) | Sim | Anotações sobre a aplicação da vacina |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| SitVac | Number(001,0) | Sim | Define a situação da solicitação da vacina |
| CodCam | Number(004,0) | Sim | Código de identificação da campanha |
| SeqCam | Number(002,0) | Sim | Sequência da campanha |
| DatAte | Date | Sim | Data do Atendimento |
| HorAte | Number(005,0) | Sim | Hora do atendimento |
| NumVac | Number(009,0) | Sim | Nr. identificação da geração de solicitação |
| QtdApl | Number(010,4) | Sim | Quantidade de medicação aplicada |
| CodPos | Number(007,0) | Sim | Código do posto  de atendimento |
| IdeLot | String(020) | Sim | Identificação do lote |
| NumRec | Number(006,0) | Sim | Número da Receita Médica |
| FusHor | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- NumEmp
- CodFic
- CodRem
- DatSol
- SeqDos

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R111VAC_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R111VAC_002

**Tabela:** R110REM

| Origem | Destino |
|--------|---------|
| CodRem | CodRem |

