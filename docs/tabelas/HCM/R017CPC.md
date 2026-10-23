# R017CPC

## Descrição

Postos de Trabalho - Características - Cargos

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatIni | Date | Não | Data de início das Características do Posto de Trabalho |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos do Posto de Trabalho |
| CarPos | String(024) | Não | Código do Cargo do Posto de Trabalho |

---

## Chave Primária

- EstPos
- PosTra
- DatIni
- EstCar
- CarPos

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017CPC_002

**Tabela:** R017CAR

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |
| DatIni | DatIni |

### IR_R017CPC_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CarPos | CodCar |

