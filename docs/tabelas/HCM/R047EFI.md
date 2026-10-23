# R047EFI

## Descrição

Dados por Empresa e Filial

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
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodFor | Number(009,0) | Sim | Código Fornecedor |
| SerNfi | String(003) | Sim | Série da Nota Fiscal ERP |

---

## Chave Primária

- CodCif
- NumEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047EFI_000

**Tabela:** R047CIF

| Origem | Destino |
|--------|---------|
| CodCif | CodCif |

### IR_R047EFI_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

