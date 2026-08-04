# E055FIP

## Descrição

Tabelas - Impostos - Parâmetro Financeiro/Patrimônio Formação Base Impostos

---

## Resumo

- Campos: 18
- Chave Primária: 8 campo(s)
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
| CodTns | String(005) | Não | Código da transação |
| CodCli | Number(009,0) | Não | Código do cliente para filtrar o título no financeiro |
| CodFor | Number(009,0) | Não | Código do fornecedor para filtrar o título no financeiro |
| CodTpt | String(003) | Não | Tipo de título para filtrar título de imposto no financeiro |
| VlrMov | String(001) | Não | Opção do cálculo a ser efetuado com o valor do movimento financeiro |
| VlrJur | String(001) | Não | Opção do cálculo a ser efetuado com o valor dos juros |
| VlrMul | String(001) | Não | Opção do cálculo a ser efetuado com o valor da multa |
| VlrCmo | String(001) | Não | Opção do cálculo a ser efetuado com o valor da correção monetária |
| VlrEnc | String(001) | Não | Opção do cálculo a ser efetuado com o valor dos encargos |
| VlrOac | String(001) | Não | Opção do cálculo a ser efetuado com o valor de outros acréscimos |
| VlrPat | String(001) | Não | Opção do cálculo a ser efetuado com o valor do movimento do Patrimônio |
| VlrDsc | String(001) | Não | Opção do cálculo a ser efetuado com o valor do desconto |
| SepOdc | String(001) | Sim | Indicativo se devem ser gerados dois outros documentos, sendo um para Multa e outro para Juros |
| MovAdi | String(001) | Sim | Indicativo se o movimento a ser integrado é relativo a um adiantamento do contas a receber |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- CodTns
- CodCli
- CodFor
- CodTpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055FIP_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

