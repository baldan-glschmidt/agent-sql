# E020MSL

## Descrição

Cadastros - Movimentação dos Selos de IPI

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSip | String(010) | Não | Código do selo do IPI |
| SeqSip | Number(009,0) | Não | Sequência do lançamento do selo do IPI |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| DatMov | Date | Não | Data do movimento da nota fiscal de saída |
| QtdSip | Number(015,0) | Sim | Quantidade de selos de IPI utilizados na nota fiscal |
| SelIni | Number(015,0) | Sim | Número do selo inicial utilizado na nota fiscal |
| SelFim | Number(015,0) | Sim | Número do selo final utilizado na nota fiscal |
| ObsUti | String(255) | Sim | Observação para a utilização do selo |

---

## Chave Primária

- CodEmp
- CodFil
- CodSip
- SeqSip

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E020MSL_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E020MSL_002

**Tabela:** E020SEL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSip | CodSip |

