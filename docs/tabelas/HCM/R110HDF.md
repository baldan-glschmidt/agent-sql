# R110HDF

## Descrição

Ficha Médica - Deficiências

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFic | Number(009,0) | Não | Código da Ficha Médica |
| CodDef | Number(002,0) | Não | Código da Deficiência |
| DatDef | Date | Sim | Data início da deficiência |
| ObsDef | String(500) | Sim | Observação sobre a deficiência. |
| PriDef | String(001) | Sim | Indicador da principal deficiência |

---

## Chave Primária

- NumEmp
- CodFic
- CodDef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HDF_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110HDF_002

**Tabela:** R022DEF

| Origem | Destino |
|--------|---------|
| CodDef | CodDef |

