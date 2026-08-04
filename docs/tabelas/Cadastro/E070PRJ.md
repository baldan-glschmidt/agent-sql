# E070PRJ

## Descrição

Cadastros - Filiais - Parâmetros do Controle de Projetos

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
| PrjCta | String(005) | Sim | Critério de rateio para as contas e centros de custos |
| NumPpp | Number(008,0) | Sim | Número do projeto padrão para projetos para efeito de rateio |
| CodFpp | Number(004,0) | Sim | Código da fase do projeto padrão para efeito de rateio |
| FinCrp | Number(007,0) | Sim | Conta financeira de receita padrão para efeito de rateio |
| FinCdp | Number(007,0) | Sim | Conta financeira de despesa padrão para efeito de rateio |
| CcuCpp | String(009) | Sim | Código do centro de custo padrão para efeito de rateio |
| NumPpe | Number(008,0) | Sim | Número do projeto padrão para estoques ao gerar solicitação de compras a partir da requisição |
| CodFpe | Number(004,0) | Sim | Código da fase do projeto para estoques ao gerar solicitação de compras a partir da requisição |
| FinCpe | Number(007,0) | Sim | Conta financeira para estoques ao gerar solicitação de compras a partir da requisição |
| CtaRpe | Number(007,0) | Sim | Conta contábil reduzida para estoques ao gerar solicitação de compras a partir da requisição |
| CcuCpe | String(009) | Sim | Código do centro de custo para estoques ao gerar solicitação de compras a partir da requisição |
| DatFes | Date | Sim | Data final do fechamento de estoque |
| RcpEst | String(001) | Sim | Rodar conciliação de projetos para o estoque |
| CtrCpr | String(001) | Sim | Tipo de regime de entrada nos contratos de compra |
| CtrVen | String(001) | Sim | Tipo de regime de entrada nos contratos de venda |
| DatFcc | Date | Sim | Data do período de fechamento dos contratos de compra |
| DatFcv | Date | Sim | Data do período de fechamento dos contratos de venda |
| OrcQtd | String(001) | Sim | Orça quantidade nos recursos previstos |
| RegApr | String(020) | Sim | Regra para controle de aprovação. |
| RegAmn | Number(001,0) | Sim | Tipo de regime do orçamento para a aprovação multinível |
| ConOze | String(001) | Sim | Consiste orçamentos zerados |
| OrcIni | Date | Sim | Data inicial do período para realizar orçamentos |
| OrcFim | Date | Sim | Data final do período para realizar orçamentos |
| TsoIni | Date | Sim | Data inicial do período para realizar transferências de saldos de orçamentos |
| TsoFim | Date | Sim | Data final do período para realizar transferências de saldos de orçamentos |
| LctMan | String(001) | Sim | Gera lançamento manual na aprovação |
| GerFin | String(001) | Sim | Gera orçamento financeiro a partir do orçamento físico |
| ClaFpj | String(001) | Sim | Utiliza classificação fase |
| BloOcp | Number(001,0) | Sim | Bloqueio ordem de compra |
| TotOrc | String(001) | Sim | Totaliza orçamento sintético a partir do orçamento analítico |
| BloAgr | String(001) | Sim | Mostra bloqueio orçamentário agrupado |
| TnsRrp | String(005) | Sim | Transação padrão para reconhecer receita (IFRS/POC) positiva |
| TnsRrn | String(005) | Sim | Transação padrão para reconhecer receita (IFRS/POC) negativa |

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
