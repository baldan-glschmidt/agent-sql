# E004PAE

## Descrição

Tabelas - Parâmetros - Análise de Embarque

---

## Resumo

- Campos: 74
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| ObsPae | String(250) | Sim | Texto da observação |
| AbgPed | String(999) | Sim | Abrangência de pedidos |
| EntIni | Date | Sim | Data de entrega inicial para análise de embarque |
| EntFim | Date | Sim | Data de entrega final para análise de embarque |
| EmiIni | Date | Sim | Data de emissão de pedido inicial para análise de embarque |
| EmiFim | Date | Sim | Data de emissão de pedido final para análise de embarque |
| AbgTpd | Number(002,0) | Sim | Tipos de pedidos |
| AbgPrc | Number(002,0) | Sim | Procedências dos pedidos |
| AbgTns | String(250) | Sim | Abrangência das transações dos pedidos |
| AbgCpg | String(250) | Sim | Abrangência das condições de pagamento dos pedidos |
| PgtAnt | String(001) | Não | Indicativo se só analisa pedidos com pagamento antecipado |
| AbgCli | String(250) | Sim | Abrangência dos clientes dos pedidos |
| AbgCat | String(030) | Sim | Abrangência das categorias dos clientes dos pedidos |
| AbgRam | String(250) | Sim | Abrangência dos ramos de atividade dos clientes dos pedidos |
| AbgRoe | String(250) | Sim | Abrangência das rotas de entrega dos clientes dos pedidos |
| AbgUfs | String(150) | Sim | Abrangência dos estados dos clientes dos pedidos |
| AbgRve | String(250) | Sim | Abrangência das regiões de venda dos clientes dos pedidos |
| AbgCrp | String(250) | Sim | Abrangência dos grupos a receber dos clientes dos pedidos |
| AbgRep | String(250) | Sim | Abrangência dos representantes dos pedidos |
| AbgTra | String(250) | Sim | Abrangência das transportadoras/redespachos dos pedidos |
| AbgPor | String(250) | Sim | Abrangência dos portadores dos pedidos |
| AbgOri | String(250) | Sim | Abrangência das origens dos pedidos |
| AbgFam | String(250) | Sim | Abrangência das famílias dos pedidos |
| IndAgr | String(001) | Não | Indicativo se deve considerar agrupamento de derivação (grade completa) |
| AbgPro | String(250) | Sim | Abrangência dos produtos dos pedidos |
| AbgDer | String(250) | Sim | Abrangência das derivações dos pedidos |
| AbgDep | String(250) | Sim | Abrangência dos depósitos dos pedidos |
| AbgDv1 | String(250) | Sim | Abrangência - 1 |
| AbgDv2 | String(250) | Sim | Abrangência - 2 |
| AbgDv3 | String(250) | Sim | Abrangência - 3 |
| AbgDv4 | String(250) | Sim | Abrangência - 4 |
| AbgDv5 | String(250) | Sim | Abrangência - 5 |
| CriAne | Number(001,0) | Não | Critério a ser adotado pela análise de embarque |
| VenVmn | Number(015,2) | Não | Valor mínimo permitido para as notas fiscais |
| RecVmt | Number(015,2) | Não | Valor mínimo permitido para títulos do contas a receber |
| QtdMfp | Number(003,0) | Não | Quantidade máxima de faturamento por pedido |
| PerMpe | Number(005,2) | Não | Percentual mínimo do pedido em estoque para gerar pré-fatura |
| PerCan | Number(005,2) | Não | Percentual do pedido sem estoque que deve ser cancelado |
| CriSpd | Number(001,0) | Não | Primeiro critério de seleção dos pedidos para análise de embarque |
| CriSp2 | Number(001,0) | Sim | Segundo critério de seleção dos pedidos para análise de embarque |
| CriSp3 | Number(001,0) | Sim | Terceiro critério de seleção dos pedidos para análise de embarque |
| CriSp4 | Number(001,0) | Sim | Quarto critério de seleção dos pedidos para análise de embarque |
| CriEst | Number(001,0) | Não | Critério de cálculo dos estoques para efeito de análise |
| GerMvp | String(001) | Não | Indicativo se gera movimento de estoque pela pré-fatura |
| CriTre | Number(001,0) | Não | Critério de tratamento do estoque reservado para pedido não atendidos |
| CriGpf | Number(001,0) | Não | Critério para geração de pré-faturas |
| GerPfb | String(001) | Não | Indicativo se gera pré-fatura com problema de crédito e cadastro (Bloqueada) |
| RatEst | String(001) | Sim | Indicativo se o saldo em estoque deve ser distribuído entre os pedidos |
| ExcPfv | String(001) | Sim | Excluir pré-faturas vencidas antes da geração da nova análise de embarque |
| SldMnf | Number(001,0) | Sim | Critério para tratamento do saldo do pedido quando este for menor que o mínimo da NF |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| QtdMpe | Number(014,5) | Sim | Quantidade mínima do pedido em estoque para gerar pré-fatura |
| AbgPrd | String(250) | Sim | Abrangência relatório de produção |
| AbgFab | String(250) | Sim | Abrangência do código do fabricante |
| AbgFor | String(250) | Sim | Abrangência do código do fornecedor |
| ConVmt | String(001) | Sim | Sempre consiste valor mínimo dos títulos |
| TnsLin | String(001) | Sim | Indicativo se deve ser feito a gravação a cada pré-fatura gerada |
| AnaDep | String(001) | Sim | Indicativo se a análise deve analisar outros depósitos caso o depósito do pedido não tenha saldo para atender o item |
| AnaPep | String(001) | Sim | Indicativo se a análise deve analisar itens de pedido em preparação (Situação 8) |
| AbgGre | String(250) | Sim | Código do grupo de empresas |
| NegAbg | String(050) | Sim | Negação dos campos de abrangência da seleção |
| AbgSro | String(250) | Sim | Abrangência das subrotas de entrega dos clientes dos pedidos |
| ConMin | String(001) | Sim | Considerar mínimos de reposição |
| MulFil | String(001) | Sim | Indicativo se irá gerar análise pré-fatura multifilial |
| AbgFil | String(100) | Sim | Abrangência do código da filial |
| AbgFpg | String(050) | Sim | Abrangência das formas de pagamento dos pedidos |
| ObgPla | String(001) | Sim | Obrigar informações da placa do veículo na formação de carga |
| FecIni | Date | Sim | Data de inicio do fechamento do pedido |
| FecFim | Date | Sim | Data final do fechamento do pedido |
| PsqPfc | Number(001,0) | Sim | Tipo de pesquisa padrão para carga de pendências na formação de carga |

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
