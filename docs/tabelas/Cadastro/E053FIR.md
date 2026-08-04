# E053FIR

## Descrição

Cadastros - Tributos - Formação Faturamento IRPJ e CSLL

---

## Resumo

- Campos: 30
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| DatBas | Date | Não | Mês e ano base inicial de validade para formação do faturamento bruto |
| CodTns | String(005) | Não | Código da transação |
| TipApl | Number(001,0) | Não | Tipo de aplicação |
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
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- DatBas
- CodTns
- TipApl

---

## Índices

### E053FIRIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns

---

## Relacionamentos

### IR_E053FIR_002

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

