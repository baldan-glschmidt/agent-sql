# R995PRT

## Descrição

Parâmetros do tipo de auditoria

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CODRPA | Number(015,0) | Não | Código do registro de auditoria de tela |
| NAMPPA | String(255) | Não | Nome do parâmetro |
| CONPPA | String(1000) | Sim | Conteúdo do parâmetro |

---

## Chave Primária

- CODRPA
- NAMPPA

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R995PRT_000

**Tabela:** R995RPA

| Origem | Destino |
|--------|---------|
| CODRPA | CODRPA |

