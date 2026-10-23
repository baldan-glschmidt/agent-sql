# R034AFD

## Descrição

Ação da faixa do dispositivo

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPes | String(023) | Não | Identificador da Pessoa |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| DiaSem | Number(001,0) | Não | Dia da Semana |
| AcoFai | Number(001,0) | Sim | Ação da faixa |
| EstPos | Number(003,0) | Sim | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho |

---

## Chave Primária

- IdtPes
- CodDsp
- DiaSem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034AFD_005

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

