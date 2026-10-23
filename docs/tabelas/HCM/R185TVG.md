# R185TVG

## Descrição

Orçamento Ind - Def Gerais - Sal Mensal/Tipo Vaga

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| TipVag | Number(002,0) | Não | Código do tipo de vaga |
| IteOrc | Number(003,0) | Sim | Item de orçamento destinado ao cálculo do salário mensal |

---

## Chave Primária

- NumEmp
- AnoBas
- TipVag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185TVG_001

**Tabela:** R185PAR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |

### IR_R185TVG_002

**Tabela:** R022VAG

| Origem | Destino |
|--------|---------|
| TipVag | TipVag |

### IR_R185TVG_003

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

