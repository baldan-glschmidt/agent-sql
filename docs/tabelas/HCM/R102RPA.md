# R102RPA

## Descrição

Reuniões da Brigada - Plano de Ação

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodBri | Number(003,0) | Não | Código da Brigada |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora da Reunião |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |

---

## Chave Primária

- NumEmp
- CodBri
- DatReu
- HorReu
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102RPA_001

**Tabela:** R102BRI

| Origem | Destino |
|--------|---------|
| CodBri | CodBri |

### IR_R102RPA_003

**Tabela:** R102REB

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodBri | CodBri |
| DatReu | DatReu |
| HorReu | HorReu |

### IR_R102RPA_004

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

