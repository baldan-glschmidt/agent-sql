# R088HST

## Descrição

Histórico de Situações de Veículos

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatIni | Date | Não | Data do Início do Histórico de Situações de Veículo |
| HorIni | Number(005,0) | Não | Hora do Início do Histórico de Situações de Veículo |
| SitVei | Number(003,0) | Sim | Situação do Veículo |
| DatFim | Date | Sim | Data do Final do Histórico de Situações de Veículo |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico de Situações de Veículo |
| ObsSit | String(080) | Sim | Observação da Situação |

---

## Chave Primária

- PlaVei
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088HST_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088HST_003

**Tabela:** R088SIT

| Origem | Destino |
|--------|---------|
| SitVei | SitVei |

