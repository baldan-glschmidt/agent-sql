# R350TMP

## Descrição

eSocial - Pendências geradas para colaboradores em processo de migração do eSocial

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PidPen | String(030) | Não | Identificador sequencial da pendência |
| DatHor | Number(014,6) | Sim | Data e hora de geração da pendência |
| TabPen | String(007) | Sim | Tabela do sistema que originou a pendência |
| OpePen | String(001) | Sim | Operação que originou a pendência (I,A,E) |
| EvePen | String(001) | Sim | Evento que originou a pendência |
| UsuPen | Number(010,0) | Sim | Usuário que originou a pendência |
| NumEmp | Number(004,0) | Sim | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Sim | Tipo do colaborador |
| NumCad | Number(009,0) | Sim | Cadastro |
| IniVal | Date | Sim | Início da validade da pendência |
| FimVal | Date | Sim | Fim da validade da pendência |
| VlrPe1 | String(2000) | Sim | Dados da pendência |
| VlrPe2 | String(2000) | Sim | Dados da pendência |
| LayOut | String(006) | Sim | Leiaute de origem da pendência |
| DatEnc | Date | Sim | Data de encerramento |
| DatRef | Date | Sim | Data de referência |
| PenExt | String(001) | Sim | Pendência gerada por uma alteração extemporânea |
| OriPen | String(060) | Sim | Origem da pendência |

---

## Chave Primária

- PidPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
