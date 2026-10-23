# W200PCY

## Descrição

Tabela para histórico de execução de pendências de processos de workflow

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| PRCSTP | Number(008,0) | Não | Passo do processo onde a atividade foi executada |
| ACTVID | Number(005,0) | Não | Identificador da atividade que gerou a pendência dona desta delegação |
| ACTNAM | String(255) | Sim | Nome da atividade |
| INIDAT | Date | Sim | Data de criação da pendência |
| INITIM | Number(005,0) | Sim | Tempo da criação da pendência |
| ENDDAT | Date | Sim | Data da conclusão da pendência |
| ENDTIM | Number(005,0) | Sim | Tempo da conclusão da pendência |
| USURES | Number(010,0) | Sim | Usuário/grupo responsável inicial da pendência |
| USUEXE | Number(010,0) | Sim | Código do usuário que tratou a pendência |
| EXPDAT | Date | Sim | Data de expiração da pendência |
| EXPTIM | Number(005,0) | Sim | Tempo da expiração da pendência |
| PCYTYP | Number(005,0) | Sim | Tipo da pendência |
| PCYDES | String(255) | Sim | Descrição da pendência |
| PCYHNT | String(4000) | Sim | Hint da pendência |

---

## Chave Primária

- PRCIID
- ACTVID
- PRCSTP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
