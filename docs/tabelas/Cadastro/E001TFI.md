# E001TFI

## Descrição

Tabelas - Transações - Financeiro

---

## Resumo

- Campos: 44
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| PagTco | String(001) | Sim | Indicativo se a transação gera título de Cofins |
| PagTpi | String(001) | Sim | Indicativo se a transação gera título de PIS |
| PagTcl | String(001) | Sim | Indicativo se a transação gera título de CSLL |
| PagTor | String(001) | Sim | Indicativo se a transação gera título de Outras Retenções |
| PagVbn | String(001) | Sim | Formação do valor base para cálculo do INSS nas comissões |
| PagTin | String(001) | Sim | Indicativo se a transação é de INSS |
| PagHro | String(001) | Sim | Indicativo se a transação herda o rateio da origem |
| PagGin | String(001) | Sim | Indicativo se a transação gera título de INSS |
| PagGis | String(001) | Sim | Indicativo se a transação gera título de  ISS |
| RecRco | String(001) | Sim | Indicativo se a transação retêm Cofins na baixa |
| RecPco | Number(004,2) | Sim | Percentual de Cofins a ser retido na baixa do título |
| RecRpi | String(001) | Sim | Indicativo se a transação retêm PIS na baixa do título |
| RecPpi | Number(004,2) | Sim | Percentual de PIS a ser retido na baixa do título |
| RecRcl | String(001) | Sim | Indicativo se a transação retêm CSLL na baixa do título |
| RecPcl | Number(004,2) | Sim | Percentual de CSLL a ser retido na baixa do título |
| RecRro | String(001) | Sim | Indicativo se a transação retêm Outras Retenções na baixa do título |
| RecPro | Number(004,2) | Sim | Percentual de Outras Retenções a ser retido na baixa do título |
| RecHro | String(001) | Sim | Indicativo se a transação herda o rateio da origem |
| CxbTte | String(001) | Sim | Indicativo se a transação é de transferência  eletrônica |
| CxbHro | String(001) | Sim | Indicativo se a transação herda o rateio da origem |
| CxbAtu | Number(002,0) | Sim | Atualiza aplicação/captação de recursos |
| CxbBlq | String(001) | Sim | Indicativo se soma saldo bloqueado  na conta interna |
| TptFre | String(003) | Sim | Tipo de título gerado no contas a pagar referente aos títulos de frete |
| RecRir | String(001) | Sim | Indicativo se a transação retêm Imposto de Renda na baixa |
| RecPir | Number(007,5) | Sim | Percentual de Imposto de Renda a ser retido na baixa do título |
| RecTic | String(001) | Sim | Indicativo se a transação é de cartão de crédito/débito |
| ObrTxf | String(001) | Sim | Indicativo se é obrigatória a ligação transação X conta financeira |
| RedBas | String(001) | Sim | Indicativo se a transação de entrada de título reduz base de IRRF |
| PerRba | Number(005,2) | Sim | Percentual de redução de base de IRRF |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| RenSub | String(001) | Sim | Indicativo renegociação gera comissão na substituição de títulos |
| VcaPas | String(001) | Sim | Indica se a variação cambial é passiva |
| VcaAti | String(001) | Sim | Indica se a variação cambial é ativa |
| IdeRen | Number(009,0) | Sim | Identificador do Registro da Natureza de Rendimento |
| NatRen | String(009) | Sim | Natureza Rendimentos |
| CxbLpr | Number(001,0) | Sim | Tipo de lançamento para Livro Caixa Digital do Produtor Rural |
| IntAcp | String(001) | Sim | Habilitar integração com Antecipação Contas a Pagar |
| SemRet | String(001) | Sim | Operação tributável sem retenção - REINF |
| AdtTit | String(001) | Sim | Indicativo se o título criado via pedido pode ser adiantado |
| LibPed | String(001) | Sim | Indicativo se pedido deve ser liberado automaticamente após baixa do título |
| BloPed | String(001) | Sim | Indicativo se pedido deverá ser bloqueado ao gerar título |

---

## Chave Primária

- CodEmp
- CodTns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
