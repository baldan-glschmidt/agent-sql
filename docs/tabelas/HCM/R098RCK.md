# R098RCK

## Descrição

Checklist da Revisão de Tipo de Equipamentos

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| TipSvc | Number(003,0) | Não | Tipo de Serviço |
| CodCkl | Number(003,0) | Não | Código |

---

## Chave Primária

- TipEqp
- TipSvc
- CodCkl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098RCK_001

**Tabela:** R098RTE

| Origem | Destino |
|--------|---------|
| TipEqp | TipEqp |
| TipSvc | TipSvc |

### IR_R098RCK_002

**Tabela:** R098CKL

| Origem | Destino |
|--------|---------|
| CodCkl | CodCkl |

