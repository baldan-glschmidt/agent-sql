# R047FEM

## Descrição

Dados Cpl. R047FAT - Por Empresa

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFat | Number(004,0) | Não | Código da definição da Fatura |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTrs | String(005) | Sim | Código da Transação |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Sim | Conta Financeira |

---

## Chave Primária

- CodFat
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047FEM_000

**Tabela:** R047FAT

| Origem | Destino |
|--------|---------|
| CodFat | CodFat |

### IR_R047FEM_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

