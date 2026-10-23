# R050LOG

## Descrição

Compromissos - Log

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DtHPro | Number(014,6) | Não | Data/Hora do Log |
| CnxUsu | Number(005,0) | Não | Número de Conexão do Usuário |
| SeqLog | Number(003,0) | Não | Sequência do Log |
| MsgLog | String(255) | Sim | Mensagem do Log |
| CodCom | Number(004,0) | Sim | Código do Compromisso |
| CodGru | Number(004,0) | Sim | Código do Grupo |
| TipCal | Number(002,0) | Sim | Tipo do Cálculo |
| IniOco | Date | Sim | Data de Início da Ocorrência |
| CodUsu | Number(010,0) | Sim | Código do Usuário |

---

## Chave Primária

- DtHPro
- CnxUsu
- SeqLog

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
