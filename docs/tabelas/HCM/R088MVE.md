# R088MVE

## Descrição

Movimentação de Manutenções do Veículo

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatIni | Date | Não | Data Inicio Manutenção |
| HorIni | Number(005,0) | Não | Hora de Início da Manutenção |
| DatPrv | Date | Sim | Data Prevista da Manutenção (Agendamento) |
| QuiPrv | Number(007,0) | Sim | Quilometragem Prevista no Agendamento da Manutenção |
| ClaMan | Number(001,0) | Sim | Classificação da Manutenção |
| CodOem | Number(008,0) | Sim | Código da Empresa que Realizou a Manutenção |
| QuiMan | Number(007,0) | Sim | Quilometragem para Manutenção |
| NumNFS | String(044) | Sim | Número da Nota Fiscal |
| NumOse | Number(007,0) | Sim | Número da Ordem Serviço |
| ObsMan | String(1500) | Sim | Observação da Manutenção |
| CodSol | Number(006,0) | Sim | Código da Solicitação de Oficina |

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

### IR_R088MVE_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

