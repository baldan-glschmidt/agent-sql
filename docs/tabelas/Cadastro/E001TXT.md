# E001TXT

## Descrição

Tabelas - Transação - Ligação Transação Saída X Transação Entrada

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| TnsVen | String(005) | Não | Código da transação de saída |
| TnsCpr | String(005) | Não | Código da transação de entrada |
| SeqTxt | Number(009,0) | Não | Sequência de ligação |
| TipNfe | Number(002,0) | Sim | Tipo de nota fiscal de entrada |
| StiNfe | String(003) | Sim | Código da situação tributária de ICMS na entrada |
| StpNfe | String(002) | Sim | Código da situação tributária de IPI na entrada |
| CodFin | Number(004,0) | Sim | Código da finalidade de compra e venda |
| TipCcu | Number(001,0) | Sim | Tipo do centro de custos |
| TipPro | String(001) | Sim | Tipo do produto |
| ProImp | Number(002,0) | Sim | Indicativo do tipo de produto para impostos |
| StpNfs | String(002) | Sim | Código da situação tributária de IPI na saída |
| StiNfs | String(003) | Sim | Código da situação tributária de ICMS na saída |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- TnsVen
- TnsCpr
- SeqTxt

---

## Índices

### E001TXTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- TnsCpr

---

## Relacionamentos

### IR_E001TXT_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| TnsVen | CodTns |

### IR_E001TXT_002

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| TnsCpr | CodTns |

