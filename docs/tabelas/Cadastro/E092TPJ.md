# E092TPJ

## Descrição

Tabelas - Projetos - Tipos de Projetos

---

## Resumo

- Campos: 110
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa do tipo de projeto |
| CodTpj | Number(003,0) | Não | Código do tipo de projeto |
| DesTpj | String(100) | Não | Descrição do tipo de projeto |
| AbrTpj | String(020) | Não | Abreviatura do tipo de projeto |
| TpjCvl | String(001) | Não | Indicativo se o tipo do projeto tem controle de valor |
| RegOrc | String(001) | Sim | Indicativo do regime de orçamento do projeto |
| TpjCvm | String(001) | Não | Indicativo se o tipo do projeto tem controle de valor por mês |
| TpjCvp | String(001) | Não | Indicativo se o tipo do projeto tem controle de valor por Projeto |
| TpjCvf | String(001) | Não | Indicativo se o tipo do projeto tem controle de valor por fase |
| TpjCvc | String(001) | Não | Indicativo se o tipo do projeto tem controle de valor por conta de receita/despesa |
| TpjCvu | String(001) | Não | Indicativo se o tipo do projeto tem controle de valor por centro de custo |
| PrjFis | String(001) | Sim | Indicativo se para este projeto haverá controle físico |
| TpjQtd | String(001) | Sim | Indicativo se o controle físico por quantidade |
| TpjUni | String(001) | Sim | Indicativo se o controle físico pelo valor unitário |
| TpjTot | String(001) | Sim | Indicativo se o controle físico pelo valor total |
| IndAoi | String(001) | Sim | Indicativo se para este projeto é permitido alterar o orçamento inicial |
| CodPj1 | String(008) | Sim | Código da Máscara para 1ª parte do código do projeto |
| CodPj2 | String(008) | Sim | Código da Máscara para 2ª parte do código do projeto |
| CodPj3 | String(008) | Sim | Código da Máscara para 3ª parte do código do projeto |
| CodPj4 | String(008) | Sim | Código da Máscara para 4ª parte do código do projeto |
| CodPj5 | String(008) | Sim | Código da Máscara para 5ª parte do código do projeto |
| CodPj6 | String(008) | Sim | Código da Máscara para 6ª parte do código do projeto |
| CodPj7 | String(008) | Sim | Código da Máscara para 7ª parte do código do projeto |
| CodPj8 | String(008) | Sim | Código da Máscara para 8ª parte do código do projeto |
| CodPj9 | String(008) | Sim | Código da Máscara para 9ª parte do código do projeto |
| CodPj0 | String(008) | Sim | Código da Máscara para 10ª parte do código do projeto |
| TnsPtp | String(005) | Sim | Transação padrão para projetos deste tipo |
| ObjPtp | String(250) | Sim | Texto padrão para descrição dos objetivos do tipo de projeto |
| CliPtp | Number(009,0) | Sim | Código do cliente padrão do tipo de projeto |
| FatPtp | Number(009,0) | Sim | Código do cliente padrão para faturamento do tipo de projeto |
| ForPtp | Number(009,0) | Sim | Código do órgão financiador padrão do tipo de projeto |
| UsuPtp | Number(010,0) | Sim | Usuário responsável padrão do tipo de projeto |
| CcuPtp | String(009) | Sim | Centro de custo responsável padrão do tipo de projeto |
| SitPtp | String(003) | Não | Situação padrão do tipo de projeto |
| ClaFpj | String(001) | Sim | Utiliza classificação fase |
| MotPtp | Number(006,0) | Sim | Código do motivo da situação padrão do tipo de projeto |
| ObsPtp | String(250) | Sim | Observação padrão do motivo da situação do tipo de projeto |
| FinCrp | Number(007,0) | Sim | Conta financeira de receita padrão do tipo de projeto para efeito de rateio |
| FinCdp | Number(007,0) | Sim | Conta financeira de despesa padrão do tipo de projeto para efeito de rateio |
| CcuCpp | String(009) | Sim | Centro de custo padrão do tipo de projeto para efeito de rateio |
| SitTpj | String(001) | Sim | Indicativo da situação do tipo do projeto |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do tipo do projeto |
| ObsMot | String(250) | Sim | Observação do motivo da situação do tipo do projeto |
| LctMan | String(001) | Sim | Gerar Lançamento Manual nos Recursos Previstos para Contabilização |
| EstRat | String(001) | Sim | Gerar estorno do rateio em projetos na data atual |
| EstCco | String(001) | Sim | Atualizar situação no conta corrente do projeto ao estornar |
| TpjNat | String(001) | Sim | Natureza do projeto |
| OrcPos | String(001) | Sim | Consistir alterações de orçamento de projetos |
| RegAtu | String(001) | Sim | Regime para atualização on-line de projetos |
| TotOrc | String(001) | Sim | Totaliza orçamento sintético a partir do orçamento analítico |
| PrjCvr | String(001) | Sim | Indicativo se o projeto tem controle de valor por rotina |
| CriBrq | String(001) | Sim | Indicativo do critério de bloqueio nas requisições (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBrq | String(100) | Sim | Mensagem para aviso ou bloqueio nas requisições |
| CriBsc | String(001) | Sim | Indicativo do critério de bloqueio nas solicitações de compra (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBsc | String(100) | Sim | Mensagem para aviso ou bloqueio nas solicitações de compra |
| CriBoc | String(001) | Sim | Indicativo do critério de bloqueio nas ordens de compra (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBoc | String(100) | Sim | Mensagem para aviso ou bloqueio nas ordens de compra |
| CriBcp | String(001) | Sim | Indicativo do critério de bloqueio no contas a pagar (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBcp | String(100) | Sim | Mensagem para aviso ou bloqueio no contas a pagar |
| CriBpt | String(001) | Sim | Indicativo do critério de bloqueio nas preparações de tesouraria (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBpt | String(100) | Sim | Mensagem para aviso ou bloqueio nas preparações de tesouraria |
| CriBte | String(001) | Sim | Indicativo do critério de bloqueio na tesouraria (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBte | String(100) | Sim | Mensagem para aviso ou bloqueio na tesouraria |
| CriBes | String(001) | Sim | Indicativo do critério de bloqueio nos estoques (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBes | String(100) | Sim | Mensagem para aviso ou bloqueio nos estoques |
| CriBma | String(001) | Sim | Indicativo do critério de bloqueio nos lançamentos manuais (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBma | String(100) | Sim | Mensagem para aviso ou bloqueio nos lançamentos manuais |
| CriBcr | String(001) | Sim | Indicativo do critério de bloqueio nos créditos do contas a receber (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBcr | String(100) | Sim | Mensagem para aviso ou bloqueio nos créditos do contas a receber |
| CriBfr | String(001) | Sim | Indicativo do critério de bloqueio nas requisições (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBfr | String(100) | Sim | Mensagem para aviso ou bloqueio nas requisições |
| CtrQfr | String(001) | Sim | Controle físico por quantidade nas requisições |
| CtrUfr | String(001) | Sim | Controle físico pelo valor unitário nas requisições |
| CtrTfr | String(001) | Sim | Controle físico pelo valor total nas requisições |
| CriBfs | String(001) | Sim | Indicativo do critério de bloqueio nas solicitações de compra (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBfs | String(100) | Sim | Mensagem para aviso ou bloqueio nas solicitações de compra |
| CtrQfs | String(001) | Sim | Controle físico por quantidade nas solicitações de compra |
| CtrUfs | String(001) | Sim | Controle físico pelo valor unitário nas solicitações de compra |
| CtrTfs | String(001) | Sim | Controle físico pelo valor total nas solicitações de compra |
| CriBfo | String(001) | Sim | Indicativo do critério de bloqueio nas ordens de compra (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBfo | String(100) | Sim | Mensagem para aviso ou bloqueio nas ordens de compra |
| CtrQfo | String(001) | Sim | Controle físico por quantidade nas ordens de compra |
| CtrUfo | String(001) | Sim | Controle físico pelo valor unitário nas ordens de compra |
| CtrTfo | String(001) | Sim | Controle físico pelo valor total nas ordens de compra |
| CriBfp | String(001) | Sim | Indicativo do critério de bloqueio no contas a pagar (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBfp | String(100) | Sim | Mensagem para aviso ou bloqueio no contas a pagar |
| CtrQfp | String(001) | Sim | Controle físico por quantidade no contas a pagar |
| CtrUfp | String(001) | Sim | Controle físico pelo valor unitário no contas a pagar |
| CtrTfp | String(001) | Sim | Controle físico pelo valor total no contas a pagar |
| CriBfe | String(001) | Sim | Indicativo do critério de bloqueio nos estoques (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBfe | String(100) | Sim | Mensagem para aviso ou bloqueio nos estoques |
| CtrQfe | String(001) | Sim | Controle físico por quantidade nos estoques |
| CtrUfe | String(001) | Sim | Controle físico pelo valor unitário nos estoques |
| CtrTfe | String(001) | Sim | Controle físico pelo valor total nos estoques |
| CriBfm | String(001) | Sim | Indicativo do critério de bloqueio nos lançamentos manuais (L=Libera, A=Avisa, B=Bloqueia) |
| MsgBfm | String(100) | Sim | Mensagem para aviso ou bloqueio nos lançamentos manuais |
| CtrQfm | String(001) | Sim | Controle físico por quantidade nos lançamentos manuais |
| CtrUfm | String(001) | Sim | Controle físico pelo valor unitário nos lançamentos manuais |
| CtrTfm | String(001) | Sim | Controle físico pelo valor total nos lançamentos manuais |
| LibMov | String(001) | Sim | Indicativo se o projeto receberá movimentações quando suspenso por ocorrência |
| PerEre | Number(001,0) | Sim | Indicativo da periodicidade da entrega de relatórios do projeto |
| DiaApo | Number(002,0) | Sim | Dias de entrega após apuração |
| TrfSal | String(001) | Sim | Transferir saldos da competência anterior para a competência atual |
| OrcAnt | String(001) | Sim | Considerar orçamentos anteriores para o bloqueio orçamentário |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |

---

## Chave Primária

- CodEmp
- CodTpj

---

## Índices

### E092TPJIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- SitPtp

---

## Relacionamentos

### IR_E092TPJ_033

**Tabela:** E615SPJ

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| SitPtp | CodSpj |

