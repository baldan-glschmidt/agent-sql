# R151VEI

## Descrição

Vínculo de Veículos e Legislação

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumRen | String(011) | Não | Código Renavam (documento do veículo) |
| CodLeg | Number(003,0) | Não | Código da legislação |
| CodRec | Number(003,0) | Não | Código do recinto alfandegado |
| PlaVei | String(010) | Sim | Placa do veículo |
| DatInc | Date | Sim | Data integração BDCC |
| PrpVei | Number(001,0) | Sim | Proprietário do veículo para o controle alfandegado |
| TpoVei | String(004) | Sim | Tipo de veículo alfandegado |
| RgAntt | String(020) | Sim | Registro ANTT |
| DatIni | Date | Sim | Data de início da vigência |
| HorIni | Number(005,0) | Sim | Hora início da vigência |
| DatFim | Date | Sim | Data fim da vigência |
| HorFim | Number(005,0) | Sim | Hora fim da vigência |
| Status | Number(001,0) | Sim | Status do vínculo |

---

## Chave Primária

- NumRen
- CodLeg
- CodRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
