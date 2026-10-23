# R092EFE

## Descrição

Quadro Efetivo p/ Posto de Trabalho

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| CodPlv | Number(004,0) | Não | Código do Plano de Vagas |
| PosTra | String(024) | Não | Posto de Trabalho |
| DatEfe | Date | Não | Data do Efetivo |
| QtdVag | Number(006,0) | Sim | Quantidade de Vagas do Efetivo |
| QtdAfa | Number(006,0) | Sim | Quantidade de Afastamentos do Efetivo |
| QtdRqu | Number(006,0) | Sim | Quantidade de Requisições do Efetivo |
| QtdSol | Number(006,0) | Sim | Quantidade de Solicitações do Efetivo |
| OriEfe | Number(001,0) | Sim | Origem do Efetivo |

---

## Chave Primária

- EstPos
- CodPlv
- PosTra
- DatEfe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R092EFE_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R092EFE_001

**Tabela:** R017PLV

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodPlv | CodPlv |

### IR_R092EFE_002

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

