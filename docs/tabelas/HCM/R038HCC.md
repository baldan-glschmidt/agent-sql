# R038HCC

## Descrição

Histórico Centro de Custo

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração do C.Custo |
| CodCcu | String(018) | Sim | Código do Novo Centro de Custo |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| ConFin | Number(007,0) | Sim | Conta Financeira |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HCCIndice2

**Tipo:** Não unico

Campos:
- StaHis
- DatAlt

### R038HCCIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- CodCcu

---

## Relacionamentos

### IR_R038HCC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HCC_004

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

