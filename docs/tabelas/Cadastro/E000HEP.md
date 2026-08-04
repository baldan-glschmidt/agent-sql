# E000HEP

## Descrição

Histórico de Execução de Processo

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| TipPrc | String(090) | Não | Tipo de processo que foi iniciado |
| NumSec | Number(014,0) | Não | Sessão do usuário que iniciou a execução do processo |
| DatTim | Number(014,6) | Sim | Data do inicio da conexão |
| ParExe | String(8000) | Sim | Sessão do usuário que iniciou a execução do processo |
| UsuGer | Number(010,0) | Sim | Usuário que iniciou a execução do processo |
| DatReq | Date | Sim | Data da requisição |
| HorReq | Number(005,0) | Sim | Hora da requisição |
| IdePle | Number(009,0) | Sim | Identificador do Plano de execução dos webservices |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
