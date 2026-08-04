# E210SFC

## Descrição

Estoques - Saldos Consignados Mensais por Depósito

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto consignado |
| CodDer | String(007) | Não | Código da derivação do produto consignado |
| CodDep | String(010) | Não | Código do depósito do produto consignado |
| MesAno | Date | Não | Mês e ano correspondente as informações |
| CodCli | Number(009,0) | Não | Código do cliente com o produto consignado |
| CodFor | Number(009,0) | Não | Código do fornecedor do produto consignado |
| FilDep | Number(005,0) | Sim | Código da filial que o depósito pertence |
| QtdCsg | Number(014,5) | Sim | Quantidade consignado com o cliente ou do fornecedor |
| VlrCsg | Number(015,2) | Sim | Valor consignado com o cliente ou do fornecedor |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodDep
- CodCli
- CodFor
- MesAno

---

## Índices

### E210SFCIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodDep

---

## Relacionamentos

### IR_E210SFC_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E210SFC_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E210SFC_003

**Tabela:** E205DEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDep | CodDep |

