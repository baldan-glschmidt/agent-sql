# R017GRU

## Descrição

Postos de trabalho - Grupos de usuário

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
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatSeq | Number(005,0) | Não | Sequência |
| DatOne | String(254) | Sim | Dado Um (Criptografado) |
| DatTwo | String(254) | Sim | Dado Dois (Criptografado) |

---

## Chave Primária

- EstPos
- PosTra
- DatSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017GRU_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

