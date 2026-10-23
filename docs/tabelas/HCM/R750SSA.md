# R750SSA

## Descrição

Status dos serviços agendados

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IDPROC | String(100) | Não | ID do Processo |
| DATINI | Date | Sim | Data/Hora de início |
| STATUS | Number(001,0) | Sim | Status |
| REQPRO | String(020) | Sim | Número da requisição de processamento |
| REQAGE | String(020) | Sim | Número da requisição agendada |
| CODUSU | Number(010,0) | Sim | Código do Usuário |
| DTPING | Date | Sim | Data/Hora da última notificação |
| PERCON | Number(003,0) | Sim | Percentual Concluído |
| QTDERR | Number(009,0) | Sim | Quantidade de erros |
| SEQETA | Number(004,0) | Sim | Etapas concluídas |
| INFADI | String(255) | Sim | Informações adicionais |

---

## Chave Primária

- IDPROC

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
