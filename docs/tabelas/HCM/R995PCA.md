# R995PCA

## Descrição

Parametros da categoria

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
| CODCPA | Number(004,0) | Não | Código da categoria de auditoria de tela |
| CODSYS | Number(004,0) | Não | Código do Sistema |
| NAMPCA | String(255) | Não | Nome do parametro da categoria |
| DESPCA | String(255) | Sim | Descrição do parâmetro da categoria |
| SEQPCA | Number(004,0) | Sim | Sequencia do parêmetro da categoria |

---

## Chave Primária

- CODCPA
- CODSYS
- NAMPCA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R995PCA_001

**Tabela:** R995CPA

| Origem | Destino |
|--------|---------|
| CODCPA | CODCPA |
| CODSYS | CODSYS |

