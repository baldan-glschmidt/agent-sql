# E055CAT

## Descrição

Cadastros - Configurações Crédito Acumulado

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| CodLan | String(006) | Não | Código do Lançamento |
| SeqCat | Number(009,0) | Não | Sequência de Lançamento |
| ProImp | String(255) | Sim | Indicativo do tipo de produto para impostos |
| TipNfs | String(255) | Sim | Tipo da nota fiscal de saída |
| TipNfe | String(255) | Sim | Tipo da nota fiscal de entrada |
| CodEdc | String(255) | Sim | Espécie de documento para fins fiscais |
| CodStr | String(255) | Sim | Código da situação tributária |
| PerIcm | String(255) | Sim | Percentual do ICMS |
| ObsCat | String(250) | Sim | Observação lançamento |
| TipPro | String(255) | Sim | Tipo do produto |
| IndMis | String(255) | Sim | Indicativo que o produto é produzido mas também pode ser comprado (Misto) |
| IndVen | String(255) | Sim | Indicativo se o produto pode ser vendido/faturado (item pedido e NF saída) |

---

## Chave Primária

- CodEmp
- CodTns
- CodLan
- SeqCat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055CAT_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E055CAT_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

