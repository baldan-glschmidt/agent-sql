# E140TAX

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Produtos - Taxas

---

## Resumo

- Campos: 30
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item de produto na nota fiscal de saída |
| CodItx | Number(004,0) | Não | Código do item de taxa |
| TipPtx | Number(001,0) | Não | Tipo da taxa |
| DatIni | Date | Não | Data Inicial da Vigência |
| DatFim | Date | Não | Data Final da Vigência |
| VlrPtx | Number(018,5) | Sim | Valor da taxa para os tipos (1-Valor e 2-Valor por Peso) |
| PerPtx | Number(007,4) | Sim | Percentual da taxa para o tipo (3-Percentual) |
| DiaCar | Number(004,0) | Sim | Dias de carência |
| DiaPrd | Number(004,0) | Sim | Dias de periodicidade |
| AplPtx | Number(001,0) | Não | Aplicação da taxa |
| VlrTax | Number(015,2) | Sim | Valor da taxa calculado |
| IndVcr | String(001) | Não | Indicativo se o valor da taxa foi calculado por regra do usuário |
| IndVau | String(001) | Não | Indicativo se o valor da taxa foi alterado pelo usuário |
| IndGtt | String(001) | Não | Indicativo se gera título de taxa |
| FilTax | Number(005,0) | Sim | Código da filial do título gerado |
| NumTax | String(010) | Sim | Número do título gerado |
| TptTax | String(003) | Sim | Tipo de título da taxa gerado |
| TnsTax | String(005) | Sim | Código da transação do título gerado |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| QtdTax | Number(014,5) | Sim | Quantidade de taxa descontada em produto |
| IndTpr | String(001) | Sim | Indicativo se gera taxa em produto |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv
- CodItx
- TipPtx
- DatIni
- DatFim

---

## Índices

### E140TAXIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodItx

---

## Relacionamentos

### IR_E140TAX_004

**Tabela:** E140IPV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIpv | SeqIpv |

### IR_E140TAX_005

**Tabela:** E113ITX

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodItx | CodItx |

