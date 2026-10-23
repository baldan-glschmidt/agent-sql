# R117IRE

## Descrição

Perguntas - Itens de Resposta

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(002,0) | Não | Código da Pergunta |
| IteRes | Number(002,0) | Não | Item Resposta |
| DesIte | String(100) | Sim | Descrição do Item de Resposta |
| TipIte | String(001) | Sim | Tipo do Item de Resposta |

---

## Chave Primária

- CodPer
- IteRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R117IRE_000

**Tabela:** R117PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

