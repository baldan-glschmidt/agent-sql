# E210SCM

## Descrição

Estoques - Saldos Consignados Mensais

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 2
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| CodDep | String(010) | Não | Código do depósito |
| MesAno | Date | Não | Mês e ano correspondente as informações |
| CodCli | Number(009,0) | Não | Código do cliente com o produto consignado |
| CodFor | Number(009,0) | Não | Código do fornecedor do produto consignado |
| QtdCfo | Number(014,5) | Sim | Quantidade consignada a fornecedor |
| VlrCfo | Number(015,2) | Sim | Valor total consignado a fornecedor |
| QtdCcl | Number(014,5) | Sim | Quantidade consignada a cliente |
| VlrCcl | Number(015,2) | Sim | Valor total consignado a cliente |

---

## Chave Primária

- CodEmp
- CodFil
- CodPro
- CodDer
- CodDep
- MesAno
- CodCli
- CodFor

---

## Índices

### E210SCMIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodDep

### E210SCMIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

---

## Relacionamentos

### IR_E210SCM_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E210SCM_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E210SCM_002

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E210SCM_003

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E210SCM_004

**Tabela:** E205DEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDep | CodDep |

