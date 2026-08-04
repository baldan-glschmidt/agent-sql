# E070EMP

## Descrição

Cadastros - Empresas

---

## Resumo

- Campos: 138
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| NomEmp | String(100) | Não | Nome da empresa |
| SigEmp | String(030) | Não | Nome fantasia da empresa |
| CodGre | Number(009,0) | Sim | Código do grupo de empresas |
| CodPai | String(004) | Sim | Código do país |
| EanPai | Number(003,0) | Sim | Código EAN do país (usado na formação do código de barras EAN) |
| EanEmp | Number(007,0) | Sim | Código EAN da empresa (usado na formação do código de barras EAN) |
| EstLef | String(001) | Não | Indicativo se lança os movimentos de estoque no plano financeiro |
| RecLtp | String(001) | Sim | Indicativo se lança títulos de previsão do contas a receber no plano financeiro |
| CprPpr | Number(003,0) | Sim | Peso válido para melhor cotação para o quesito preço |
| CprPql | Number(003,0) | Sim | Peso válido para melhor cotação para o quesito qualidade |
| CprPpe | Number(003,0) | Sim | Peso válido para melhor cotação para o quesito pontualidade na entrega |
| CprPat | Number(003,0) | Sim | Peso válido para melhor cotação para o quesito atendimento |
| CprPrz | Number(003,0) | Sim | Peso válido para melhor cotação para o quesito prazo de entrega |
| CprPpg | Number(003,0) | Sim | Peso válido para melhor cotação para o quesito prazo de pagamento |
| CprNct | Number(002,0) | Sim | Número de cotações a classificar na rotina de melhores cotações |
| EisEmp | String(001) | Não | Indicativo se a empresa utiliza a rotina do SIG (EIS) |
| EstEmp | String(001) | Não | Indicativo se a gestão de estoques está instalada na empresa |
| CprEmp | String(001) | Não | Indicativo se a gestão de compras está instalada na empresa |
| VenEmp | String(001) | Não | Indicativo se a gestão de vendas está instalada na empresa |
| RecEmp | String(001) | Não | Indicativo se a gestão de contas a receber está instalada na empresa |
| PagEmp | String(001) | Não | Indicativo se a gestão de contas a pagar está instalada na empresa |
| CxbEmp | String(001) | Não | Indicativo se a gestão de tesouraria está instalada na empresa |
| CtbEmp | String(001) | Não | Indicativo se a gestão de contabilidade está instalada na empresa |
| EfiEmp | String(001) | Não | Indicativo se a gestão de tributos está instalada na empresa |
| PatEmp | String(001) | Não | Indicativo se a gestão de patrimônio está instalada na empresa |
| PrdEmp | String(001) | Não | Indicativo se a área de manufatura está instalada na empresa |
| CusEmp | String(001) | Não | Indicativo se a área de custos está instalada na empresa |
| PagLtp | String(001) | Sim | Indicativo se lança títulos de previsão do contas a pagar no plano financeiro |
| CtbLfd | String(001) | Não | (Descontinuado) Indicativo se a empresa aceita lotes com filiais diferentes |
| PrdMas | String(001) | Não | Utiliza Máscara para montar o Código do Produto |
| PrdMpp | String(008) | Sim | Código da Máscara padrão para produto produzido (última parte) |
| PrdOpp | String(003) | Sim | Código da origem padrão para propor como última máscara |
| EspDep | Number(004,0) | Sim | Código especial para mascara de depósito |
| EspPro | Number(004,0) | Sim | Quantidade de decimais utilizada para preço de venda |
| TipPer | String(001) | Sim | Indicativo se o percentual (%) de perda p/ composição do Produto é aplicado à Quantidade necessária (Sim) ou líquida utilizada (Não) |
| LogEmp | Image | Sim | Logotipo da Empresa |
| CodMpc | Number(004,0) | Sim | Código do modelo de plano contábil utilizado |
| CodMpf | Number(004,0) | Sim | Código do modelo de plano financeiro utilizado |
| CodMpu | Number(004,0) | Sim | Código do modelo de plano de centro de custos utilizado |
| IndPrj | String(001) | Sim | Indicativo se a empresa utiliza controle de projetos |
| OriRat | Number(001,0) | Não | (Descontinuado) Origem do rateio a ser considerado na contabilização |
| SugCtb | String(001) | Não | Indicativo se sugere conta contábil no rateio plano financeiro |
| FinRea | String(001) | Não | Indicativo se os lançamentos do plano financeiro serão em real time |
| IndEma | String(001) | Sim | Indicativo se a empresa utiliza correio eletrônico |
| IndMr2 | String(001) | Sim | [DEPRECADO] Indicativo se a empresa utiliza conceitos de MRP II no Planejamento de Necessidades |
| PatMco | String(003) | Sim | Código da Moeda Corrente para o Patrimônio |
| PatMio | String(003) | Sim | Código da Moeda em Índice Oficial para o Patrimônio |
| PatMig | String(003) | Sim | Código da Moeda em Índice Gerencial para o Patrimônio |
| PatLgt | String(001) | Sim | Indicativo se a empresa utiliza o Log de Telas do Patrimônio (E678LOG) |
| PatEsp | String(001) | Sim | Verifica ao inserir um Bem se a Conta Contábil informada para o Bem (E045PLA.CtaRed) é a mesma informada na espécie do Bem. |
| PatMb1 | String(008) | Sim | Código da Máscara para 1ª parte do código do bem |
| PatMb2 | String(008) | Sim | Código da Máscara para 2ª parte do código do bem |
| PatMb3 | String(008) | Sim | Código da Máscara para 3ª parte do código do bem |
| PatMb4 | String(008) | Sim | Código da Máscara para 4ª parte do código do bem |
| PatMb5 | String(008) | Sim | Código da Máscara para 5ª parte do código do bem |
| PatMb6 | String(008) | Sim | Código da Máscara para 6ª parte do código do bem |
| PatMb7 | String(008) | Sim | Código da Máscara para 7ª parte do código do bem |
| IndPla | String(001) | Sim | Indicativo se o número da plaqueta dos bens foram consistidos |
| DepMas | String(001) | Não | Indicativo se a empresa utiliza máscara para depósitos |
| CprLpf | String(001) | Não | Bloquear compra de produto que não está ligado ao fornecedor? |
| CprLsf | String(001) | Não | Bloquear compra de serviço que não está ligado ao fornecedor? |
| DisEmp | String(001) | Não | Indicativo se o cliente utiliza as rotinas de Distribuição |
| SgqEmp | String(001) | Não | Indicativo se a área de qualidade está instalada na empresa |
| QtdCen | Number(003,0) | Sim | Quantidade de caracteres para limitar digitação dos endereços (Filiais, Fornecedores, Clientes, Transportadoras, Representantes) |
| QtdCno | Number(003,0) | Sim | Quantidade de caracteres para limitar digitação dos nomes (Fornecedores, Clientes, Transportadoras, Representantes, Recebedor) |
| ComPsi | String(001) | Sim | Indicativo se possui serviços com tributação de ICMS/IPI para entradas e saídas |
| CodMpx | Number(004,0) | Sim | Código do modelo de plano auxiliar utilizado |
| QtdCdp | Number(003,0) | Sim | Quantidade de caracteres para limitar digitação da Descrição do Produto |
| QtdCcp | Number(002,0) | Sim | Quantidade de caracteres para limitar digitação do Complemento do Produto |
| QtdCdc | Number(002,0) | Sim | Quantidade de caracteres para limitar digitação da Descrição Complementar da Derivação |
| QtdCdd | Number(002,0) | Sim | Quantidade de caracteres para limitar digitação da Descrição da Derivação (Máscara) |
| EstPre | Number(001,0) | Sim | Preço padrão para calcular o valor da requisição e da solicitação de compra |
| CodAgc | String(005) | Sim | Código de agrupamento para comercial |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| CprCsn | String(001) | Sim | Indicativo se a série da nota fiscal deve ser considerada na verificação da existência da nota em outra filial |
| CprPcz | String(001) | Sim | Indicativo se permite gravar uma cotação com o preço unitário zerado |
| IndSdm | String(001) | Sim | Indicativo se a empresa utiliza saldo devedor da multimoeda para cálculo da multi-moeda |
| UtiWms | String(001) | Sim | Indicativo se a empresa utiliza o sistema WMS (Se sim gera os controles para integração) |
| IndHis | String(001) | Sim | Indicador de histórico de localizações gerado |
| VenCrl | String(001) | Sim | Usa pedidos com clientes relacionados |
| QtdCct | Number(003,0) | Sim | (Descontinuado) Quantidade de caracteres para limitar digitação da Descrição Conta Contábil |
| CprFoc | Number(001,0) | Sim | Tipo de filtro utilizado para permitir visualização e alteração de ordens de compra (Padrão sugerido para o usuário) |
| CprFcp | Number(001,0) | Sim | Tipo de filtro utilizado para permitir visualização e alteração do contrato de compra (Padrão sugerido para o usuário) |
| CtrMar | String(001) | Sim | Indicativo se tem controle de marca dos produtos nos pedidos, pré-faturas e notas fiscais de saída |
| UtiQmv | String(001) | Sim | Indicativo se a empresa controla a quantidade múltipla de venda do produto |
| AncEmp | String(001) | Sim | Indicativo se a análise de crédito é por empresa ou seja considera todas as filiais para a análise. |
| RetCgc | String(001) | Sim | Indicativo se a empresa possui controle de retenções por CNPJ e não por código do cliente/fornecedor |
| RetPro | String(001) | Sim | Indicativo se a empresa emite controle de retenções de PIS, Cofins, CSLL, IRRF, e Outras Retenções por produto |
| TipWms | Number(001,0) | Sim | Tipo de integração com o WMS |
| ForGne | Number(001,0) | Sim | Forma de geração dos números das embalagens de estocagem |
| NfvSeq | String(001) | Sim | Indica se a empresa aceita impressão de notas fora da ordem de sequência |
| UtiGec | String(001) | Sim | Indicativo se a empresa utiliza o sistema GECEX (Se sim gera os controles para integração) |
| UtiBio | String(001) | Sim | Indicativo se a empresa utiliza o sistema da Biosalc (Se sim gera os controles para integração) |
| AcgEmp | String(001) | Sim | Indicativo se a análise de crédito do grupo do cliente é por empresa ou seja considera todas as filiais para a análise. |
| AprDoc | String(001) | Sim | Indica se a empresa utiliza o controle de aprovação de documentos do SGQ |
| MntEmp | String(001) | Sim | Indicativo se a gestão de manutenção de equipamentos está instalada na empresa |
| CusFil | String(001) | Sim | Custos por filial |
| UtiNor | String(001) | Sim | Indicador se utiliza o nível da origem para definir árvore hierárquica do produto acabado final |
| PrdMul | String(001) | Sim | Cálculo de Explosão de Necessidades Encadeado (Multinível) |
| ConDig | String(001) | Sim | Considera O.Ps. digitadas na quantidade de ordens do estoque (influencia na quantidade disponível) |
| GerCor | String(001) | Sim | Gera calendário ocupação dos recursos da OP |
| UtiLic | String(001) | Sim | Indicativo se a empresa utiliza controle de licitação na área de suprimentos |
| LotBrf | String(001) | Sim | Controle de Lote na Baixa de Títulos do CRE por Filial |
| IndImh | String(001) | Sim | Indicativo se a empresa utiliza índice por hora para cálculo da multi-moeda |
| FatFis | String(001) | Sim | Calcular faturamento por item de documento fiscal |
| UtiEml | String(001) | Sim | Indicativo se a empresa utiliza estrutura de embalagem multinível (volumes) |
| SltIqp | String(010) | Sim | Código do status do lote para inspeções de qualidade pendentes |
| LotVen | String(001) | Sim | Permite a transferência de produtos com lote vencido |
| VlaPro | String(001) | Sim | Valoriza produto acabado em nota fiscal de entrada do tipo 8 |
| LgiOcp | String(001) | Sim | Permite ligar item de OC na situação 8(Em preparação)  à uma nova NF de Entrada |
| CabNfe | String(001) | Sim | Permite gravar apenas o cabeçalho da nota fiscal de entrada |
| UsaAgr | String(001) | Sim | Utilizar agrupamento de filial |
| CcaIcm | String(001) | Sim | Utilizar controle de crédito acumulado de ICM |
| CotCpr | String(001) | Sim | Utiliza controle de cota de compra |
| UsuNct | Number(010,0) | Sim | Usuário para notificação do controle de cotas de compra por competência |
| AcrTcc | String(001) | Sim | Indicativo se a empresa trabalha com central de crédito na matriz |
| UtiVcf | String(001) | Sim | Indicativo se a empresa utiliza controle de verba de compra das filiais |
| UtiTju | String(001) | Sim | Indicativo se a empresa utiliza tabela de juros no varejo |
| ReaIsv | String(001) | Sim | Indicativo se a empresa realiza intermediação de serviços |
| QtdClv | Number(002,0) | Sim | Quantidade de caracteres para controlar a leitura única de volumes |
| PerCdm | Number(005,2) | Sim | Percentual do custo do dinheiro ao mês |
| PerDop | Number(005,2) | Sim | Percentual de despesas operacionais |
| UtiVar | String(001) | Sim | Indicativo se a empresa utiliza módulo varejo eletromóveis |
| RemEmp | String(001) | Sim | Indicativo se a empresa utiliza receituário agronômico na gestão de vendas |
| IndTfp | String(001) | Sim | Indicativo se a empresa gera nota fiscal de compra de taxa na filial da pesagem |
| RegEsp | String(001) | Sim | Registra entrada e saída dos prrodutos para controle de impostos. |
| DprEmp | String(001) | Sim | Indicativo se duplica automaticamente o produto para outras empresas |
| ClcVal | String(001) | Sim | Indicativo se a empresa utiliza controle de Coleção por Validade. |
| CfgBal | String(001) | Sim | Local de Configuração da Balança |
| CtaTra | Number(007,0) | Sim | Conta Contábil Transitória para Distribuição de Custo |
| IndFcx | String(001) | Sim | Indicativo se integra fluxo de caixa entre ERP x SeniorX (utilizado também na integração do fluxo de caixa por eventos de negócio) |
| GraRnf | String(001) | Sim | Gravar origens da integração do reinf bloco 4 |
| USU_ConSid | String(060) | Sim | Conexao SID |
| USU_SITEST | String(001) | Sim | Ataliza Estoque Depois Geracao |
| USU_TNSPER | String(200) | Sim | Transações - Rotina Sobras e Perdas |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
