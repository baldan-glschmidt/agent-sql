# E070EST

## Descrição

Cadastros - Filiais - Parâmetros Estoques

---

## Resumo

- Campos: 35
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| MovEmb | String(001) | Sim | Indicativo se baixa estoque de embalagens |
| TnsBae | String(005) | Sim | Transação baixa de estoque de embalagens |
| DepDis | String(010) | Sim | Código do depósito distribuidor |
| IprInv | String(001) | Sim | Indicativo se permite incluir produto não existente no inventário |
| IndRep | String(001) | Sim | Indicativo se o processo de análise de reposição está em execução para esta filial |
| IndOti | String(001) | Sim | Indicativo se a respectiva filial foi inicializada para buscar os saldos de estoque de forma otimizada |
| CriFer | Number(001,0) | Sim | Critério de formação de estoques para geração de remessas |
| MoeCm1 | String(003) | Sim | Moeda entrangeira para a conversão do valor do movimento de estoque 1 |
| MoeCm2 | String(003) | Sim | Moeda entrangeira para a conversão do valor do movimento de estoque 2 |
| UlpVm1 | Date | Sim | Último período de valorização para multi-moeda 1 |
| UlpVm2 | Date | Sim | Último período de valorização para multi-moeda 2 |
| VmaBal | String(001) | Sim | Valor para o movimento de ajuste de balança |
| BnrReq | String(001) | Sim | Tipo de busca da numeração para novas requisições |
| MovFre | String(001) | Sim | Indicativo se a filial aceitará movimentos de estoque de frete quando o saldo do produto estiver zerado |
| CalIcm | String(001) | Sim | Indicativo se a filial fará o cálculo de icms nos movimentos de estoque |
| UltQbt | Date | Sim | Data da última execução da rotina de quebra técnica |
| EstMfd | String(001) | Sim | Indicativo se considera a ligação de filial x depósito p/ movimentação |
| UltIsm | Date | Sim | Último mês de inicialização de saldos mensais |
| EstTdr | String(005) | Sim | Transação padrão para devolução de requisição de estoques |
| TdpReq | String(001) | Sim | Indicativo se obriga a utilização da transação padrão na requisição |
| IndAqt | String(001) | Sim | Indica se permite alterar a qtde. que se deseja transf. para outros depósitos |
| TrfPer | String(001) | Sim | Transf. entre prod. devem ratear o valor do movimento com base no percentual. |
| EspCfo | String(001) | Sim | Considera saldo consignado a fornecedor no cálculo do saldo de estoque próprio |
| EspCcl | String(001) | Sim | Considera saldo consignado a cliente no cálculo do saldo de estoque próprio |
| ConQan | String(001) | Sim | Indicativo se deve consistir quantidade anterior do depósito no movimento |
| EstTni | String(005) | Sim | Transação padrão para Nota Fiscal de Entrada por Inventário |
| EstSni | String(003) | Sim | Série padrão para Nota Fiscal de Entrada por Inventário |
| ForPni | Number(009,0) | Sim | Fornecedor padrão para Nota Fiscal de Entrada por Inventário |
| EstTns | String(005) | Sim | Transação padrão para Nota Fiscal de Saída por Inventário |
| EstSns | String(003) | Sim | Série padrão para Nota Fiscal de Saída por Inventário |
| CliPne | Number(009,0) | Sim | Cliente padrão para Nota Fiscal de Saída por Inventário |
| TnsDpe | String(005) | Sim | Transação padrão nota fiscal saída débito finalidade 7 - Perda em Estoque por Inventário |
| VlrCon | String(001) | Sim | Valorização de Estoque Consignado na Inicialização de Saldos Mensais |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
