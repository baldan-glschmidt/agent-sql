# R088MES

## Descrição

Movimentação de veículos em estacionamento

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VerPlf | Number(003,0) | Não | Versão do plano de localização física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| PlaVei | String(010) | Não | Placa do veículo |
| DatEnt | Date | Não | Data de entrada do veículo |
| HorEnt | Number(005,0) | Não | Hora entrada veiculo |
| NumCra | Number(012,0) | Sim | Número do crachá |
| ArePlf | Number(007,0) | Sim | Ambiente de estacionamento de veículos. |
| DatSai | Date | Sim | Data de saída do veículo |
| HorSai | Number(005,0) | Sim | Hora saída veículo |
| ObsEst | String(080) | Sim | Observação da movimentação em estacionamento |

---

## Chave Primária

- VerPlf
- CodPlf
- PlaVei
- DatEnt
- HorEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088MES_002

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

