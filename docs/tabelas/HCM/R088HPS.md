# R088HPS

## Descrição

Histórico de Crachás de Veículos de Prestador de Serviço

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do veículo |
| DatIni | Date | Não | Data início |
| HorIni | Number(005,0) | Não | Hora início |
| NumCra | Number(012,0) | Sim | Número do crachá |
| DatFim | Date | Sim | Data final |
| HorFim | Number(005,0) | Sim | Hora final |
| StaAcc | Number(001,0) | Sim | Status da atualização da tabela CONTROLE |

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

Nenhum relacionamento cadastrado.
