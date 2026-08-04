# E000PLE

## Descrição

Plano de execução dos webservices

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| AbrFil | String(100) | Não | Abrangência do código da filial |
| TipPrc | String(090) | Não | Tipo de processo que foi iniciado |
| DatReq | Date | Sim | Data da requisição |
| HorReq | Number(005,0) | Sim | Hora/minuto da requisição |
| ParEnt | String(8000) | Sim | Parâmetros de entrada |
| CodUsu | Number(010,0) | Sim | Código do usuário responsável pela execução do processo automático |
| StsReq | Number(002,0) | Não | Status da requisição |
| SeqPle | Number(004,0) | Não | Sequencial do plano de execução |
| ParMd5 | String(032) | Não | Hash dos parâmetros (MD5) |
| CamSrv | String(255) | Não | Caminho do serviço de integração |
| NomPor | String(255) | Não | Nome da porta da integração |
| MsgErr | String(500) | Sim | Mensagem de erro |

---

## Chave Primária

- IdeUni

---

## Índices

### E000PLEIndice1

**Tipo:** Não unico

Campos:
- ParMd5

### E000PLEIndice2

**Tipo:** Não unico

Campos:
- StsReq

---

## Relacionamentos

Nenhum relacionamento cadastrado.
