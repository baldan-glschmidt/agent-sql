# E019SUB

## Descrição

Tabelas - Substituição de ICMS -  Por Estado

---

## Resumo

- Campos: 77
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTst | String(003) | Não | Código do tipo de ICMS Substituído |
| SigUfs | String(002) | Não | Sigla do estado |
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| AplSub | String(001) | Não | Aplicação da substituição |
| DatIni | Date | Não | Data início de validade da tabela de substituição de impostos |
| CodCrt | Number(001,0) | Não | Código do regime tributário |
| TexTst | String(050) | Sim | Texto para impressão na nota fiscal de saída |
| IcmEst | Number(004,2) | Não | Percentual do imposto do estado |
| RedIcm | Number(008,5) | Sim | Percentual de redução para cálculo do imposto substituído |
| MarLuc | Number(007,4) | Sim | Percentual margem de lucro ou base para cálculo do imposto substituído |
| VlrIpi | String(001) | Não | Indicativo se o valor do IPI está na base do imposto substituído |
| VlrFre | String(001) | Não | Indicativo se o valor do frete está na base do imposto substituído |
| VlrSeg | String(001) | Não | Indicativo se o valor do seguro está na base do imposto substituído |
| VlrEmb | String(001) | Não | Indicativo se o valor das embalagens está na base do imposto substituído |
| VlrEnc | String(001) | Não | Indicativo se o valor dos encargos está na base do imposto substituído |
| VlrOut | String(001) | Não | Indicativo se o valor das outras despesas está na base do imposto substituído |
| EmpTpr | Number(004,0) | Sim | Código da Empresa |
| CodTpr | String(004) | Sim | Tabela de preço base para busca do preço para cálculo imposto |
| CodMsg | Number(004,0) | Sim | Código da mensagem associada ao ICMS substituído |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| StpBas | String(001) | Sim | Indicativo se o valor de Substituição de PIS deve ser somado na base de substituição |
| StcBas | String(001) | Sim | Indicativo se o valor de Substituição de COFINS deve ser somado na base de substituição |
| SomNfs | String(001) | Sim | Soma ou não no total dos documentos (cotação / ordem e pedido / nota de entrada e saída) |
| PerRet | Number(005,2) | Sim | Percentual de retenção de ICMS Substituto |
| GerTit | String(001) | Não | Indicativo se deve ser gerado o título de retenção de ICMS Substituto via N.F.E. |
| DimRet | String(001) | Não | Indicativo se o valor da retenção deve ser diminuído só do valor financeiro, do financeiro e líquido ou não diminuir |
| GerTis | String(001) | Sim | Indicativo se deve ser gerado o título de retenção de ICMS Substituto via N.F.S. |
| DzfBas | String(001) | Sim | Indicativo se o valor de desconto zona franca deve ser subtraído da base de substituição |
| DefBcs | Number(001,0) | Sim | Definição da base de cálculo da substituição |
| DsoIcm | Number(001,0) | Sim | Tipo do desconto do ICMS normal na operação |
| IndMva | String(001) | Sim | Indicativo se considera a variação das alíquotas de ICMS no cálculo da margem de lucro (MVA ajustada) |
| CalStv | String(001) | Sim | Indicativo se calcula ST na saída para produtos com ST calculada na entrada |
| CalBas | String(001) | Sim | Indicativo de como é formada a base de cálculo das substituições |
| PerCtm | Number(004,2) | Sim | Percentual da carga tributária média |
| VlrDar | String(001) | Não | Indicativo se o valor do arredondamento está na base do imposto substituído |
| QtdDec | Number(002,0) | Sim | Quantidade de decimais utilizada para o arredondamento do cálculo da margem |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 associada ao imposto substituído |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 associada ao imposto substituído |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 associada ao imposto substituído |
| VlrFrd | String(001) | Sim | Indicativo se o valor do frete destacado está na base do imposto substituído |
| VlrOud | String(001) | Sim | Indicativo se o valor de outras destacadas está na base do imposto substituído |
| IcmNco | Number(004,2) | Sim | Percentual de ICMS para não contribuinte |
| IcsOut | String(001) | Sim | Considera o valor de ICMS ST como despesa acessória em devoluções de compra |
| VlrIcm | String(001) | Sim | Indicativo se o valor do ICMS normal está na base do imposto substituído |
| VlrIim | String(001) | Sim | Indicativo se o valor do imposto de importação está na base do imposto substituído |
| VlrSei | String(001) | Sim | Indicativo se o valor do seguro de importação está na base do imposto substituído |
| VlrFei | String(001) | Sim | Indicativo se o valor do frete de importação está na base do imposto substituído |
| VlrOui | String(001) | Sim | Indicativo se o valor das outras despesas de importação está na base do imposto substituído |
| VlrPis | String(001) | Sim | Indicativo de como o valor do PIS é considerado na base do imposto substituído |
| VlrCof | String(001) | Sim | Indicativo de como o valor do COFINS é considerado na base do imposto substituído |
| PisImp | String(001) | Sim | Indicativo se o valor do PIS de importação está na base do imposto substituído |
| CofImp | String(001) | Sim | Indicativo se o valor do COFINS de importação está na base do imposto substituído |
| BecIcm | String(001) | Sim | Informa base usada para ICMS efetivamente creditado |
| VlrAim | String(001) | Sim | Indicativo se o valor do AFRMM está na base do ICMS Subtituição |
| BusSep | String(001) | Sim | Busca ICMS substituído pela da entrada do produto |
| PisRbs | String(001) | Sim | Indicativo de como o valor do PIS a recuperar é considerado na base do imposto substituído |
| CofRbs | String(001) | Sim | Indicativo de como o valor do COFINS a recuperar é considerado na base do imposto substituído |
| GuiFcp | String(001) | Sim | Indicativo que deve gerar a guia de FCP separadamente da guia do ICMS ST. |
| IstMin | Number(005,2) | Sim | Percentual mínimo de ICMS Subtituição |
| DesIcm | String(001) | Sim | Desconta o valor de ICMS na base de cálculo de PIS/COFINS ST |
| DifIcs | String(001) | Sim | Calcular DIFAL como ICMS ST para operações de Consumo Próprio ou Imobilizado. |
| TipBda | Number(002,0) | Sim | Tipo da base de cálculo do diferencial de alíquota do ICMS |
| SubEsc | String(001) | Sim | Realizar cálculo do ICMS ST para produtos com produção em escala não relevante |
| RedBda | String(001) | Sim | Indicativo se a Redução do DIFAL deve ser aplicada após o cálculo do ICMS por dentro do estado de destino |
| DesIci | String(001) | Sim | Indicativo se deve descontar o ICMS da operação interestadual na formação da base de cálculo do DIFAL |
| AliBda | Number(001,0) | Sim | Indicativo de qual alíquota deve ser aplicada na formação da base de cálculo do DIFAL |
| FcpDsb | String(001) | Sim | Calcular valor da base FCP ST descontando valor da base de cálculo do ICMS em operação interna |
| CtmFcp | Number(004,2) | Sim | Percentual de Carga Triburária Média para FCP ST |
| MtdIst | Number(002,0) | Sim | Motivo desoneração ICMS-ST |
| DesPis | String(001) | Sim | Desconta o valor do PIS Retido da base ICMS ST |
| DesCos | String(001) | Sim | Desconta o valor do COFINS Retido da base ICMS ST |
| CodTp2 | String(004) | Sim | Segunda Tabela de preço base para busca do preço para cálculo imposto |
| PerTrv | Number(004,2) | Sim | Percentual da Trava do PMPF |
| TipTrv | String(001) | Sim | Indicador de Trava Ajustada para PMPF |

---

## Chave Primária

- CodTst
- SigUfs
- CodEmp
- CodFil
- AplSub
- DatIni
- CodCrt

---

## Índices

### E019SUBIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E019SUB_000

**Tabela:** E019TST

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

### IR_E019SUB_001

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

