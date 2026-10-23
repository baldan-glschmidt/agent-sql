# R085SIT

## Descrição

Orçamento - Itens - Situações

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
| IteOrc | Number(003,0) | Não | Código do Item |
| SitAfa | Number(003,0) | Não | Situação de Afastamento |

---

## Chave Primária

- IteOrc
- SitAfa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085SIT_000

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

### IR_R085SIT_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitAfa | CodSit |

