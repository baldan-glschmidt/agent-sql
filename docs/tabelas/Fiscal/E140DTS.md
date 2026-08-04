# E140DTS

## Descrição

Vendas - Notas Fiscais de Saída - Detalhamento de Tributos em Serviços

---

## Resumo

- Campos: 20
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIsv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| VlrBas | Number(015,2) | Sim | Valor base sobre o qual o imposto foi calculado |
| VlrIcm | Number(015,2) | Sim | Valor de ICMS |
| VlrIpi | Number(015,2) | Sim | Valor de IPI |
| VlrIss | Number(015,2) | Sim | Valor de ISS |
| VlrIof | Number(015,2) | Sim | Valor de IOF |
| VlrPis | Number(015,2) | Sim | Valor de PIS |
| VlrCof | Number(015,2) | Sim | Valor de Cofins |
| VlrPim | Number(015,2) | Sim | Valor de PIS Importação |
| VlrCim | Number(015,2) | Sim | Valor de Cofins Importação |
| VlrIns | Number(015,2) | Sim | Valor de INSS |
| VlrIim | Number(015,2) | Sim | Valor de Imposto Importação |
| VlrCid | Number(015,2) | Sim | Valor de CIDE |
| IbpFed | Number(015,2) | Sim | Valor aproximado dos tributos federais - IBPT |
| IbpEst | Number(015,2) | Sim | Valor aproximado dos tributos estaduais - IBPT |
| IbpMun | Number(015,2) | Sim | Valor aproximado dos tributos municipais - IBPT |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIsv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140DTS_004

**Tabela:** E140ISV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIsv | SeqIsv |

