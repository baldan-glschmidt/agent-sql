# R017GHE

## Descrição

Postos de Trabalho - Histórico dos GHEs do Posto

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de trabalho |
| DatIni | Date | Não | Define o início do histórico do GHE para o Posto de trabalho |
| SeqHis | Number(002,0) | Não | Sequência do Histórico de GHE |
| CodPRA | Number(009,0) | Sim | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Sim | Código do GHE - Grupo Homogêneo de Exposição |
| AnoHis | String(2000) | Sim | Permite descrever as anotações referentes ao histórico |
| DatFim | Date | Sim | Define o término do histórico do GHE para o Posto de trabalho |

---

## Chave Primária

- EstPos
- PosTra
- DatIni
- SeqHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017GHE_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R017GHE_005

**Tabela:** R583GHE

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |

