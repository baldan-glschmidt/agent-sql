# R017HDE

## Descrição

Postos de Trabalho - Revisão descrição

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatHis | Date | Não | Data da revisão da descrição do Posto |

---

## Chave Primária

- EstPos
- PosTra
- DatHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017HDE_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

