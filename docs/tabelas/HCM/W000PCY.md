# W000PCY

## Descrição

Tabela para manutenção de pendências de processos do workflow

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| PRCSTP | Number(008,0) | Não | Passo do processo onde a atividade foi executada |
| ACTVID | Number(005,0) | Não | Identificador da atividade que gerou a pendência dona desta delegação |
| USURES | Number(010,0) | Sim | Usuário ou grupo responsável pela pendência |
| PRCNAM | String(255) | Sim | Nome do processo de workflow |
| PCYDES | String(255) | Sim | Descrição da pendência |
| PCYHNT | String(4000) | Sim | Hint para pendência |
| PCYDAT | Image | Sim | Dados da pendência controlados pelo Performer |
| PERFID | Number(003,0) | Sim | Identificador do performer para a pendência |
| INIDAT | Date | Sim | Data de criação da pendencia |
| INITIM | Number(005,0) | Sim | Tempo da criação da pendências |
| UPDDAT | Date | Sim | Data da última alteração da pendencia |
| UPDTIM | Number(005,0) | Sim | Tempo da última alteração na pendência |
| EXPDAT | Date | Sim | Data de expiração da pendencia |
| EXPTIM | Number(005,0) | Sim | Tempo para a expiração da pendência |
| PROCID | Number(005,0) | Sim | Identificador único do processo de workflow |
| PRCVER | Number(005,0) | Sim | Versão do processo |
| PRIKEY | String(030) | Sim |  |

---

## Chave Primária

- PRCIID
- PRCSTP
- ACTVID

---

## Índices

### W000PCYIndice01

**Tipo:** Não unico

Campos:
- USURES
- PRCNAM

---

## Relacionamentos

Nenhum relacionamento cadastrado.
