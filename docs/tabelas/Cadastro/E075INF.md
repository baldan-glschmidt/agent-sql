# E075INF

## Descrição

Cadastros - Produtos - Impostos no Documento Fiscal

---

## Resumo

- Campos: 24
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodSer | String(014) | Não | Código do serviço |
| PerInf | Date | Não | Data base inicial de validade |
| ConIcm | String(001) | Sim | Considerar ICMS do Faturamento do Item da Nota Fiscal |
| PerIcm | Number(005,2) | Sim | Percentual do ICMS |
| ConIpi | String(001) | Sim | Considerar IPI do Faturamento do Item da Nota Fiscal |
| PerIpi | Number(013,4) | Sim | Percentual ou alíquota de IPI |
| ConIss | String(001) | Sim | Considerar ISS do Faturamento do Item da Nota Fiscal |
| PerIss | Number(007,4) | Sim | Percentual do ISS |
| PerIof | Number(005,2) | Sim | Percentual de IOF |
| ConPis | String(001) | Sim | Considerar PIS do Faturamento do Item da Nota Fiscal |
| PerPis | Number(013,4) | Sim | Percentual ou alíquota do PIS |
| ConCof | String(001) | Sim | Considerar COFINS do Faturamento do Item da Nota Fiscal |
| PerCof | Number(013,4) | Sim | Percentual ou alíquota do Cofins |
| PerPim | Number(007,4) | Sim | Percentual do PIS importação |
| PerCim | Number(007,4) | Sim | Percentual do Cofins importação |
| ConIns | String(001) | Sim | Considerar INSS do Faturamento do Item da Nota Fiscal |
| PerIns | Number(005,2) | Sim | Percentual do INSS |
| PerIim | Number(005,2) | Sim | Percentual de imposto de importação |
| ConCid | String(001) | Sim | Considerar CIDE do Faturamento do Item da Nota Fiscal |
| PerCid | Number(011,2) | Sim | Valor unitário do CIDE |

---

## Chave Primária

- CodEmp
- CodFil
- CodPro
- CodDer
- CodSer
- PerInf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
