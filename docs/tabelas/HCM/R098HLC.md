# R098HLC

## Descrição

Histórico de Localização dos Equipamentos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| DatAlt | Date | Não | Data da Alteração do Local |
| CodLcz | Number(004,0) | Sim | Código da Localização |

---

## Chave Primária

- NumEmp
- TipEqp
- CodEqp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098HLC_002

**Tabela:** R098EQP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |

### IR_R098HLC_004

**Tabela:** R098LCZ

| Origem | Destino |
|--------|---------|
| CodLcz | CodLcz |

