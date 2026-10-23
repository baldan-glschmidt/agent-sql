# R086OCA

## Descrição

Ocorrências - Causas de Acidente

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
| CauAct | Number(003,0) | Não | Causa Acidente |

---

## Chave Primária

- NumEmp
- TipOco
- OcoAct
- CauAct

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086OCA_002

**Tabela:** R086OCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| OcoAct | OcoAct |

### IR_R086OCA_003

**Tabela:** R086CAC

| Origem | Destino |
|--------|---------|
| CauAct | CodCau |

