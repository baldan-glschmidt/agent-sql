# R088NFS

## Descrição

Notas Fiscais de Movimentação de Carga e Descarga

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatChg | Date | Não | Data e Hora de Chegada do Veículo - Estacionamento |
| HorChg | Number(005,0) | Não | Hora de Chegada do Veículo |
| SeqNfs | Number(002,0) | Não | Sequência do Registro |
| TipOpe | Number(001,0) | Sim | Tipo de Operação (Carga/Descarga) |
| NotFis | String(050) | Sim | Notas Fiscais de Movimentação |

---

## Chave Primária

- PlaVei
- DatChg
- HorChg
- SeqNfs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088NFS_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

