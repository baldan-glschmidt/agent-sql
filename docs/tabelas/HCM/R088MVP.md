# R088MVP

## Descrição

Peças e Serviços para Manutenção de Veículos

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatIni | Date | Não | Data de Início da Manutenção |
| HorIni | Number(005,0) | Não | Hora de Início da Manutenção |
| CodPec | Number(006,0) | Não | Código da Peça/Serviço Realizado na Manutenção |
| ValPec | Number(011,2) | Sim | Valor da Peça/Serviço |
| UniPec | Number(003,0) | Sim | Unidade de Medida para Peça / Serviço |
| QtdPec | Number(008,2) | Sim | Quantidade de Peça / Serviço |
| NumNfs | String(044) | Sim | Nota(s) Fiscal(ais) da peça. |
| ObsPec | String(1500) | Sim | Observação da Peça de Manutenção |
| DatCmp | Date | Sim | Data da Compra da Peça da Manutenção |
| PerGar | Number(008,0) | Sim | Período Garantia (em dias) |
| TipGar | String(001) | Sim | Tipo de Duração da Garantia de Peças e Serviços |

---

## Chave Primária

- PlaVei
- DatIni
- HorIni
- CodPec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088MVP_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088MVP_002

**Tabela:** R088MVE

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |
| DatIni | DatIni |
| HorIni | HorIni |

### IR_R088MVP_003

**Tabela:** R088PEC

| Origem | Destino |
|--------|---------|
| CodPec | CodPec |

