# E440RCI

## Descrição

Compras - Notas Fiscais de Entrada - Registro de Entrada de produtos para controle de impostos

---

## Resumo

- Campos: 31
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeRci | Number(009,0) | Não | Identificador do registro de entrada |
| CodEmp | Number(004,0) | Não | Código da empresa da Nota fiscal de entrada |
| CodFil | Number(005,0) | Não | Código da filial da Nota fiscal de entrada |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| CodPro | String(014) | Não | Código do produto da nota fiscal de entrada |
| CodDer | String(007) | Sim | Código da derivação do produto da nota fiscal de entrada |
| DatEnt | Date | Sim | Data da Entrada da Nota |
| QtdEst | Number(014,5) | Sim | Quantidade de entrada conforme unidade de medida de estoque |
| QtdUsa | Number(014,5) | Sim | Quantidade de entrada já em uso por notas fiscais de saída |
| CodTst | String(003) | Sim | Código do ICMS substituído |
| VlrBic | Number(015,2) | Sim | Valor base do ICMS |
| VlrIcm | Number(015,2) | Sim | Valor do ICMS do item da nota fiscal de entrada |
| VlrBsi | Number(015,2) | Sim | Valor base ICMS substituído da nota fiscal de entrada |
| VlrIcs | Number(015,2) | Sim | Valor do ICMS substituído do item da nota fiscal de entrada |
| PerIcs | Number(005,2) | Sim | Percentual do ICMS substituído da última entrada |
| BsiUni | Number(015,9) | Sim | Valor base unitário do ICMS substituído do item da nota fiscal de entrada |
| IcsUni | Number(015,9) | Sim | Valor unitário do ICMS substituído do item da nota fiscal de entrada |
| CodFci | String(036) | Sim | Código da ficha de conteúdo de importação do item da nota fiscal de entrada |
| OriMer | String(001) | Sim | Origem fiscal da mercadoria do item da nota fiscal de entrada |
| IdeMov | String(001) | Sim | Tipo de movimento |
| PerMva | Number(007,4) | Sim | Percentual de MVA do item da nota fiscal de entrada |
| VlrTot | Number(015,2) | Sim | Valor total do item |
| PerFcp | Number(007,4) | Sim | Alíquota do fundo de combate a pobreza |
| BasFcp | Number(015,2) | Sim | Valor base do fundo de combate a pobreza |
| VlrFcp | Number(015,2) | Sim | Valor do fundo de combate a pobreza |
| NopOpe | String(005) | Sim | Natureza de operação |
| UniMed | String(003) | Sim | Código da unidade de medida |
| RedIcm | Number(008,5) | Sim | Percentual de redução para cálculo do imposto |

---

## Chave Primária

- IdeRci

---

## Índices

### E440RCIIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer

### E440RCIIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc

---

## Relacionamentos

### IR_E440RCI_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

