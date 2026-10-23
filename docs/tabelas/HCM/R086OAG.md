# R086OAG

## Descrição

Ocorrências - Agente Causador

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipOco | Number(001,0) | Não | Tipo da Ocorrência (Acidente/Incidente) |
| OcoAct | Number(006,0) | Não | Código da Ocorrência |
| AgeLes | Number(003,0) | Não | Código do Agente Causador |

---

## Chave Primária

- NumEmp
- TipOco
- OcoAct
- AgeLes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086OAG_002

**Tabela:** R086OCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| OcoAct | OcoAct |

### IR_R086OAG_003

**Tabela:** R086AGT

| Origem | Destino |
|--------|---------|
| AgeLes | CodAgt |

