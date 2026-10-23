# R995MTA

## Descrição

Mensagem por tipo de parametro da auditoria de tela

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CODTPA | Number(004,0) | Não | Código do tipo de auditoria de tela |
| CODSYS | Number(004,0) | Não | Código do Sistema |
| VERTPA | Number(004,0) | Não | Versão do tipo de mensagem |
| MSGTPA1 | String(2047) | Sim | Mensagem por tipo de parametro |
| MSGTPA2 | String(2047) | Sim | Mensagem 2 |
| MSGTPA3 | String(2047) | Sim | Mensagem 3 |

---

## Chave Primária

- CODTPA
- CODSYS
- VERTPA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R995MTA_001

**Tabela:** R995TPA

| Origem | Destino |
|--------|---------|
| CODTPA | CODTPA |
| CODSYS | CODSYS |

