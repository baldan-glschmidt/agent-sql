# R050GRU

## Descrição

Compromissos - Grupos

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCom | Number(004,0) | Não | Código do Compromisso |
| CodGru | Number(004,0) | Não | Código do Grupo |

---

## Chave Primária

- CodCom
- CodGru

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R050GRU_000

**Tabela:** R050COM

| Origem | Destino |
|--------|---------|
| CodCom | CodCom |

### IR_R050GRU_001

**Tabela:** R150GRU

| Origem | Destino |
|--------|---------|
| CodGru | CodGru |

