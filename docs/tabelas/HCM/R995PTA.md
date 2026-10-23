# R995PTA

## Descrição

Parâmetros da categoria do evento de auditoria - Auditoria de telas

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CODTPA | Number(004,0) | Não | Código do tipo de auditoria de tela |
| CODSYS | Number(004,0) | Não | Código do Sistema |
| NAMPTA | String(255) | Não | Nome do parâmetro da categoria de auditoria |
| DESPTA | String(255) | Sim | Descrição do parâmetro da categoria de auditoria |
| SEQPTA | Number(004,0) | Sim | Sequencia do parametro da categia de auditoria |

---

## Chave Primária

- CODTPA
- CODSYS
- NAMPTA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R995PTA_001

**Tabela:** R995TPA

| Origem | Destino |
|--------|---------|
| CODTPA | CODTPA |
| CODSYS | CODSYS |

