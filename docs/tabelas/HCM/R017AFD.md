# R017AFD

## Descrição

Ação da faixa do dispositivo - Posto de trabalho

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Não | Posto de trabalho |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| DiaSem | Number(001,0) | Não | Dia da Semana |
| AcoFai | Number(001,0) | Sim | Ação da faixa |

---

## Chave Primária

- EstPos
- PosTra
- CodDsp
- DiaSem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017AFD_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R017AFD_002

**Tabela:** R058DSP

| Origem | Destino |
|--------|---------|
| CodDsp | CodDsp |

