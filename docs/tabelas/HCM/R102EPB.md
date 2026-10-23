# R102EPB

## Descrição

Epi da Brigada

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
| NumEmp | Number(004,0) | Não | Número Empresa |
| CodEpi | Number(008,0) | Não | Código do Equipamento |

---

## Chave Primária

- NumEmp
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102EPB_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R102EPB_001

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

