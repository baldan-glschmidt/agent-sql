# E055RDE

## Descrição

Detalhamento das Receitas/Deduções e Exclusões PIS/COFINS

---

## Resumo

- Campos: 28
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodDet | String(060) | Não | Código de detalhamento |
| DatCpt | Date | Não | Competência |
| SeqCon | Number(009,0) | Não | Sequência |
| IndMov | Number(001,0) | Não | Tipo movimento |
| PerRat | Number(005,2) | Sim | Percentual do rateio |
| CodTns | String(255) | Sim | Código da transação |
| CodPro | String(255) | Sim | Código do produto |
| CodSer | String(255) | Sim | Código do serviço |
| CodCst | String(255) | Sim | Código da situação tributária |
| AliPis | Number(015,4) | Sim | Alíquota de PIS |
| AliCof | Number(015,4) | Sim | Alíquota de COFINS |
| VlrCtb | String(001) | Não | Opção do cálculo a ser efetuado com o valor contábil |
| VlrIpi | String(001) | Não | Opção do cálculo a ser efetuado com o valor do IPI |
| VlrIrf | String(001) | Não | Opção do cálculo a ser efetuado com o valor do IRRF |
| VlrIss | String(001) | Não | Opção do cálculo a ser efetuado com o valor do ISS |
| VlrIns | String(001) | Não | Opção do cálculo a ser efetuado com o valor do INSS |
| VlrSic | String(001) | Não | Opção do cálculo a ser efetuado com o valor do ICMS substituído |
| VlrCrt | String(001) | Não | Opção do cálculo a ser efetuado com o valor do COFINS retido |
| VlrPit | String(001) | Não | Opção do cálculo a ser efetuado com o valor do PIS retido |
| VlrCsl | String(001) | Não | Opção do cálculo a ser efetuado com o valor do CSLL retido |
| VlrOur | String(001) | Não | Opção do cálculo a ser efetuado com o valor de outras retenções |
| VlrDsc | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do desconto |
| VstFcp | String(001) | Sim | Opção do cálculo a ser efetuado com o valor da Substituição Tributária do FCP |
| VlrStp | String(001) | Sim | Opção do cálculo a ser efetuado com o valor da Substituição Tributária do Pis |
| VlrStc | String(001) | Sim | Opção do cálculo a ser efetuado com o valor da Substituição Tributária do Cofins |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |

---

## Chave Primária

- CodEmp
- CodFil
- CodDet
- DatCpt
- SeqCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055RDE_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E055RDE_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

