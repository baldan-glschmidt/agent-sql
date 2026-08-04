# E055PAR

## Descrição

Tabelas - Impostos - Parâmetros dos Impostos por Filial

---

## Resumo

- Campos: 48
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| UsaBru | String(001) | Não | Indicativo se usa ou não o faturamento bruto calculado |
| TemVas | String(001) | Não | Indicativo se permite valores adicionais e de exclusão p/ formação da base de cálculo |
| CodPri | String(001) | Não | Código da periodicidade de apuração/cálculo do imposto |
| DiaVct | Number(003,0) | Sim | Quantidade de dias após data apuração final para vencimento |
| AntPos | String(001) | Não | Indicativo do critério de definição de vencimento do imposto |
| CodDrf | Number(006,0) | Sim | Código para documento de arrecadação |
| VlrMin | Number(015,2) | Sim | Valor mínimo do imposto a ser gerado |
| TipAcu | String(001) | Sim | Indicativo se acumula ou não o imposto até atingir o valor mínimo |
| VlrAcu | Number(015,2) | Sim | Valor acumulado do imposto a ser comparado com valor mínimo |
| UltDba | Date | Sim | Última data base utilizada nos parâmetros de formação da base de cálculo |
| CtaDev | Number(007,0) | Sim | Conta contábil devedora |
| CtaCre | Number(007,0) | Sim | Conta contábil credora |
| CtaFdv | Number(007,0) | Sim | Conta financeira devedora |
| CtaFcr | Number(007,0) | Sim | Conta financeira credora |
| ImpPad | String(001) | Não | Indicativo se o código de imposto é padrão para o seu tipo de imposto |
| PagFil | Number(005,0) | Sim | Filial padrão para gerar título de imposto a pagar no financeiro |
| PagFor | Number(009,0) | Sim | Fornecedor padrão para gerar título de imposto a pagar no financeiro |
| PagTti | String(003) | Sim | Tipo de título padrão para geração do título de imposto a pagar no financeiro |
| PagTri | String(005) | Sim | Transação padrão para geração do título de imposto a pagar no financeiro |
| AutFin | String(001) | Sim | Indicativo se gera título automaticamente no cálculo do imposto |
| ImpPai | String(003) | Sim | Código do imposto pai |
| TipFat | String(001) | Sim | Tipo de faturamento a considerar na base de cálculo do imposto |
| IniCon | Number(001,0) | Sim | Critério de início de contagem dos dias de vencimento |
| AtuGri | String(001) | Sim | Atualiza guias de recolhimento de imposto |
| CodGri | Number(004,0) | Sim | Código da guia de recolhimento |
| ValTtr | Number(001,0) | Sim | Campo de busca da tabela de tributação |
| CodFct | String(005) | Sim | Código da forma de contabilização |
| OriCal | String(001) | Sim | Origem dos valores base para cálculo |
| ComImp | String(001) | Sim | Composição gerada para base de cálculo ou imposto a recolher |
| ApuImp | String(001) | Sim | Indicativo se o imposto permite a sua apuração |
| ConApu | Number(002,0) | Sim | Código da contribuição social apurada (tabela 4.3.5 do SPED Pis/Cofins) |
| CodFcc | String(005) | Sim | Código da forma de contabilização do crédito |
| DatIni | Date | Sim | Data inicial para entrada de títulos no regime de caixa |
| VlrMpa | Number(015,2) | Sim | Valor mínimo para parcelar o imposto |
| QtdPar | Number(003,0) | Sim | Quantidade de parcelas para parcelar o imposto |
| UtiAcu | String(001) | Sim | Forma que o Valor Acumulado será lançado na apuração do imposto |
| RegApu | Number(001,0) | Sim | Regime de Apuração do imposto |
| SerEmi | String(001) | Sim | Realizar a apuração do imposto baseado na data de execução do serviço |
| IdeTan | Number(009,0) | Sim | Tabela Alq. Nom. simples por estado |
| TipCmr | String(001) | Sim | Tipo de Comércio |
| MetApu | Number(001,0) | Sim | Método Apuração ISS Próprio Inst. Financeiras |
| TipCal | String(001) | Sim | Tipo de Cálculo do ISS Próprio Inst. Financeiras |
| TipCom | Number(001,0) | Sim | Tipo Compensação |
| ParCre | Number(003,0) | Sim | Parcelamento do Crédito |
| RecIss | String(001) | Sim | Recalcular ISS agrupado por Alíquota |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp

---

## Índices

### E055PARIndice1

**Tipo:** Não unico

Campos:
- CodImp

---

## Relacionamentos

### IR_E055PAR_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E055PAR_002

**Tabela:** E051IMP

| Origem | Destino |
|--------|---------|
| CodImp | CodImp |

