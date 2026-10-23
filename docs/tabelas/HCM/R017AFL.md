# R017AFL

## Descrição

Ação da faixa do local físico - Posto de trabalho

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Não | Posto de trabalho |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| DiaSem | Number(001,0) | Não | Dia da Semana |
| AcoFai | Number(001,0) | Sim | Ação da Faixa |

---

## Chave Primária

- EstPos
- PosTra
- VerPlf
- CodPlf
- DiaSem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017AFL_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R017AFL_002

**Tabela:** R058VPL

| Origem | Destino |
|--------|---------|
| VerPlf | VerPlf |

### IR_R017AFL_003

**Tabela:** R058PLF

| Origem | Destino |
|--------|---------|
| VerPlf | VerPlf |
| CodPlf | CodPlf |

