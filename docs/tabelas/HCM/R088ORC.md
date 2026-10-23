# R088ORC

## Descrição

Solicitações de Oficina - Orçamentos

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSol | Number(006,0) | Não | Código da Solicitação de Oficina |
| CodOem | Number(008,0) | Não | Código da Empresa que Gerou o Orçamento |
| ApvOrc | String(001) | Sim | Orçamento Aprovado |

---

## Chave Primária

- CodSol
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088ORC_000

**Tabela:** R088SOF

| Origem | Destino |
|--------|---------|
| CodSol | CodSol |

### IR_R088ORC_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

