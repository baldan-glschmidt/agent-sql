# R028PVT

## Descrição

Passes do Vale Transporte

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Código do Cadastro do Empregado |
| DatVtr | Date | Não | Data dos Passes VTR |
| CodLin | Number(005,0) | Não | Código da Linha |
| ValPas | Number(008,2) | Sim | Valor dos Passes |
| QtdPas | Number(004,0) | Sim | Qtde de Passes Linha |
| QtdMul | Number(002,0) | Não | Qtde de Múltiplos |
| StaPvt | String(001) | Sim | Status do Vale |
| OriPvt | String(001) | Sim | Origem dos Passes |
| StaRcs | String(001) | Sim | Status do Vale Antes da Rescisão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatVtr
- CodLin
- QtdMul

---

## Índices

### R028PVTIndice2

**Tipo:** Não unico

Campos:
- CodLin

### R028PVTIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodLin
- DatVtr
- QtdPas
- ValPas

---

## Relacionamentos

### IR_R028PVT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R028PVT_004

**Tabela:** R028LVT

| Origem | Destino |
|--------|---------|
| CodLin | CodLin |

