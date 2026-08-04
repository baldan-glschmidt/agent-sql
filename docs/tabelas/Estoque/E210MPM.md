# E210MPM

## Descrição

Estoques - Movimentos - Preço Médio Depósito

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificação do movimento |
| IdePmd | String(050) | Não | Identificação do mov. preço médio depósito |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDep | String(010) | Não | Código do depósito |
| CodPro | String(014) | Não | Código do produto movimentado |
| CodDer | String(007) | Não | Código da derivação do produto movimentado |
| DatMov | Date | Não | Data da movimentação do estoque |
| SeqMov | Number(006,0) | Não | Sequência de movimento na data de movimentação |

---

## Chave Primária

- IdeUni

---

## Índices

### E210MPMindice1

**Tipo:** Unico

Campos:
- CodEmp
- CodPro
- CodDer
- CodDep
- DatMov
- SeqMov
- IdePmd

---

## Relacionamentos

### IR_E210MPM_001

**Tabela:** E210PMD

| Origem | Destino |
|--------|---------|
| IdePmd | IdeUni |

