# E140PVD

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Produtos - Diversos

---

## Resumo

- Campos: 76
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| IcmBfc | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza na UF de destino |
| BasFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza |
| AliFcp | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza |
| VlrFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza |
| BstFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza retido por substituição tributária |
| AstFcp | Number(007,4) | Sim | Alíquota do fundo de combate à pobreza retido por substituição tributária |
| VstFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza retido por substituição tributária |
| BreFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza retido ant. por subst. trib. |
| AreFcp | Number(007,4) | Sim | Alíquota do fundo de combate à pobreza retido anteriormente por subst. trib. |
| VreFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza retido anteriormente por subst. trib. |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| VlrRas | Number(015,2) | Sim | Valor do acréscimo rateado do subtotal |
| VlrRds | Number(015,2) | Sim | Valor do desconto rateado do subtotal |
| VlrBgi | Number(015,2) | Sim | Base de cálculo do GILRAT |
| PerGil | Number(004,2) | Sim | Percentual de GILRAT - Grau Incid. Incapac. Laborat. Decor. Riscos Amb. de Trab. |
| VlrGil | Number(015,2) | Sim | Valor do GILRAT |
| CodDev | Number(012,0) | Sim | Código de Lançamento no SisDev |
| DatDev | Date | Sim | Data de Lançamento no SisDev |
| CanDev | String(100) | Sim | Motivo Cancelamento no SisDev |
| VicStd | Number(015,2) | Sim | Valor do ICMS-ST desonerado |
| MtdIst | Number(002,0) | Sim | Motivo desoneração ICMS-ST |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| VdiFcp | Number(015,2) | Sim | Valor diferido do ICMS relativo ao FCP |
| EfiFcp | Number(015,2) | Sim | Valor efetivo do ICMS relativo ao FCP |
| VlrDev | Number(015,2) | Sim | Valor da devolução do item para acerto |
| QtmBic | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico |
| VmoIcm | Number(015,2) | Sim | Valor do ICMS Monofásico |
| AliImo | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico |
| QtmBir | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Retido |
| VmoIcr | Number(015,2) | Sim | Valor do ICMS Monofásico Retido |
| AliImr | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Retido |
| QtmBif | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Diferido |
| VmoIcf | Number(015,2) | Sim | Valor do ICMS Monofásico Diferido |
| AliImf | Number(007,4) | Sim | Percentual de Diferimento do ICMS Monofásico |
| QtmBid | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Destacado |
| VmoIcd | Number(015,2) | Sim | Valor do ICMS Monofásico Destacado |
| AliImd | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Destacado |
| AliMor | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Original |
| CbfRbc | String(010) | Sim | Código de Benefício Fiscal de redução de base de cálculo |
| AliFus | Number(005,2) | Sim | Percentual do FUST |
| BasFus | Number(015,2) | Sim | Base de Cálculo do FUST |
| VlrFus | Number(015,2) | Sim | Valor do FUST |
| AliFnt | Number(005,2) | Sim | Percentual do FUNTTEL |
| BasFnt | Number(015,2) | Sim | Base de Cálculo do FUNTTEL |
| VlrFnt | Number(015,2) | Sim | Valor do FUNTTEL |
| CnpjLD | Number(014,0) | Sim | Informar o CNPJ da operadora LD que irá lançar o item de cofaturamento em nota do tipo faturamento 2 |
| DocIdeLD | String(014) | Sim | Informar o CNPJ da operadora LD que irá lançar o item de cofaturamento em nota do tipo faturamento 2 |
| SnfNfr | String(003) | Sim | Série da nota fiscal de saída |
| NumNfr | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpr | Number(003,0) | Sim | Sequência do item da nota fiscal de saída |
| CodNfc | String(007) | Sim | Código item cClass |
| PerImo | Number(007,4) | Sim | Proporção Transmitida do Imóvel |
| IndTor | String(001) | Sim | Indicador de Torna |
| ImoTor | String(020) | Sim | Imóveis transmitidos junto com a torna |
| VlrTor | Number(015,2) | Sim | Valor da Torna |
| VlrIRe | Number(015,2) | Sim | Valor Inicial do Redutor de Ajuste |
| VlrItb | Number(015,2) | Sim | Valor do ITBI |
| VlrLau | Number(015,2) | Sim | Valor Laudêmio |
| VlrOne | Number(015,2) | Sim | Valores despendidos a título de outorga onerosa do direito de construir, de outorga onerosa por alteração de uso |
| DemCon | Number(015,2) | Sim | Demais contrapartidas de ordem urbanística e ambientais pagas ou entregues aos entes públicos em virtude de legislação federal, estadual ou municipal |
| VlrRed | Number(015,2) | Sim | Valor do Redutor de Ajuste Imóvel |
| IReSoc | String(001) | Sim | Indicador de Redutor Social |
| TipIns | String(002) | Sim | Tipo de instrumento |
| DesIns | String(060) | Sim | Descrição dos outros instrumentos |
| DatIns | Date | Sim | Data do instrumento |
| LimMin | Number(014,5) | Sim | Teto legal/estatutário redutor social Individual |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv

---

## Índices

### E140IPVIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodDev

### E140PVDIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- SnfNfr
- NumNfr
- SeqIpr

---

## Relacionamentos

Nenhum relacionamento cadastrado.
