# R185TCO

## Descrição

Orçamento Ind - Def Gerais - Sal Mensal/Tipo Contrato

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano base de cálculo do orçamento |
| TipCon | Number(002,0) | Não | Tipo de contrato para quem o item será considerado |
| IteOrc | Number(003,0) | Sim | Item de orçamento destinado ao cálculo do salário mensal |

---

## Chave Primária

- NumEmp
- AnoBas
- TipCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R185TCO_001

**Tabela:** R185PAR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| AnoBas | AnoBas |

### IR_R185TCO_003

**Tabela:** R085ITE

| Origem | Destino |
|--------|---------|
| IteOrc | IteOrc |

