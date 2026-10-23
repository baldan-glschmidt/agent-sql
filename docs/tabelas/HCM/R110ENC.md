# R110ENC

## Descrição

Encaminhamentos

---

## Resumo

- Campos: 23
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Medica |
| DatEnc | Date | Não | Data Encaminhamento |
| HorEnc | Number(005,0) | Não | Hora do Encaminhamento |
| SeqEnc | Number(003,0) | Não | Sequência do Encaminhamento |
| AreEnc | Number(004,0) | Sim | Código da Área de Atuação do Solicitante |
| CodEnc | Number(003,0) | Sim | Tipo de Encaminhamento |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| CvnMed | Number(008,0) | Sim | Código do Convênio Médico |
| DatMar | Date | Sim | Data Marcada |
| HorMar | Number(005,0) | Sim | Hora Marcada |
| DatRes | Date | Sim | Data Resultado |
| HorRes | Number(005,0) | Sim | Hora Resultado |
| OemEnc | Number(008,0) | Sim | Código da Outra Empresa a ser Encaminhado |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| ObsSol | String(2000) | Sim | Anotações do Solicitante |
| ObsAte | String(2000) | Sim | Anotações do Atendimento |
| SitEnc | Number(001,0) | Sim | Situação do encaminhamento |
| AteEnc | Number(006,0) | Sim | Código do Atendente Encaminhado |
| AreAte | Number(004,0) | Sim | Código da Área de Atuação do Encaminhado |
| IndAge | String(001) | Sim | Houve Agendamento |
| PosSol | Number(007,0) | Sim | Código do posto de atendimento do Solicitante |
| PosEnc | Number(007,0) | Sim | Código do posto de atendimento do Encaminhado |

---

## Chave Primária

- NumEmp
- CodFic
- DatEnc
- HorEnc
- SeqEnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110ENC_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110ENC_005

**Tabela:** R108ARE

| Origem | Destino |
|--------|---------|
| AreEnc | AreAte |

### IR_R110ENC_006

**Tabela:** R108TEN

| Origem | Destino |
|--------|---------|
| CodEnc | CodEnc |

### IR_R110ENC_007

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

