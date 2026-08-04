# E055ISS

## Descrição

Impostos - Parâmetros por Cidade ISS do ISS Retido

---

## Resumo

- Campos: 29
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| CodRai | Number(007,0) | Não | Código da cidade RAIS utilizada para apuração do ISS Retido |
| SeqOrd | Number(004,0) | Não | Ordem preferencial do cálculo por cidade ISS |
| DiaVct | Number(003,0) | Sim | Quantidade de dias após data apuração final para vencimento |
| IniCon | Number(001,0) | Sim | Critério de início de contagem dos dias de vencimento |
| AntPos | String(001) | Não | Indicativo do critério de definição de vencimento do imposto |
| CodDrf | Number(006,0) | Sim | Código para documento de arrecadação |
| VlrMin | Number(015,2) | Sim | Valor mínimo do imposto a ser gerado |
| TipAcu | String(001) | Sim | Indicativo se acumula ou não o imposto até atingir o valor mínimo |
| VlrAcu | Number(015,2) | Sim | Valor acumulado do imposto a ser comparado com valor mínimo |
| UltDba | Date | Sim | Última data base utilizada nos parâmetros de formação da base de cálculo |
| CtaDev | Number(007,0) | Sim | Conta contábil devedora |
| CtaCre | Number(007,0) | Sim | Conta contábil credora |
| CodFor | Number(009,0) | Sim | Código do Fornecedor |
| CodTpt | String(003) | Sim | Tipo de título padrão para geração do título de imposto a pagar no financeiro |
| CodTns | String(005) | Sim | Transação padrão para geração do título de imposto a pagar no financeiro |
| AutFin | String(001) | Sim | Indicativo se gera título automaticamente no cálculo do imposto |
| AtuGri | String(001) | Sim | Atualiza guias de recolhimento de imposto |
| CodGri | Number(004,0) | Sim | Código da guia de recolhimento |
| CodFct | String(005) | Sim | Código da forma de contabilização |
| TipRet | String(001) | Sim | Indicativo do tipo de apuração ou retenção do ISS |
| TipCom | Number(001,0) | Sim | Tipo de Compensação |
| ParCre | Number(003,0) | Sim | Parcelamento do Crédito |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- CodRai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055ISS_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

