# E055FVB

## Descrição

Tabelas - Impostos - Parâmetro Formação Base Impostos

---

## Resumo

- Campos: 26
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| CodTns | String(005) | Não | Código da transação |
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
| ExcFis | String(001) | Sim | Indicativo da transação para uma exceção fiscal conforme lei 12.546/2011 |
| VlrDsc | String(001) | Não | Opção do cálculo a ser efetuado com o valor do desconto |
| VlrFre | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do frete |
| VlrSeg | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do seguro |
| VlrOut | String(001) | Sim | Opção do cálculo a ser efetuado com o valor de outras depesas acessórias |
| VstFcp | String(001) | Sim | Opção do cálculo a ser efetuado com o valor da Substituição Tributária do FCP |
| VlrStp | String(001) | Sim | Opção do cálculo a ser efetuado com o valor da Substituição Tributária do Pis |
| VlrStc | String(001) | Sim | Opção do cálculo a ser efetuado com o valor da Substituição Tributária do Cofins |
| VlrCbs | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do CBS |
| VlrIbu | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do IBS estado |
| VlrIbm | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do IBS município |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- CodTns

---

## Índices

### E055FVBIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns

---

## Relacionamentos

### IR_E055FVB_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

### IR_E055FVB_004

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

