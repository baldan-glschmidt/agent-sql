# R130CEV

## Descrição

Custos Treinamento - Códigos de Eventos p/Reembolso

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTcu | Number(004,0) | Não | Código do Item de Custo |
| NumEmp | Number(004,0) | Não | Número da Empresa p/Reembolso |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |
| CodEvd | Number(004,0) | Sim | Código do evento para lançamento de desconto |

---

## Chave Primária

- CodTcu
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130CEV_000

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

### IR_R130CEV_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R130CEV_003

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

