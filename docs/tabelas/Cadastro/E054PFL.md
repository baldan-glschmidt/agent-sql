# E054PFL

## Descrição

Tabelas - Impostos - Parâmetros Formação Faturamento Líquido Mês

---

## Resumo

- Campos: 23
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| DatBas | Date | Não | Mês e ano base inicial de validade para formação do faturamento líquido |
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
| VlrDsc | String(001) | Sim | Opção do cálculo a ser efetuado com o valor do desconto |
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
- DatBas
- CodTns

---

## Índices

### E054PFLIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns

---

## Relacionamentos

### IR_E054PFL_001

**Tabela:** E054FFL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| DatBas | DatBas |

### IR_E054PFL_002

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

