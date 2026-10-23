# R086OPA

## Descrição

Ocorrências - Planos de Ação

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
| CodPln | Number(009,0) | Não | Código do Plano de Ação |

---

## Chave Primária

- NumEmp
- TipOco
- OcoAct
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086OPA_002

**Tabela:** R086OCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| OcoAct | OcoAct |

### IR_R086OPA_003

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

