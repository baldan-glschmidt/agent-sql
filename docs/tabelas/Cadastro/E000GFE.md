# E000GFE

## Descrição

Tabelas - Integrações - Grupo Fiscal para compras

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeGfe | Number(009,0) | Não | Identificador do grupo fiscal |
| CodEmp | Number(004,0) | Não | Código da empresa |
| SigUfs | String(002) | Não | Sigla do estado |
| CodStr | String(003) | Sim | Código da situação tributária para compra do produto |
| PerCim | Number(008,4) | Sim | Percentual de COFINS a Recuperar na Importação |
| PerPim | Number(008,4) | Sim | Percentual de PIS a Recuperar na Importação |
| PerPis | Number(008,4) | Sim | Percentual de PIS do produto |
| PerCof | Number(008,4) | Sim | Percentual de Cofins do produto |
| TriPis | String(001) | Sim | Indicativo se o produto tem tributação de PIS ou não |
| TriCof | String(001) | Sim | Indicativo se o produto tem tributação de COFINS ou não |
| CstPic | String(002) | Sim | Código da situação tributária de PIS nas operações de compra |
| CstCoc | String(002) | Sim | Código da situação tributária de COFINS nas operações de compra |
| IcmEco | Number(008,4) | Sim | Percentual de ICMS de entrada para contribuinte |
| RedIce | Number(008,5) | Sim | Percentual de redução para cálculo do ICMS substituído de entrada |
| RedEnt | Number(008,5) | Sim | Percentual de redução/acréscimo na base do imposto nas entradas de contribuinte |
| MarLuc | Number(007,4) | Sim | Percentual margem de lucro ou base para cálculo do imposto substituído |
| PerIpi | Number(008,4) | Sim | Percentual de IPI do item da nota fiscal de entrada |
| IstMin | Number(008,4) | Sim | Percentual mínimo de ICMS Substituição |
| IcmEnc | Number(008,4) | Sim | Percentual de ICMS especial entrada para não contribuinte |
| TemIcm | String(001) | Sim | Indicativo se o produto tem tributação de ICMS |
| IcmIeo | Number(005,2) | Sim | Alíquota de ICMS Interestadual da operação |

---

## Chave Primária

- IdeGfe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
