# R211CLI

## Descrição

Pesquisa - Itens de classificação dos participantes

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
| TabCla | Number(003,0) | Não | Código da tabela de classificação dos participantes da pesquisa |
| IteCla | Number(003,0) | Não | Código do item de classificação dos participantes da pesquisa |
| DesIte | String(100) | Sim | Descrição do item de classificação dos participantes da pesquisa |

---

## Chave Primária

- TabCla
- IteCla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R211CLI_000

**Tabela:** R211CLA

| Origem | Destino |
|--------|---------|
| TabCla | TabCla |

