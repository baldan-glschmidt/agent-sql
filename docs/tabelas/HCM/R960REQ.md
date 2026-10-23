# R960REQ

## Descrição

Requisições de serviços Multicamada

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 4
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IDREQ | String(020) | Não | Identificador da requisição |
| TIPSER | String(255) | Sim | Tipo do serviço |
| STATUS | Number(001,0) | Sim | Status da Requisição |
| DATINI | Date | Sim | Data de execução |
| DATFIN | Date | Sim | Data de término da execução |
| CPU | Number(003,0) | Sim | Percentual de utilização de CPU da requisição |
| MEM | Number(012,0) | Sim | Quantidade utilizada de memória virtual da requisição |
| PERCON | Number(003,0) | Sim | Percentual de conclusão do processamento da requisição |
| IDPAR | String(020) | Sim | Identificador da requisição agrupadora |
| NUMLOT | Number(003,0) | Sim | Número do lote dentro da requisição agrupadora |
| HASLOG | String(001) | Sim | Processamento gerou log |
| NOMSVR | String(255) | Sim | Nome do servidor onde o processamento está sendo executado |
| CODUSU | Number(010,0) | Sim | Código do usuário que gerou o processamento |
| NUMSEC | Number(014,0) | Não | Sessão do usuário que iniciou a execução do processo |
| SVREXC | String(050) | Sim | Nome do servidor onde o a instância está sendo processada |
| PIDEXC | Number(009,0) | Sim | Número do PID de execução no servidor |

---

## Chave Primária

- IDREQ

---

## Índices

### IDX_R960REQ_1

**Tipo:** Não unico

Campos:
- TIPSER

### IDX_R960REQ_2

**Tipo:** Não unico

Campos:
- TIPSER
- DATINI
- IDREQ

### IDX_R960REQ_3

**Tipo:** Não unico

Campos:
- TIPSER
- DATFIN
- IDREQ

### IDX_R960REQ_4

**Tipo:** Não unico

Campos:
- STATUS
- NUMSEC
- SVREXC

---

## Relacionamentos

Nenhum relacionamento cadastrado.
