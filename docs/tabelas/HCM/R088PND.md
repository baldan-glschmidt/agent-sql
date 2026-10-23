# R088PND

## Descrição

Manutenções Programadas Pendentes

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| CodPec | Number(006,0) | Não | Código da Peça/Serviço em Manutenção |
| QuiPrv | Number(007,0) | Sim | Quilometragem Prevista para Manutenção do Veículo |
| QuiRlz | Number(007,0) | Sim | Quilometragem Realizada na Manutenção do Veículo |
| DatAgm | Date | Sim | Data do Agendamento da Manutenção |
| HorAgm | Number(005,0) | Sim | Hora de Agendamento da Manutenção |
| ManAgm | String(001) | Sim | Manutenção já agendada (S/N) |
| AgePen | String(001) | Sim | Agendar essa pendência (S/N) |
| QuiPen | Number(007,0) | Sim | Quilometragem do veículo ao gerar pendência |

---

## Chave Primária

- PlaVei
- CodPec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088PND_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088PND_001

**Tabela:** R088PEC

| Origem | Destino |
|--------|---------|
| CodPec | CodPec |

