# E140CMC

## Descrição

Vendas - Notas Fiscais de Saída - Controle de Movimento de Cooperado

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificação do controle de movimento de cooperado |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCli | Number(009,0) | Não | Código do cliente da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| MovCoo | String(001) | Sim | Indicativo se o item da nota fiscal de saída é movimento de cooperado |
| IdePrn | Number(009,0) | Sim | Identificação do cálculo da proporcionalidade do movimento de ato cooperado |
| TipNfs | Number(002,0) | Sim | Tipo da nota fiscal de saída |
| DatEmi | Date | Não | Data de emissão da nota fiscal de saída |
| TnsPro | String(005) | Sim | Transação de produto do item da nota |
| CodPro | String(014) | Sim | Código do produto da nota fiscal de saída |
| CodDer | String(007) | Sim | Código da derivação do produto da nota fiscal de saída |
| QtdFat | Number(014,5) | Sim | Quantidade faturada do item da nota fiscal de saída |
| VlrBru | Number(015,2) | Sim | Valor bruto do item da nota fiscal de saída |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item de produto da nota fiscal de saída |
| SitNfv | String(001) | Não | Situação da nota fiscal de saída |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E140CMCIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv

---

## Relacionamentos

### IR_E140CMC_006

**Tabela:** E140IPV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIpv | SeqIpv |

