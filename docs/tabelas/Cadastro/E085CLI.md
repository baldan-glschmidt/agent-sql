# E085CLI

## Descrição

Cadastros - Clientes

---

## Resumo

- Campos: 192
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| NomCli | String(100) | Não | Nome do cliente |
| ApeCli | String(050) | Não | Nome fantasia do cliente |
| MarCli | String(020) | Sim | Marca do cliente |
| SenCli | String(010) | Sim | Senha do cliente |
| TipCli | String(001) | Não | Tipo do cliente |
| TipMer | String(001) | Não | Tipo de mercado do cliente |
| TipEmc | Number(001,0) | Sim | Tipo do direito de propriedade da empresa |
| CliCon | String(001) | Não | Indicativo se o cliente é contribuinte de ICMS |
| CodRam | String(005) | Sim | Código do ramo de atividade |
| InsEst | String(025) | Sim | Inscrição estadual do cliente |
| InsMun | String(016) | Sim | Inscrição municipal do cliente |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do cliente |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do cliente |
| CodGre | Number(009,0) | Sim | Código do grupo de empresas |
| ZonFra | Number(001,0) | Sim | Indicativo de qual é o benefício fiscal do cliente |
| CodSuf | String(010) | Sim | Número do cliente junto à Suframa |
| EndCli | String(100) | Sim | Endereço do cliente |
| CplEnd | String(200) | Sim | Complemento do endereço do cliente (sala, andar, etc.) |
| CliPrx | String(120) | Sim | Ponto de referência ou proximidade do cliente |
| ZipCod | String(014) | Sim | Código da cidade do cliente externo - ZIP CODE |
| CepCli | Number(008,0) | Sim | CEP do cliente |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade do cliente |
| BaiCli | String(075) | Sim | Bairro do cliente |
| CidCli | String(060) | Sim | Cidade do cliente |
| SigUfs | String(002) | Sim | Sigla do estado do cliente |
| CodPai | String(004) | Sim | Código do país do cliente |
| TemEnt | String(001) | Não | Indicativo se o cliente tem endereços de entrega diferentes |
| EndEnt | String(100) | Sim | Endereço de entrega do cliente |
| CplEnt | String(200) | Sim | Complemento do endereço de entrega do cliente |
| ZipEnt | String(014) | Sim | Código da cidade do endereço de entrega do cliente externo - ZIP CODE |
| CepEnt | Number(008,0) | Sim | CEP do endereço de entrega do cliente |
| IniEnt | Number(008,0) | Sim | Faixa inicial do CEP do endereço de entrega do cliente |
| CidEnt | String(060) | Sim | Cidade do endereço de entrega do cliente |
| EstEnt | String(002) | Sim | Estado do endereço de entrega do cliente |
| InsEnt | String(025) | Sim | Inscrição estadual do endereço de entrega |
| CgcEnt | Number(014,0) | Sim | Número do CNPJ de Entrega |
| DocIdeEnt | String(014) | Sim | Número do CNPJ de Entrega |
| FonEnt | String(020) | Sim | Telefone do endereço de entrega |
| EmaEnt | String(060) | Sim | E-mail do endereço de entrega |
| TemCob | String(001) | Não | Indicativo se o cliente tem endereços de cobrança diferentes |
| EndCob | String(100) | Sim | Endereço de cobrança do cliente |
| CplCob | String(200) | Sim | Complemento do endereço de cobrança do cliente |
| CepCob | Number(008,0) | Sim | CEP do endereço de cobrança do cliente |
| IniCob | Number(008,0) | Sim | Faixa inicial do CEP do endereço de cobrança do cliente |
| CidCob | String(060) | Sim | Cidade do endereço de cobrança do cliente |
| EstCob | String(002) | Sim | Estado do endereço de cobrança do cliente |
| CgcCob | Number(014,0) | Sim | Número do CNPJ de cobrança |
| DocIdeCob | String(014) | Sim | Número do CNPJ de cobrança |
| EntCor | String(001) | Sim | Indicativo do endereço de entrega de correspondências |
| FonCli | String(020) | Sim | Número do telefone - 1 |
| FonCl2 | String(020) | Sim | Número do telefone - 2 |
| FonCl3 | String(020) | Sim | Número do telefone - 3 |
| FonCl4 | String(020) | Sim | Número do telefone - 4 |
| FonCl5 | String(020) | Sim | Número do telefone - 5 |
| FaxCli | String(020) | Sim | Número do FAX do cliente |
| CxaPst | Number(006,0) | Sim | Número da caixa postal do cliente |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| CodRoe | String(003) | Sim | Código da Rota ou Localidade do Cliente |
| SeqRoe | Number(004,0) | Sim | Sequência da rota ou localidade |
| CodFor | Number(009,0) | Sim | Código do cliente como fornecedor |
| CliRep | Number(009,0) | Sim | Código do cliente como representante |
| CliTra | Number(009,0) | Sim | Código do cliente como transportadora |
| UsuCad | Number(010,0) | Sim | Usuário responsável pelo cadastramento |
| DatCad | Date | Sim | Data início do cadastramento do cliente |
| DatFim | Date | Sim | Data fim do cadastramento do cliente |
| HorCad | Number(005,0) | Sim | Hora/minuto do início do cadastramento do cliente |
| HorFim | Number(005,0) | Sim | Hora/minuto final do cadastramento do cliente |
| DatVct | Date | Sim | Data do vencimento do cadastro do cliente |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| QtdAtu | Number(004,0) | Sim | Quantidade de renovações cadastrais do cliente |
| DatIcv | Date | Sim | Data inicial Vendor |
| SitCli | String(001) | Não | Situação do cliente |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do cliente |
| BloCre | String(001) | Sim | Indicativo se o motivo bloqueia crédito para o cliente (Faturamento) |
| ObsMot | String(250) | Sim | Observação do motivo da situação do cliente |
| UsuMot | Number(010,0) | Sim | Usuário responsável pelo motivo da situação do cliente |
| DatMot | Date | Sim | Data do motivo da situação do cliente |
| HorMot | Number(005,0) | Sim | Hora do motivo da situação do cliente |
| UsuOpe | Number(010,0) | Sim | Código da operadora de cadastrou o cliente |
| CodAma | String(030) | Sim | Código do cliente no Amadeus |
| CodSab | String(030) | Sim | Código do cliente no Sabre |
| CodGal | String(030) | Sim | Código do cliente no Galileo |
| TriIcm | String(001) | Sim | Indicativo se o cliente tem tributação de ICMS ou não |
| TriIpi | String(001) | Sim | Indicativo se o cliente tem tributação de IPI ou não |
| BaiEnt | String(075) | Sim | Bairro de Entrega do cliente |
| BaiCob | String(075) | Sim | Bairro de Cobrança do cliente |
| CliFor | String(001) | Sim | Indicativo se o registro representa um cliente ou um fornecedor ou ambos |
| IdeCli | String(020) | Sim | Código para identificação do cliente |
| TriPis | String(001) | Sim | Indicativo se o cliente tem tributação de PIS ou não |
| TriCof | String(001) | Sim | Indicativo se o cliente tem tributação de COFINS ou não |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| RetCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de Cofins |
| RetCsl | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de CSLL |
| RetPis | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de PIS |
| RetOur | String(001) | Sim | Indicativo se as notas fiscais poderão ter Outras Retenções |
| CodSro | String(003) | Sim | Código da Sub Rota |
| DatSuf | Date | Sim | Data de validade do registro do SUFRAMA |
| CepFre | Number(008,0) | Sim | Faixa inicial do CEP para cálculo do frete no pedido |
| CodPdv | Number(009,0) | Sim | Código interno no PDV |
| DatPdv | Date | Sim | Data da última alteração para o PDV |
| HorPdv | Number(005,0) | Sim | Hora/minuto da última alteração para o PDV |
| RetPro | String(001) | Sim | Indicativo se o cliente controla retenções de PIS, Cofins, CSLL, IRRF, e Outras Retenções por produto |
| RetIrf | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de IRRF |
| LimRet | String(001) | Sim | Indicativo de como é utilizado o valor limite para cálculos de retenção para o cliente nas notas fiscais de saída |
| CodCnv | Number(004,0) | Sim | Código do convênio |
| CalFun | String(001) | Sim | Indicativo se calcula Funrural nas notas fiscais de saídas. |
| EenCli | String(018) | Sim | Código do endereço do cliente |
| EenEnt | String(018) | Sim | Código do endereço de entrega do cliente |
| EenCob | String(018) | Sim | Código do endereço de cobrança do cliente |
| PerAin | Number(004,2) | Sim | Percentual adicional do INSS |
| NenCli | String(060) | Sim | Número do Endereço do Cliente |
| NenEnt | String(060) | Sim | Número do endereço de entrega do cliente |
| NenCob | String(060) | Sim | Número do endereço de cobrança do cliente |
| TipAce | Number(001,0) | Não | Tipo de acerto(arredondamento) do cliente |
| EmaNfe | String(100) | Sim | Endereço eletrônico (E-Mail) para envio de arquivos de documentos eletrônicos |
| InsAnp | Number(007,0) | Sim | Código da instalação conforme cadastro da ANP |
| IndCoo | String(001) | Sim | Indicativo se cliente/fornecedor é cooperado. |
| CodRtr | Number(001,0) | Sim | Código do Regime Tributário |
| RegEst | Number(002,0) | Sim | Regime Especial de Tributação (Meramente Informativo para NF-e) |
| NatRet | Number(002,0) | Sim | Indicador de natureza da retenção na fonte de PIS e Cofins |
| NatPis | Number(005,0) | Sim | Natureza da receita do PIS |
| NatCof | Number(005,0) | Sim | Natureza da receita do COFINS |
| NatIrp | Number(002,0) | Sim | Indicador de natureza da retenção na fonte de IRPJ (SPED) |
| NatCsl | Number(002,0) | Sim | Indicador de natureza da retenção na fonte de CSLL (SPED) |
| NumIdf | String(040) | Sim | Número de identificação fiscal |
| CodMsg | Number(004,0) | Sim | Código da mensagem - 1 |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 |
| CalSen | String(001) | Sim | Indicativo se calcula Senar nas notas fiscais de saídas |
| TipEmp | Number(002,0) | Sim | Tipo de empresa |
| ConFin | String(001) | Sim | Consumidor Final (deprecado a partir da versão 5.8.3) |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| EntPaa | String(001) | Sim | Entidade inscrita no Programa de Aquisição de Alimentos (PAA) |
| ClaTri | Number(002,0) | Sim | Código da classificação tributária para o Reinf |
| DatSpc | Date | Sim | Data da última consulta do SPC |
| CidSpc | String(060) | Sim | Cidades de pesquisa e de Intercâmbio do SPC |
| InfSpc | Number(001,0) | Sim | Informação levantada junto ao SPC |
| UsuSpc | Number(010,0) | Sim | Usuário responsável pela última atualização SPC |
| IndNif | Number(001,0) | Sim | Indicativo do Número de Identificação Fiscal |
| MsgPdv | String(250) | Sim | Mensagem a ser exibida ao caixa ao identificar o cliente no PDV |
| TipVin | Number(001,0) | Sim | Tipo de vinculação do cliente com a empresa |
| CodTaf | String(060) | Sim | Código do participante no arquivo da TAF |
| VlrLat | String(100) | Sim | Valor da Latitude |
| VlrLon | String(100) | Sim | Valor da Longitude |
| CatEst | String(003) | Sim | Categoria do estabelecimento |
| TipAse | Number(002,0) | Sim | Tipo de assinante |
| FinCib | String(003) | Sim | Aplicação da CBS/IBS |
| TipEgo | Number(001,0) | Sim | Tipo de ente governamental |
| IndSpf | String(001) | Sim | Indicativo se o serviço é prestado fisicamente |
| MecCet | Number(002,0) | Sim | Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço |
| CaePfi | String(014) | Sim | Cadastro de Atividade Econômica da Pessoa Física (CAEPF) |
| IndCon | Number(001,0) | Sim | Indicador de Contribuinte do Regime Regular do IBS/CBS para NFE ABI |
| USU_despec | Number(005,2) | Sim | Desc. Peca |
| USU_LisPla | String(001) | Sim | Cliente que recebe somente Lista de Precos de Plantio |
| USU_lispro | String(001) | Sim | Cliente que recebe somente Lista de Precos de Preparo de Solo |
| USU_lispec | String(001) | Sim | Cliente que recebe somente Lista de Precos de Pecas |
| USU_LisTra | String(001) | Sim | Cliente que recebe somente Lista de Precos Tracao Animal |
| USU_desadi | Number(005,2) | Sim | Desconto Adicional |
| USU_desrev | Number(005,2) | Sim | Desconto Revenda |
| USU_datvimp1 | Date | Sim | Data Validade Tabela Preco Implemento WEB |
| USU_tapimp | String(004) | Sim | Tabela de preco implementos valido para WEB |
| USU_dtvpec | Date | Sim | Data Validade Tabela Preco Pecas WEB |
| USU_CodRaf | String(005) | Sim | Ramo de Atividade para Fiscal |
| USU_codemp | Number(004,0) | Sim | Codigo da Empresa |
| USU_clicat | Number(013,0) | Sim | Cliente catalogo |
| USU_NaoEntFut | String(001) | Sim | Nao Aceita Entrega Futura |
| USU_NumJoi | Number(004,0) | Sim | Visão Unica |
| USU_TPMAIL | String(100) | Sim | E-Mail Resposável Site Tabela Preço |
| USU_TPRESP | String(100) | Sim | Nome do Resposável Site Tabela Preço |
| USU_TPFONE | String(020) | Sim | Telefone do Resposável Site Tabela Preço |
| USU_TPSEMG | String(001) | Sim | Segmento do Cliente Site Tabela Preço |
| USU_AceDesTit | String(001) | Sim | ACEITA DESCONTO DE TÍTULOS |
| USU_DocRuc | String(010) | Sim | Documento RUC |
| USU_PagBol | String(001) | Sim | Pago por Boleto |
| USU_PUBALV | String(003) | Sim | CRM: Público Alvo |
| USU_TAMPRO | String(003) | Sim | CRM: Tamanho da Propriedade |
| USU_CULTUR | String(003) | Sim | CRM: Tipo de Cultura |
| USU_EMBSEG | String(003) | Sim | CRM: Emb. do Agro - Segmentação |
| USU_ZAPCLI | String(020) | Sim | Número do Whatsapp |
| USU_AtuGeo | String(001) | Sim | Atualizar Geolocalização |
| USU_SFIDProc | Number(010,0) | Sim | Salesforce - ID Processo de Cadastro |
| USU_CliEst | String(001) | Sim | Cliente Estratégico |
| USU_VALDOC | Date | Sim | Data da Validade da Documentação do Financeiro |
| USU_ComExp | String(001) | Sim | Comercial Exportadora |

---

## Chave Primária

- CodCli

---

## Índices

### E085CLIIndice2

**Tipo:** Unico

Campos:
- CgcCpf
- DocIde
- CodCli

---

## Relacionamentos

Nenhum relacionamento cadastrado.
