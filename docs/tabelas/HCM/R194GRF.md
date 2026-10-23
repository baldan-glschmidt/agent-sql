# R194GRF

## Descrição

BS - Grupos de Tarefas - Faixas

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
| CodGru | Number(004,0) | Não | Código do Grupo de Tarefas |
| VlrFai | Number(011,2) | Não | Valor da Faixa |
| PerGra | Number(005,2) | Sim | Percentual Gratificação |

---

## Chave Primária

- CodGru
- VlrFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R194GRF_000

**Tabela:** R194GRU

| Origem | Destino |
|--------|---------|
| CodGru | CodGru |

