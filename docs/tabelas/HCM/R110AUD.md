# R110AUD

## Descrição

Audiômetros

---

## Resumo

- Campos: 32
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodAud | Number(003,0) | Não | Código do Audiômetro |
| DesAud | String(030) | Sim | Descrição Audiômetro |
| FabAud | String(040) | Sim | Fabricante do Audiometro |
| MldAut | String(030) | Sim | Modelo do Audiômetro |
| UltAfe | Date | Sim | Data da Última Aferição |
| TemAfe | Number(002,0) | Sim | Tempo para Aferição em Meses |
| UltCal | Date | Sim | Data da Última Calibragem |
| TemCal | Number(002,0) | Sim | Tempo para Calibragem em Meses |
| NroSer | String(030) | Sim | Número de série do aparelho |
| LA0250 | Number(003,0) | Sim | Limite da frequência 0,25 Khz na Via Aérea |
| LA0500 | Number(003,0) | Sim | Limite da frequência 0,5 Khz na Via Aérea |
| LA1000 | Number(003,0) | Sim | Limite da frequência 1 Khz na Via Aérea |
| LA2000 | Number(003,0) | Sim | Limite da frequência 2 Khz na Via Aérea |
| LA3000 | Number(003,0) | Sim | Limite da frequência 3 Khz na Via Aérea |
| LA4000 | Number(003,0) | Sim | Limite da frequência 4 Khz na Via Aérea |
| LA6000 | Number(003,0) | Sim | Limite da frequência 6 Khz na Via Aérea |
| LA8000 | Number(003,0) | Sim | Limite da frequência 8 Khz na Via Aérea |
| LO0250 | Number(003,0) | Sim | Limite da frequência 0,25 Khz na Via Óssea |
| LO0500 | Number(003,0) | Sim | Limite da frequência 0,5 Khz na Via Óssea |
| LO1000 | Number(003,0) | Sim | Limite da frequência 1 Khz na Via Óssea |
| LO2000 | Number(003,0) | Sim | Limite da frequência 2 Khz na Via Óssea |
| LO3000 | Number(003,0) | Sim | Limite da frequência 3 Khz na Via Óssea |
| LO4000 | Number(003,0) | Sim | Limite da frequência 4 Khz na Via Óssea |
| LO6000 | Number(003,0) | Sim | Limite da frequência 6 Khz na Via Óssea |
| CodCab | Number(003,0) | Sim | Código da Cabine |
| LA0125 | Number(003,0) | Sim | Limite da frequência 0,125 Khz na Via Aérea |
| LA0750 | Number(003,0) | Sim | Limite da frequência 0,75 Khz na Via Aérea |
| LA1500 | Number(003,0) | Sim | Limite da frequência 1,5 Khz na Via Aérea |
| LO0125 | Number(003,0) | Sim | Limite da frequência 0,125 Khz na Via Óssea |
| LO0750 | Number(003,0) | Sim | Limite da frequência 0,75 Khz na Via Óssea |
| LO1500 | Number(003,0) | Sim | Limite da frequência 1,5 Khz na Via Óssea |

---

## Chave Primária

- NumEmp
- CodAud

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110AUD_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

