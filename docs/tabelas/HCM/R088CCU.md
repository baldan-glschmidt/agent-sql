# R088CCU

## Descrição

Histórico de Centro de Custos

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
| DatIni | Date | Não | Data de Início do Histórico do Centro de Custo |
| HorIni | Number(005,0) | Não | Hora de Início do Histórico do Centro de Custo |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodCcu | String(018) | Sim | Código Centro de Custo Contábil |
| DatFim | Date | Sim | Data Final do Histórico do Centro de Custo |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico do Centro de Custo |

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

### IR_R088CCU_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088CCU_004

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

