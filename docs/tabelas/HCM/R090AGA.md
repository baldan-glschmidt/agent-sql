# R090AGA

## Descrição

Agendamento de Visitantes - Acompanhantes

---

## Resumo

- Campos: 27
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatPrv | Date | Não | Data Prevista da Visita |
| HorPrv | Number(005,0) | Não | Hora Prevista da Visita |
| NumEmp | Number(004,0) | Não | Código da Empresa do Visitado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador Visitado |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Visitado |
| SeqAgv | Number(002,0) | Não | Sequência do Agendamento |
| SeqAco | Number(002,0) | Não | Sequência do Acompanhamento |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Acompanhante |
| NumDoc | String(020) | Sim | Número do Documento do Acompanhante |
| NomAco | String(040) | Sim | Nome do Acompanhante |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| NomOem | String(060) | Sim | Nome da Empresa do Acompanhante |
| StaPng | Number(001,0) | Sim | Status do Agendamento |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| EstCid | String(002) | Sim | Estado do Orgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| ObsAco | String(080) | Sim | Observação do Acompanhante |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| SegTDo | Number(001,0) | Sim | Segundo Tipo do Documento do Visitante |
| SegDoc | String(020) | Sim | Segundo Número do Documento do Visitante |
| NomDoc | String(040) | Sim | Nome do acompanhante no documento |
| DatNas | Date | Sim | Data de Nascimento |
| FunVis | String(060) | Sim | Função do visitante na empresa representada |
| QuaVis | String(060) | Sim | Qualificação do visitante na empresa representada |
| DvaDoc | Date | Sim | Data de Validade (Passaporte) |
| PaiDoc | Number(004,0) | Sim | País de Emissão (Passaporte) |
| TipSex | String(001) | Sim | Sexo do Visitante |

---

## Chave Primária

- DatPrv
- HorPrv
- NumEmp
- TipCol
- NumCad
- SeqAgv
- SeqAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090AGA_005

**Tabela:** R090AGV

| Origem | Destino |
|--------|---------|
| DatPrv | DatPrv |
| HorPrv | HorPrv |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| SeqAgv | SeqAgv |

