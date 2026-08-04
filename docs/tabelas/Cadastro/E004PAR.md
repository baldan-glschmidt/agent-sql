# E004PAR

## Descrição

Tabelas - Parâmetros - Fluxo de Caixa (2)

---

## Resumo

- Campos: 102
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| AbgEmp | String(250) | Sim | Códigos das empresas solicitadas |
| AbgFil | String(250) | Sim | Códigos das filiais solicitadas |
| AbgAbf | String(250) | Sim | Códigos das abrangências de filiais solicitadas |
| DatIni | Date | Não | Data inicial do período solicitado |
| DatFim | Date | Não | Data final do período solicitado |
| QtdDia | Number(003,0) | Sim | Quantidade de dias |
| DiaUti | String(001) | Sim | Indicativo se o fluxo considera somente dias úteis |
| AnaSin | String(001) | Não | Tipo de fluxo (analítico ou sintético) |
| TipPer | String(001) | Não | Tipo de Período |
| CtaFrc | Number(007,0) | Sim | Conta financeira de receita a classificar |
| CtaFdc | Number(007,0) | Sim | Conta financeira de despesas a classificar |
| DatBas | Date | Sim | Data base para cálculo de juros\multa\desconto\correção\etc. |
| RecAnt | String(001) | Sim | Indicativo se considera títulos com vencimentos anteriores |
| RecVpt | String(250) | Sim | Abrangência dos códigos dos tipos de título vencidos do contas a receber |
| RecNvp | String(001) | Sim | Indicativo se deve negar abrangência dos tipos de títulos vencidos solicitados |
| RecVin | Date | Sim | Data inicial de vencimento do títulos vencidos do contas a receber |
| RecVfi | Date | Sim | Data final de vencimento do títulos vencidos do contas a receber |
| RecInc | String(001) | Sim | Indicativo se inclui os títulos efetivos do contas a receber |
| RecPre | String(001) | Sim | Indicativo se inclui os títulos de previsão do contas a receber |
| RecJrs | String(001) | Sim | Indicativo se inclui os juros previstos para os títulos do contas a receber |
| RecMul | String(001) | Sim | Indicativo se inclui a multa prevista para os títulos do contas a receber |
| RecDsc | String(001) | Sim | Indicativo se inclui os descontos previstos para os títulos do contas a receber |
| RecIpd | String(001) | Sim | Indicativo se inclui os pedidos de venda como previsão do CR |
| RecIct | String(001) | Sim | Indicativo se inclui os contratos de venda como previsão do CR |
| RecVct | Number(001,0) | Sim | Tipo de vencimento a ser considerado |
| RecFlo | String(001) | Sim | Indicativo se considera o float bancário |
| RecAtr | String(001) | Sim | Indicativo se considera o atraso médio dos clientes |
| RecPmr | String(001) | Sim | Indicativo se considera o prazo médio de recebimento dos clientes |
| RecMfa | Number(004,0) | Sim | Maior float bancário ou maior média de atraso clientes |
| RecTpt | String(250) | Sim | Abrangência dos códigos dos tipos de título do contas a receber |
| RecNtp | String(001) | Sim | Indicativo se deve negar abrangência dos tipos de títulos solicitados |
| RecPor | String(250) | Sim | Abrangência dos códigos dos portadores do contas a receber |
| RecNpo | String(001) | Sim | Indicativo se deve negar abrangência dos portadores solicitados |
| RecCrp | String(250) | Sim | Abrangência dos grupos a receber dos títulos do contas a receber |
| RecNcr | String(001) | Sim | Indicativo se deve negar abrangência dos grupos a receber solicitados |
| RecCrt | String(250) | Sim | Abrangência dos códigos das carteiras do contas a receber |
| RecNct | String(001) | Sim | Indicativo se deve negar abrangência das carteiras solicitadas |
| RecCct | String(001) | Sim | Indicativo se calcula correção (juros,multa,desconto,etc.) dos títulos a receber |
| RecTns | String(250) | Sim | Abrangência das Transações |
| RecNtn | String(001) | Sim | Indicativo se deve negar abrangência de Transações |
| RecCco | String(250) | Sim | Abrangência das contas internas do contas a receber |
| RecTcc | String(250) | Sim | Abrangência dos tipos de contas internas do contas a receber |
| PagAnt | String(001) | Sim | Indicativo se considera títulos com vencimentos anteriores |
| PagVpt | String(250) | Sim | Abrangência dos códigos dos tipos de título vencidos do contas a pagar |
| PagNvp | String(001) | Sim | Indicativo se deve negar abrangência dos tipos de títulos vencidos solicitados |
| PagVin | Date | Sim | Data inicial de vencimento do títulos vencidos do contas a pagar |
| PagVfi | Date | Sim | Data final de vencimento do títulos vencidos do contas a pagar |
| PagInc | String(001) | Sim | Indicativo se inclui os títulos efetivos do contas a pagar |
| PagPre | String(001) | Sim | Indicativo se inclui os títulos de previsão do contas a pagar |
| PagDda | String(001) | Sim | Indicativo se inclui os títulos de previsão de Dda do contas a pagar |
| PagJrs | String(001) | Sim | Indicativo se inclui os juros previstos para os títulos do contas a pagar |
| PagMul | String(001) | Sim | Indicativo se inclui a multa prevista para os títulos do contas a pagar |
| PagDsc | String(001) | Sim | Indicativo se inclui os descontos previstos para os títulos do contas a pagar |
| PagIoc | String(001) | Sim | Indicativo se inclui as ordens de compra como previsão do CP |
| PagIct | String(001) | Sim | Indicativo se inclui os contratos de compra como previsão do CP |
| PagCom | String(001) | Sim | Indicativo se inclui comissões como previsão CP |
| PagDat | Date | Sim | Data de previsão de pagamento das comissões para CP |
| PagVct | Number(001,0) | Sim | Tipo de vencimento a ser considerado |
| PagTpt | String(250) | Sim | Abrangência dos códigos dos tipos de título do contas a pagar |
| PagNtp | String(001) | Sim | Indicativo se deve negar abrangência dos tipos de títulos solicitados |
| PagPor | String(250) | Sim | Abrangência dos códigos dos portadores do contas a pagar |
| PagNpo | String(001) | Sim | Indicativo se deve negar abrangência dos portadores solicitados |
| PagCrp | String(250) | Sim | Abrangência dos grupos a pagar dos títulos do contas a pagar |
| PagNcr | String(001) | Sim | Indicativo se deve negar abrangência dos grupos a pagar solicitados |
| PagCrt | String(250) | Sim | Abrangência dos códigos das carteiras do contas a pagar |
| PagNct | String(001) | Sim | Indicativo se deve negar abrangência das carteiras solicitadas |
| PagCct | String(001) | Sim | Indicativo se calcula correção (juros,multa,desconto,etc.) dos títulos a  pagar |
| PagTns | String(250) | Sim | Abrangência das Transações |
| PagNtn | String(001) | Sim | Indicativo se deve negar abrangência de Transações |
| PagCco | String(250) | Sim | Abrangência das contas internas do contas a pagar |
| PagTcc | String(250) | Sim | Abrangência dos tipos de contas internas do contas a pagar |
| CxbInc | String(001) | Sim | Indicativo se inclui as movimentação do caixa e bancos |
| CxbLib | String(001) | Sim | Indicativo se considera a data liberação dos movimentos |
| CxbIni | String(001) | Sim | Indicativo se dever ser iniciado com determinado saldo |
| CxbSal | Number(015,2) | Sim | Saldo inicial a ser considerado |
| CxbCmi | Number(015,2) | Sim | Caixa mínimo a ser considerado |
| CxbCco | String(250) | Sim | Abrangência das contas internas |
| CxbNcc | String(001) | Sim | Indicativo se deve negar abrangência de contas internas solicitadas |
| CxbTcc | String(250) | Sim | Abrangência dos tipos de contas internas |
| CxbNtc | String(001) | Sim | Indicativo se deve negar abrangência de tipos de contas solicitados |
| CxbFil | String(250) | Sim | Abrangência das filiais das contas internas |
| CxbNfi | String(001) | Sim | Indicativo se deve negar abrangência de filiais das contas solicitadas |
| CxbTns | String(250) | Sim | Abrangência das transações |
| CxbNtn | String(001) | Sim | Indicativo se deve negar abrangência de Transações |
| OutVpf | String(001) | Sim | Indicativo se inclui os outros valores previstos para o fluxo |
| OutCnc | String(001) | Sim | Indicativo se considera natureza da conta dos outros valores para o fluxo |
| ConApl | String(001) | Sim | Indicativo se inclui aplicação |
| ConEmp | String(001) | Sim | Indicativo se inclui empréstimo |
| ConPbc | String(250) | Sim | Abrangência do código produto bancário do contrato de aplicação/captação de recursos |
| ConNpb | String(001) | Sim | Indicativo se deve negar abrangência do produto bancário solicitados |
| ConBan | String(250) | Sim | Abrangência do banco da conta interna da aplicação/captação de recursos |
| ConNba | String(001) | Sim | Indicativo se deve negar abrangência do banco solicitados |
| RecNcc | String(001) | Sim | Negação da  abrangência das contas internas do contas a receber |
| RecNtc | String(001) | Sim | Negação da  abrangência dos tipos de ctas internas do contas a receber |
| PagNcc | String(001) | Sim | Negação da  abrangência das contas internas do contas a pagar |
| PagNtc | String(001) | Sim | Negação da  abrangência dos tipos de ctas internas do contas a pagar |
| ClaFin | String(001) | Sim | Indicativo se considera classificação da conta financeira para o fluxo |
| MotCtv | String(250) | Sim | Código do motivo do contrato de venda |
| MotCtc | String(250) | Sim | Código do motivo do contrato de compra |
| CxbMtv | String(001) | Sim | Indicativo se deve negar abrangência do motivo de venda dos itens do contrato |
| CxbMtc | String(001) | Sim | Indicativo se deve negar abrangência do motivo de compra dos itens do contrato |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
