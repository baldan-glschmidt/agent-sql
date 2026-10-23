# R090ACO_AUD

## Descrição

Auditoria Acompanhantes do Visitante

---

## Resumo

- Campos: 25
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| DatEnt | Date | Não | Data de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Entrada |
| SeqEnt | Number(002,0) | Não | Sequência do Registro |
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatSLo | Date | Sim | Data da Saída do Local Visitado na Empresa |
| HorSLo | Number(005,0) | Sim | Hora da Saída do Local Visitado na Empresa |
| DatSai | Date | Sim | Data da Saída da Empresa |
| HorSai | Number(005,0) | Sim | Hora da Saída da Empresa |
| AssVid | String(001) | Sim | Assistiu Vídeo de Segurança |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| EstCid | String(002) | Sim | Estado do Orgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| SegTDo | Number(001,0) | Sim | Segundo Tipo do Documento do Visitante |
| SegDoc | String(020) | Sim | Segundo Número do Documento do Visitante |
| DatNas | Date | Sim | Data de Nascimento |
| FunVis | String(060) | Sim | Função do visitante na empresa representada |
| QuaVis | String(060) | Sim | Qualificação do visitante na empresa representada |
| DvaDoc | Date | Sim | Data de Validade (Passaporte) |
| PaiDoc | Number(004,0) | Sim | País de Emissão (Passaporte) |
| TipSex | String(001) | Sim | Sexo do Visitante |

---

## Chave Primária

- SeqReg
- VerSeq
- DatEnt
- HorEnt
- SeqEnt
- TipDoc
- NumDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
