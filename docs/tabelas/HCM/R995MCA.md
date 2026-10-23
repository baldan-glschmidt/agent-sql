# R995MCA

## Descrição

Mensagem da categoria

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
| CODCPA | Number(004,0) | Não | Código da categoria de auditoria de tela |
| CODSYS | Number(004,0) | Não | Código do Sistema |
| VERCPA | Number(004,0) | Não | Código da versão da mensagem  de categoria de auditoria |
| MSGCPA1 | String(2047) | Sim | Mensagem da categoria |
| MSGCPA2 | String(2047) | Sim | mensagem 2 |
| MSGCPA3 | String(2047) | Sim | mensagem 3 |

---

## Chave Primária

- CODCPA
- CODSYS
- VERCPA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R995MCA_001

**Tabela:** R995CPA

| Origem | Destino |
|--------|---------|
| CODCPA | CODCPA |
| CODSYS | CODSYS |

