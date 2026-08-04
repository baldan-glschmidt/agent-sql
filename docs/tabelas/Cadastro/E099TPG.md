# E099TPG

## Descrição

Cadastros - Usuários - Últimos Parâmetros Solicitados

---

## Resumo

- Campos: 70
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| CodTpg | Number(003,0) | Não | Código da rotina gravada com últimos parâmetros |
| DesTpg | String(030) | Sim | Descrição do conteúdo da tabela de último parâmetro |
| DatIni | Date | Não | Data inicial do período solicitado |
| DatFim | Date | Não | Data final do período solicitado |
| QtdDia | Number(003,0) | Sim | Quantidade de dias |
| AbgEmp | String(250) | Sim | Códigos das empresas solicitadas |
| AbgFil | String(250) | Sim | Códigos das filiais solicitadas |
| AbgAbf | String(250) | Sim | Códigos das abrangências de filiais solicitadas |
| TitAnt | String(001) | Sim | Indicativo se considera títulos com vencimentos anteriores |
| VenTpt | String(250) | Sim | Abrangência dos códigos dos tipos de título vencidos |
| VenNtp | String(001) | Sim | Indicativo se deve negar abrangência dos tipos de títulos vencidos solicitados |
| VenIni | Date | Sim | Data inicial de vencimento do títulos vencidos |
| VenFin | Date | Sim | Data final de vencimento do títulos vencidos |
| DatBas | Date | Sim | Data base para cálculo de juros\multa\desconto\correção\etc. |
| FloAtr | Number(004,0) | Sim | Maior float bancário ou maior média de atraso clientes |
| RecInc | String(001) | Sim | Indicativo se inclui títulos do contas a receber |
| RecPre | String(001) | Sim | Indicativo se inclui os títulos de previsão do contas a receber |
| RecIpd | String(001) | Sim | Indicativo se inclui os pedidos como previsão do CR |
| RecIct | String(001) | Sim | Indicativo se inclui os contratos de venda como previsão do CR |
| RecFlo | String(001) | Sim | Indicativo se considera o float bancário |
| RecAtr | String(001) | Sim | Indicativo se considera o atraso médio dos clientes |
| RecPmr | String(001) | Sim | Indicativo se considera o prazo médio de recebimento dos clientes |
| RecVct | Number(001,0) | Sim | Tipo de vencimento a ser considerado |
| RecTpt | String(250) | Sim | Códigos dos tipos de títulos do contas a receber selecionados |
| RecNtp | String(001) | Sim | Indicativo se deve negar abrangência dos tipos de títulos solicitados |
| RecPor | String(250) | Sim | Códigos dos portadores do contas a receber selecionados |
| RecNpo | String(001) | Sim | Indicativo se deve negar abrangência dos portadores solicitados |
| RecCrp | String(250) | Sim | Códigos dos grupos de títulos do contas a receber selecionados |
| RecNcr | String(001) | Sim | Indicativo se deve negar abrangência dos grupos a receber solicitados |
| RecCrt | String(250) | Sim | Abrangência dos códigos das carteiras do contas a receber |
| RecNct | String(001) | Sim | Indicativo se deve negar abrangência das carteiras solicitadas |
| RecCct | String(001) | Sim | Indicativo se calcula correção (juros,multa,desconto,etc.) dos títulos a receber |
| RecCim | String(001) | Sim | Indicativo se calcula previsão de impostos |
| RecTim | String(005) | Sim | Código da transação para simulação de baixa para previsão de impostos |
| PagInc | String(001) | Sim | Indicativo se inclui os títulos do contas a pagar |
| PagPre | String(001) | Sim | Indicativo se inclui os títulos de previsão do contas a pagar |
| PagDda | String(001) | Sim | Indicativo se inclui os títulos de previsão  de DDA do contas a pagar |
| PagIoc | String(001) | Sim | Indicativo se inclui as ordens de compra na previsão do CP |
| PagIct | String(001) | Sim | Indicativo se inclui os contratos de compra como previsão do CP |
| PagCom | String(001) | Sim | Indicativo se inclui comissões |
| PagDat | Date | Sim | Data base de pagamento das comissões |
| PagVct | Number(001,0) | Sim | Tipo de vencimento a ser considerado |
| PagTpt | String(250) | Sim | Códigos dos tipos de títulos do contas a pagar selecionados |
| PagNtp | String(001) | Sim | Indicativo se deve negar abrangência dos tipos de títulos solicitados |
| PagPor | String(250) | Sim | Códigos dos portadores do contas a pagar selecionados |
| PagNpo | String(001) | Sim | Indicativo se deve negar abrangência dos portadores solicitados |
| PagCrp | String(250) | Sim | Códigos dos grupos de títulos do contas a pagar selecionados |
| PagNcr | String(001) | Sim | Indicativo se deve negar abrangência dos grupos a pagar solicitados |
| PagCrt | String(250) | Sim | Abrangência dos códigos das carteiras do contas a pagar |
| PagNct | String(001) | Sim | Indicativo se deve negar abrangência das carteiras solicitadas |
| PagCct | String(001) | Sim | Indicativo se calcula correção (juros,multa,desconto,etc.) dos títulos a  pagar |
| PagCim | String(001) | Sim | Indicativo se calcula previsão de impostos |
| PagTim | String(005) | Sim | Código da transação para simulação de baixa para previsão de impostos |
| CxbInc | String(001) | Sim | Indicativo se inclui as movimentação do caixa e bancos |
| CxbLib | String(001) | Sim | Indicativo se considera a data liberação dos movimentos |
| CxbIni | String(001) | Sim | Indicativo se dever ser iniciado com determinado saldo |
| CxbSal | Number(015,2) | Sim | Saldo inicial a ser considerado |
| CxbCco | String(250) | Sim | Números das contas internas selecionadas |
| CxbNcc | String(001) | Sim | Indicativo se deve negar abrangência de contas internas solicitadas |
| CxbTcc | String(250) | Sim | Códigos dos tipos de contas internas selecionados |
| CxbNtc | String(001) | Sim | Indicativo se deve negar abrangência de tipos de contas solicitados |
| CxbFil | String(250) | Sim | Abrangência das filiais das contas internas |
| CxbNfi | String(001) | Sim | Indicativo se deve negar abrangência de filiais das contas solicitadas |
| TipPer | String(001) | Sim | Tipo de Período |
| MotCtv | String(250) | Sim | Código do motivo do contrato de venda |
| MotCtc | String(250) | Sim | Código do motivo do contrato de compra |
| CxbMtv | String(001) | Sim | Indicativo se deve negar abrangência do motivo de venda dos itens do contrato |
| CxbMtc | String(001) | Sim | Indicativo se deve negar abrangência do motivo de compra dos itens do contrato |

---

## Chave Primária

- CodEmp
- CodUsu
- CodTpg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099TPG_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

