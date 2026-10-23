# R400FIL

## Descrição

Direção da Replicação de Colaboradores

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
| LclOri | Number(003,0) | Não | Código da Localidade de Origem |
| LclDes | Number(003,0) | Não | Código da Localidade de Destino |

---

## Chave Primária

- LclOri
- LclDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R400FIL_000

**Tabela:** R300LCL

| Origem | Destino |
|--------|---------|
| LclOri | CodLcl |

### IR_R400FIL_001

**Tabela:** R300LCL

| Origem | Destino |
|--------|---------|
| LclDes | CodLcl |

