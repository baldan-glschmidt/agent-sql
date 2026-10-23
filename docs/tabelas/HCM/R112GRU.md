# R112GRU

## Descrição

Grupos de Questionário - Obsoleta

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
| NumEmp | Number(004,0) | Não | Número Empresa |
| CodGrq | Number(003,0) | Não | Código Grupo Questionário |
| DesGrq | String(020) | Sim | Descrição Grupo Questionário |

---

## Chave Primária

- NumEmp
- CodGrq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R112GRU_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

