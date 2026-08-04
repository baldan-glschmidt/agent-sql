# E055RCX

## Descrição

Cadastros - Tributos - Parâmetros regime de caixa / financeiro

---

## Resumo

- Campos: 23
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
| SeqRcx | Number(003,0) | Não | Sequencial de parametrização do imposto |
| CodTns | String(005) | Não | Código da transação |
| CodPrt | Number(009,0) | Sim | Participante para filtrar título de imposto no financeiro |
| CodTpt | String(003) | Sim | Tipo de título para filtrar título de imposto no financeiro |
| VlrMov | String(001) | Não | Opção do cálculo a ser efetuado com o valor do movimento financeiro |
| VlrJur | String(001) | Não | Opção do cálculo a ser efetuado com o valor dos juros |
| VlrMul | String(001) | Não | Opção do cálculo a ser efetuado com o valor da multa |
| VlrCmo | String(001) | Não | Opção do cálculo a ser efetuado com o valor da correção monetária |
| VlrEnc | String(001) | Não | Opção do cálculo a ser efetuado com o valor dos encargos |
| VlrDsc | String(001) | Não | Opção do cálculo a ser efetuado com o valor do desconto |
| VlrIrf | String(001) | Não | Opção do cálculo a ser efetuado com o valor do IRF |
| VlrIss | String(001) | Não | Opção do cálculo a ser efetuado com o valor do ISS |
| VlrIns | String(001) | Não | Opção do cálculo a ser efetuado com o valor do INSS |
| VlrPis | String(001) | Não | Opção do cálculo a ser efetuado com o valor do PIS |
| VlrCof | String(001) | Não | Opção do cálculo a ser efetuado com o valor do cofins |
| VlrCsl | String(001) | Não | Opção do cálculo a ser efetuado com o valor do CSLL |
| VlrOur | String(001) | Não | Opção do cálculo a ser efetuado com o valor de outras retenções |
| VlrSic | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do ICMS ST da nota fiscal |
| VlrIpi | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do IPI da nota fiscal |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- SeqRcx

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055RCX_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

