# R088HLO

## Descrição

Histórico de Locais para Veículos

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
| DatIni | Date | Não | Data do Início do Histórico de Local do Veículo |
| HorIni | Number(005,0) | Não | Hora do Início do Histórico de Local do Veículo |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| DatFim | Date | Sim | Data do Final do Histórico de Local do Veículo |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico de Local do Veículo |

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

### IR_R088HLO_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088HLO_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

