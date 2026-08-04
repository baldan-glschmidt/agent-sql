# E440VPR

## Descrição

Compras - Notas Fiscais de Entrada - Valorização

---

## Resumo

- Campos: 34
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqVpr | Number(004,0) | Não | Sequência das valorizações na nota fiscal de entrada |
| SelVpr | Number(001,0) | Sim | Indicativo de seleção da valorização |
| CodPro | String(014) | Sim | Código do produto da nota fiscal de entrada |
| CodDer | String(007) | Sim | Código da derivação do produto da nota fiscal de entrada |
| QtdRec | Number(014,5) | Sim | Quantidade recebida do item da nota fiscal de entrada |
| UniMed | String(003) | Sim | Unidade de medida de estoque do item da nota fiscal de entrada |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item da nota fiscal de entrada |
| NovPro | String(014) | Sim | Novo produto da valorização |
| NovDer | String(007) | Sim | Nova derivação da valorização |
| NovUni | String(003) | Sim | Nova unidade de medida da valorização |
| NovCpl | String(250) | Sim | Novo complemento de descrição do produto da valorização |
| NovDep | String(010) | Sim | Novo código do depósito para entrada de estoque do produto |
| NovQtd | Number(014,5) | Sim | Nova quantidade recebida do item da nota fiscal de entrada |
| NovOri | String(003) | Sim | Nova origem do produto da valorização |
| SeqIpc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |
| SeqIte | Number(004,0) | Sim | Sequência ligação das valorizações na nota fiscal de entrada |
| CplIpc | String(250) | Sim | Complemento da descrição do produto |
| TnsPro | String(005) | Sim | Transação de produto do item da nota fiscal de entrada |
| CodDep | String(010) | Sim | Código do depósito para entrada de estoque do produto |
| CodFam | String(006) | Sim | Código da família do produto |
| TnsEst | String(005) | Sim | Transação de movimentação de estoque para o produto do item |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra |
| SeqIso | Number(004,0) | Sim | Sequencia do item de serviço da ordem de compra |
| EmpNfv | Number(004,0) | Sim | Código da empresa da nota fiscal de saída |
| FilNfv | Number(005,0) | Sim | Código da filial da nota fiscal de saída |
| SnfNfv | String(003) | Sim | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item da nota fiscal de saída |
| FilOcp | Number(005,0) | Sim | Código da filial da ordem de compra |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqVpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440VPR_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

