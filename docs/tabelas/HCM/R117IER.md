# R117IER

## Descrição

Perguntas - Itens de Escolha da Resposta

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
| CodPer | Number(002,0) | Não | Código da Pergunta |
| IteRes | Number(002,0) | Não | Item Resposta |
| IteEsc | Number(002,0) | Não | Item de Escolha da Resposta |
| DesEsc | String(100) | Sim | Descrição do Item de Escolha |

---

## Chave Primária

- CodPer
- IteRes
- IteEsc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R117IER_001

**Tabela:** R117IRE

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| IteRes | IteRes |

