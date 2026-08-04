# E001NOF

## Descrição

Tabelas - Naturezas de Operação FAF

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| NatOpe | String(499) | Não | Natureza de Operação |
| DatCpt | Date | Não | Mês e ano de competência inicial da Natureza de Operação |

---

## Chave Primária

- CodEmp
- DatCpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E001NOF_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

