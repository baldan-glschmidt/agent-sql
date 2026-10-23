# R088AGE

## Descrição

Agendamento de Manutenção - Peças e Serviços

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatAgm | Date | Não | Data do Agendamento da Manutenção |
| HorAgm | Number(005,0) | Não | Hora de Agendamento da Manutenção |
| CodPec | Number(006,0) | Não | Código da Peça/Serviço Realizado na Manutenção |

---

## Chave Primária

- PlaVei
- DatAgm
- HorAgm
- CodPec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088AGE_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

