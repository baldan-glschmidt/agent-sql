# R086OCU

## Descrição

Ocorrências - Custos

---

## Resumo

- Campos: 6
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
| CodCus | Number(003,0) | Não | Item de Custo da Ocorrência |
| QtdHor | Number(010,0) | Sim | Quantidade de Horas do Item de Custo |
| ValCus | Number(011,2) | Sim | Valor do Item de Custo |

---

## Chave Primária

- NumEmp
- TipOco
- OcoAct
- CodCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086OCU_002

**Tabela:** R086OCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| OcoAct | OcoAct |

### IR_R086OCU_003

**Tabela:** R086CUS

| Origem | Destino |
|--------|---------|
| CodCus | CodCus |

