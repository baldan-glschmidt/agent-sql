# R047FEF

## Descrição

Dados Cpl. R047FAT - Por Empresa/Filial

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFat | Number(004,0) | Não | Código da definição da Fatura |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodFor | Number(009,0) | Sim | Código Fornecedor |
| SerNfi | String(003) | Sim | Série da Nota Fiscal ERP |

---

## Chave Primária

- CodFat
- NumEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047FEF_000

**Tabela:** R047FAT

| Origem | Destino |
|--------|---------|
| CodFat | CodFat |

### IR_R047FEF_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

