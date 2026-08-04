# E049TTR

## Descrição

Tabelas - Tributos - Tabela de Tributação

---

## Resumo

- Campos: 43
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodImp | String(003) | Não | Código do imposto |
| DatCpt | Date | Não | Mês e ano de competência |
| CodAgf | String(005) | Não | Código do grupo fiscal |
| SeqTtr | Number(003,0) | Não | Sequência da faixa da tabela de tributação por grupo fiscal |
| VlrFax | Number(015,2) | Sim | Valor limite máximo da faixa da tabela de tributação |
| PerBas | Number(005,2) | Sim | Percentual para cálculo do valor base do imposto |
| PerImp | Number(008,4) | Sim | Percentual do imposto |
| VlrAbt | Number(015,2) | Sim | Valor do abatimento sobre o imposto válido para a faixa |
| DatVal | Date | Sim | Data de validade da seqüência de valores |
| AcAbat | String(001) | Sim | Indicativo se acumula mensalmente o valor do abatimento no cálculo/apuração do imposto |
| PerSer | Number(005,2) | Sim | Percentual do imposto considerando participação dos serviços no faturamento |
| Profax | Number(008,2) | Sim | Percentual da proporção limite máxima da faixa da tabela de tributação |
| PerAdi | Number(007,4) | Sim | Percentual adicional do imposto |
| CodTre | Number(004,0) | Sim | Tipo de remessa para o exterior do contrato de aplicação\captação de recursos |
| PerIre | Number(004,2) | Sim | Percentual do IRPJ |
| PerCsl | Number(004,2) | Sim | Percentual do CSLL |
| PerCof | Number(008,4) | Sim | Percentual do COFINS |
| PerPis | Number(008,4) | Sim | Percentual do PIS/PASEP |
| PerCpp | Number(004,2) | Sim | Percentual de contribuição patronal previdenciária |
| PerIcm | Number(005,2) | Sim | Percentual do ICMS |
| PerIpi | Number(008,4) | Sim | Percentual de IPI |
| PerIss | Number(006,4) | Sim | Percentual do ISS |
| DedAlq | String(001) | Sim | Deduzir da alíquota efetiva o percentual do ICMS/ISS |
| DedIrp | String(001) | Sim | Deduzir da alíquota efetiva o percentual do IRPJ |
| DedCsl | String(001) | Sim | Deduzir da alíquota efetiva o percentual do CSLL |
| DedCof | String(001) | Sim | Deduzir da alíquota efetiva o percentual do COFINS |
| DedPis | String(001) | Sim | Deduzir da alíquota efetiva o percentual do PIS |
| DedIpi | String(001) | Sim | Deduzir da alíquota efetiva o percentual do IPI |
| DedCpp | String(001) | Sim | Deduzir da alíquota efetiva o percentual do CPP |
| RetIrf | String(001) | Sim | Considerar o valor de retenção do imposto do IRRF das notas fiscais |
| RetCsl | String(001) | Sim | Considerar o valor de retenção do imposto do CSLL das notas fiscais |
| RetCof | String(001) | Sim | Considerar o valor de retenção do imposto do COFINS das notas fiscais |
| RetPis | String(001) | Sim | Considerar o valor de retenção do imposto do PIS das notas fiscais |
| RetIss | String(001) | Sim | Considerar o valor de retenção do imposto do ISS das notas fiscais |
| ImpIcm | String(003) | Sim | Código do imposto Simples para alíq. ICMS/ISS |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| DatGer | Date | Sim | Data de geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Código do usuário responsável pela última atualização do registro |
| DatAtu | Date | Sim | Data da última atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da última atualização do registro |
| PerFaf | Number(008,4) | Sim | Percentual do fator de ajuste de fruição |

---

## Chave Primária

- CodEmp
- CodImp
- DatCpt
- CodAgf
- SeqTtr

---

## Índices

### E049TTRIndice1

**Tipo:** Não unico

Campos:
- CodImp

---

## Relacionamentos

### IR_E049TTR_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E049TTR_001

**Tabela:** E051IMP

| Origem | Destino |
|--------|---------|
| CodImp | CodImp |

