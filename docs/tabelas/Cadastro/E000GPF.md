# E000GPF

## Descrição

Tabelas - Integrações - Grupo Fiscal

---

## Resumo

- Campos: 57
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeNgf | Number(009,0) | Não | Identificador do grupo fiscal |
| CodEmp | Number(004,0) | Não | Código da empresa |
| StIcmS | String(003) | Sim | Código da situação tributária para saídasdo produto/Serviço |
| AlIcmS | Number(004,2) | Sim | Percentual de ICMS para saídas |
| StIcmE | String(003) | Sim | Código da situação tributária para entradas do produto/Serviço |
| AlIcmE | Number(004,2) | Sim | Percentual de ICMS para entradas |
| StPisS | String(002) | Sim | Código da situação tributária de PIS para saídas |
| AlPisS | Number(004,2) | Sim | Alíquota de PIS do produto/serviço para saídas |
| StPisE | String(002) | Sim | Código da situação tributária de PIS para Entradas |
| AlPisE | Number(004,2) | Sim | Alíquota de PIS do produto/serviço para entradas |
| StCofS | String(002) | Sim | Código da situação tributária de COFINS para saídas |
| AlCofS | Number(004,2) | Sim | Percentual de Cofins para saídas |
| StCofE | String(002) | Sim | Código da situação tributária de COFINS para entradas |
| AlCofE | Number(004,2) | Sim | Percentual de Cofins para entradas |
| StIpiS | String(002) | Sim | Código da situação tributária de IPI |
| AlIpiS | Number(004,2) | Sim | Percentual do IPI de saída |
| StIpiE | String(002) | Sim | Código da situação tributária de IPI para entradas |
| AlIpiE | Number(005,2) | Sim | Percentual do IPI de entradas |
| MdcIpi | Number(001,0) | Sim | Modo de Cálculo do IPI |
| AlIssS | Number(006,4) | Sim | Percentual do ISS previsto para saídas |
| AlIssE | Number(006,4) | Sim | Percentual do ISS previsto para entradas |
| TabMva | String(003) | Sim | Tabela de Margem Valor Agregado |
| StbPaf | String(003) | Sim | Código da situação tributária do produto/Serviço para PAF |
| SigUfs | String(002) | Não | Sigla do estado |
| TipTrb | Number(001,0) | Sim | Indica Tipo de Tributo (1 = Icms, 2 = Iss) |
| MdbIcm | Number(001,0) | Sim | Modalidade de determinação da BC do ICMS |
| IcmEsE | Number(004,2) | Sim | Percentual de ICMS do estado de entrada |
| RedIcE | Number(008,5) | Sim | Percentual de redução para cálculo do ICMS substituído de entrada |
| RedSai | Number(008,5) | Sim | Percentual de redução/acréscimo da base do imposto nas saídas para contribuinte |
| RedEnt | Number(008,5) | Sim | Percentual de redução/acréscimo na base do imposto nas entradas de contribuinte |
| IcmEsS | Number(004,2) | Sim | Percentual de ICMS do estado de saída |
| RedIcS | Number(008,5) | Sim | Percentual de redução para cálculo do ICMS substituído de saída |
| TprPis | String(004) | Sim | Código da tabela de tributação para o cálculo de PIS por unidade de medida |
| TprCof | String(004) | Sim | Código da tabela de tributação para o cálculo de COFINS por unidade de medida |
| TprIpi | String(004) | Sim | Código da tabela de tributação para o cálculo de IPI por unidade de medida |
| IssErd | Number(006,4) | Sim | Alíquota do ISS de entrada (Redução) |
| IssErt | Number(006,4) | Sim | Alíquota do ISS de entrada (Retenção) |
| IssSrd | Number(006,4) | Sim | Alíquota do ISS de Saída(Redução) |
| IssSrt | Number(006,4) | Sim | Alíquota do ISS de Saída(Retenção) |
| MdcCof | Number(001,0) | Sim | Modo de Cálculo do Cofins |
| MdcPis | Number(001,0) | Sim | Modo de Cálculo do PIS |
| PerDif | Number(005,2) | Sim | Percentual de diferimento |
| IcmAfc | Number(005,2) | Sim | Percentual de ICMS do estado de destino para fundo combate à pobreza na venda |
| IcmInd | Number(005,2) | Sim | Percentual de ICMS interno para estado de destino |
| TipBda | Number(002,0) | Sim | Tipo da base de cálculo do diferencial de alíquota do ICMS |
| RedIcm | Number(008,5) | Sim | Percentual de redução da base de ICMS na UF de destino |
| TemIcm | String(001) | Sim | Indicativo se o produto ou serviço tributa ICMS na UF de destino |
| CodBnf | String(010) | Sim | Código de Benefício Fiscal |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| IstMin | Number(005,2) | Sim | Percentual mínimo de ICMS Subtituição |
| IcmNco | Number(004,2) | Sim | Percentual de ICMS para não contribuinte |
| MarLuc | Number(007,4) | Sim | Percentual margem de lucro ou base para cálculo do imposto substituído |
| RedSnc | Number(008,5) | Sim | Percentual de redução/acréscimo da base do imposto nas saídas para não contribuinte |
| RedEnc | Number(008,5) | Sim | Percentual de redução/acréscimo na base do imposto nas entradas de não contribuinte |
| AplSub | String(001) | Sim | Aplicação da substituição |
| CodCrt | Number(001,0) | Sim | Código do regime tributário |
| IcmSco | Number(004,2) | Sim | Percentual de ICMS para Contribuinte |

---

## Chave Primária

- IdeNgf

---

## Índices

### E000GPFIndice1

**Tipo:** Não unico

Campos:
- CodEmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
