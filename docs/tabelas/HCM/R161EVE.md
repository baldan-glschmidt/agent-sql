# R161EVE

## Descrição

Bs - Definições Eventos Empréstimos

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
| NumEmp | Number(004,0) | Não | Codigo da Empresa |
| CmpDef | Date | Não | Competência das Definições |
| TipEve | String(001) | Não | Tipo do Evento |
| TabEve | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |

---

## Chave Primária

- NumEmp
- CmpDef
- TipEve
- TabEve
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161EVE_001

**Tabela:** R161DEF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpDef | CmpDef |

### IR_R161EVE_003

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |

### IR_R161EVE_004

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

