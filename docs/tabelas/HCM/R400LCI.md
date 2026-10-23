# R400LCI

## Descrição

Empresas das Localidades

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
| CodLcl | Number(003,0) | Não | Código da Localidade |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |

---

## Chave Primária

- CodLcl
- NumEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R400LCI_000

**Tabela:** R300LCL

| Origem | Destino |
|--------|---------|
| CodLcl | CodLcl |

### IR_R400LCI_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

