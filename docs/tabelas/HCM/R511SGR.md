# R511SGR

## Descrição

Avaliação - Formulário de avaliação - Séries do gráfico

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPfa | Number(004,0) | Não | Código do perfil do formulário de avaliação |
| IdeEll | Number(009,0) | Não | Identificador do elemento do formulário de avaliação |
| SerGra | Number(001,0) | Não | Define o tipo de informação que será apresentado na série do gráfico |
| RotSer | String(050) | Sim | Rótulo da série |

---

## Chave Primária

- CodPfa
- IdeEll
- SerGra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R511SGR_001

**Tabela:** R511FAL

| Origem | Destino |
|--------|---------|
| CodPfa | CodPfa |
| IdeEll | IdeEll |

