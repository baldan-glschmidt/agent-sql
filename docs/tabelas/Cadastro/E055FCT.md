# E055FCT

## Descrição

Cadastros - Configurações Crédito Acumulado - Filtro

---

## Resumo

- Campos: 13
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| CodLan | String(006) | Não | Código do Lançamento |
| SeqCat | Number(009,0) | Não | Sequência de Lançamento |
| ProImp | Number(002,0) | Não | Indicativo do tipo de produto para impostos |
| TipNfs | Number(002,0) | Não | Tipo da nota fiscal de saída |
| TipNfe | Number(002,0) | Não | Tipo da nota fiscal de entrada |
| CodEdc | String(003) | Não | Espécie de documento para fins fiscais |
| CodStr | String(003) | Não | Código da situação tributária |
| PerIcm | Number(005,2) | Não | Percentual do ICMS |
| TipPro | String(001) | Sim | Tipo do produto |
| IndMis | String(001) | Sim | Indicativo que o produto é produzido mas também pode ser comprado (Misto) |
| IndVen | String(001) | Sim | Indicativo se o produto pode ser vendido/faturado (item pedido e NF saída) |

---

## Chave Primária

- CodEmp
- CodTns
- CodLan
- SeqCat
- ProImp
- TipNfs
- TipNfe
- CodEdc
- CodStr
- PerIcm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055FCT_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E055FCT_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

### IR_E055FCT_003

**Tabela:** E055CAT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |
| CodLan | CodLan |
| SeqCat | SeqCat |

