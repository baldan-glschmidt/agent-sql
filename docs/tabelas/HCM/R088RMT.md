# R088RMT

## Descrição

Relacionamento de Manutenções com Peças e Serviços

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMan | Number(003,0) | Não | Código da Manuteção |
| CodPec | Number(006,0) | Não | Código da Peça ou Serviço |

---

## Chave Primária

- CodMan
- CodPec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088RMT_000

**Tabela:** R088MNT

| Origem | Destino |
|--------|---------|
| CodMan | CodMan |

### IR_R088RMT_001

**Tabela:** R088PEC

| Origem | Destino |
|--------|---------|
| CodPec | CodPec |

