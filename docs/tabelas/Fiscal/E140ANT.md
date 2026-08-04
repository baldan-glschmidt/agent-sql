# E140ANT

## Descrição

Vendas - Nota Fiscal de Saída - Dados do Conhecimento de Transporte - Documentos Anteriores

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| CodTra | Number(009,0) | Não | Código da Transportadora |
| SeqDoc | Number(004,0) | Não | Sequências dos documentos anteriores |
| IndEle | String(001) | Sim | Indicativo se o documento anterior é eletrônico |
| TipAnt | String(002) | Sim | Tipo do documento de transporte anterior |
| CodSer | String(003) | Sim | Série do documento anterior |
| CodSsl | String(002) | Sim | Código da subsérie do documento anterior |
| NumDoc | Number(009,0) | Sim | Número do documento anterior |
| DatEmi | Date | Sim | Data de emissão do documento anterior |
| ChvAnt | String(050) | Sim | Chave do documento eletrônico |
| SeqMtr | Number(004,0) | Sim | Sequência (ordem) do modal |
| SnfCte | String(003) | Sim | Código da série do CT-e anterior |
| NumCte | Number(009,0) | Sim | Número do CT-e anterior |
| IndPst | Number(001,0) | Sim | Indicativo se a prestação é total ou parcial |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- CodTra
- SeqDoc

---

## Índices

### E140ANTIndice1

**Tipo:** Não unico

Campos:
- CodTra

---

## Relacionamentos

### IR_E140ANT_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140ANT_003

**Tabela:** E140CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140ANT_004

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodTra | CodCli |

