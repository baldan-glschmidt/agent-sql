# R047DFI

## Descrição

CIF - Cadastro de Filial (Dependentes)

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodDep | Number(002,0) | Não | Código do Dependente |
| CodFil | Number(006,0) | Não | Código da Filial (Exceção) |
| CodFor | Number(009,0) | Sim | Código Fornecedor ERP |
| SerNfi | String(003) | Sim | Série da Nota Fiscal ERP |

---

## Chave Primária

- CodCif
- NumEmp
- TipCol
- NumCad
- CodDep
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047DFI_000

**Tabela:** R047CIF

| Origem | Destino |
|--------|---------|
| CodCif | CodCif |

### IR_R047DFI_004

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

### IR_R047DFI_005

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

