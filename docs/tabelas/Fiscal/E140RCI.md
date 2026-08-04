# E140RCI

## Descrição

Vendas - Notas Fiscais de Saída - Registro de saída de produtos para controle de impostos

---

## Resumo

- Campos: 27
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdsRci | Number(009,0) | Não | Identificador do registro de saída |
| IdeRci | Number(009,0) | Não | Identificador do registro de entrada que será utilizada |
| CodEmp | Number(004,0) | Não | Código da empresa da nota fiscal de saída |
| CodFil | Number(005,0) | Não | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| QtdFat | Number(014,5) | Sim | Quantidade atendida para o item da nota fiscal de saída |
| IdeMov | String(001) | Sim | Tipo de movimento |
| DatEmi | Date | Sim | Data da emissão da Nota |
| VlrTot | Number(015,2) | Sim | Valor total do item |
| PerFcp | Number(007,4) | Sim | Alíquota do fundo de combate a pobreza |
| BasFcp | Number(015,2) | Sim | Valor base do fundo de combate a pobreza |
| VlrFcp | Number(015,2) | Sim | Valor do fundo de combate a pobreza |
| BasFcc | Number(015,2) | Sim | Valor base do fundo de combate a pobreza complementar |
| VlrFcc | Number(015,2) | Sim | Valor do fundo de combate a pobreza complementar |
| CodStr | String(003) | Sim | Código interno da situação tributária |
| NopOpe | String(005) | Sim | Natureza de operação |
| UniMed | String(003) | Sim | Código da unidade de medida |
| CodCli | Number(009,0) | Sim | Código do Cliente |
| VlrBic | Number(015,2) | Sim | Valor base do ICMS |
| VlrIcm | Number(015,2) | Sim | Valor do ICMS |
| VlrBsi | Number(015,2) | Sim | Valor base do ICMS substituído |
| VlrIcs | Number(015,2) | Sim | Valor ICMS Substituído do item NF saída |
| VlrBsc | Number(015,2) | Sim | Valor da base do ICMS ST complementar |
| VlrIsc | Number(015,2) | Sim | Valor do ICMS ST complementar |
| PerIsc | Number(005,2) | Sim | Alíquota Interna ICMS |

---

## Chave Primária

- IdsRci

---

## Índices

### E140RCIIndice2

**Tipo:** Não unico

Campos:
- IdeRci

### E140RCIIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv

---

## Relacionamentos

### IR_E140RCI_002

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

