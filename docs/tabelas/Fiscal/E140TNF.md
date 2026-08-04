# E140TNF

## Descrição

Tabelas - Notas Fiscais de Saída - Diversos

---

## Resumo

- Campos: 110
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| VlrInt | Number(015,2) | Sim | Valor total de intermediação de serviços na nota de saída |
| VlrBsn | Number(015,2) | Sim | Valor base do Senar |
| VlrSen | Number(015,2) | Sim | Valor do Senar |
| PedCli | String(020) | Sim | Número do pedido do cliente |
| CodSaf | String(010) | Sim | Código da safra |
| VlrIbs | Number(015,2) | Sim | Soma dos valores base do ICMS Simples Nacional dos itens da nota fiscal de saída |
| VlrIsn | Number(015,2) | Sim | Soma dos valores do ICMS Simples Nacional dos itens da nota fiscal de saída |
| FilCes | Number(005,0) | Sim | Filial do controle de Entrada/Saída para pesagem |
| DatCes | Date | Sim | Data do controle de Entrada/Saída para pesagem |
| SeqCes | Number(006,0) | Sim | Sequência de entrada na data |
| TipDev | Number(001,0) | Sim | Tipo de devolução escolhida no processo de saída de mercadorias |
| NumPdv | Number(003,0) | Sim | Número sequencial do PDV |
| IndPre | String(001) | Sim | Indicativo presencial do consumidor |
| DatPre | Date | Sim | Data de prestação do serviço |
| VlrIdv | Number(015,2) | Sim | Valor do IPI devolvido |
| ConCfe | Number(009,0) | Sim | Número do contador de cupom fiscal |
| CatTef | String(128) | Sim | Código de Autorização da Transação para Pagamentos Eletrônicos |
| BasIdf | Number(015,2) | Sim | Soma dos valores base do ICMS diferido dos itens da nota fiscal de saída |
| VlrIdf | Number(015,2) | Sim | Soma dos valores de ICMS diferido dos itens da nota fiscal de saída |
| NumPrc | String(030) | Sim | Número do processo de suspensão da exigibilidade do ISS |
| SomOcl | Number(015,2) | Sim | Soma dos valores originais de CSLL (anterior verificação limite retenção) |
| SomOpt | Number(015,2) | Sim | Soma dos valores originais de PIS (anterior verificação limite retenção) |
| SomOct | Number(015,2) | Sim | Soma dos valores originais de Cofins (anterior verificação limite retenção) |
| SomOor | Number(015,2) | Sim | Soma dos val. orig. de Out. Ret. (anterior verif. do valor limite p/ retenção) |
| OriInv | String(001) | Sim | Nota gerada apartir de inventário (S-Originada, outro valor-não originada) |
| TipEnt | Number(001,0) | Sim | Tipo de entrega |
| ForEnt | String(001) | Sim | Forma de entrega da nota fiscal |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| EdtBco | String(001) | Sim |  |
| CodMd5 | String(032) | Sim | Autenticação digital (MD5) |
| CgcCpf | String(040) | Sim | Identificação do cliente (CNPJ, CPF ou documento de identificação de consumidor estrangeiro) |
| NroEnv | Number(004,0) | Sim | Número de envios |
| DevFin | String(001) | Sim | Indica se a nota fiscal é de devolução financeira |
| BasIef | Number(015,2) | Sim | Soma dos valores base do ICMS dos itens da nota fiscal de saída para entrega futura |
| VlrIef | Number(015,2) | Sim | Soma dos valores do ICMS dos itens da nota fiscal de saída para entrega futura |
| VlrStr | Number(015,2) | Sim | Valor do serviço de transporte |
| CodCfp | Number(004,0) | Sim | CFOP |
| CodMfg | Number(007,0) | Sim | Código do município de ocorrência do fato gerador do ICMS do transporte |
| VlrIor | Number(015,2) | Sim | Soma dos Valores de ICMS partilhado com o estado remetente |
| VlrBde | Number(015,2) | Sim | Soma dos valores da Base de ICMS partilhado com o estado de destino |
| VlrIde | Number(015,2) | Sim | Soma dos valores de ICMS partilhado com o estado destinatário |
| BasFcp | Number(015,2) | Sim | Soma dos valores da base de cálculo do fundo de combate à pobreza |
| VlrFcp | Number(015,2) | Sim | Soma dos valores do fundo de combate à pobreza |
| BstFcp | Number(015,2) | Sim | Soma dos valores das bases de cálculo do FCP retido por substituição tributária |
| VstFcp | Number(015,2) | Sim | Soma dos valores do fundo de combate à pobreza retido por subst. tributária |
| BreFcp | Number(015,2) | Sim | Soma dos valores da Base de cálculo do FCP retido anteriormente por subst. trib. |
| VreFcp | Number(015,2) | Sim | Soma dos valores do FCP retido anteriormente por substituição tributária. |
| IcmBfc | Number(015,2) | Sim | Soma dos valores da base de cálculo do FCP na UF de destino |
| IcmVfc | Number(015,2) | Sim | Valor do ICMS para fundo de combate à pobreza na UF de destino |
| CodCrt | Number(001,0) | Sim | Código do regime tributário da filial na emissão |
| BasApe | Number(015,2) | Sim | Base de cálculo da aposentadoria especial |
| VlrApe | Number(015,2) | Sim | Valor da aposentadoria especial |
| VlrBgi | Number(015,2) | Sim | Base de cálculo do GILRAT |
| VlrGil | Number(015,2) | Sim | Valor do GILRAT |
| EmiTer | String(001) | Sim | Indicativo de Emissão realizada por terceiros |
| LocDsp | String(060) | Sim | Descrição do local de despacho |
| CodDpd | Number(009,0) | Sim | Código do dependente |
| IntRe2 | String(001) | Sim | Registro Integrado para a EFD-Reinf no bloco 2 |
| IntRe4 | String(001) | Sim | Registro Integrado para a EFD-Reinf no bloco 4 |
| CpfDcv | Number(011,0) | Sim | Identificação do dependente (CPF) do convênio. |
| IndItm | String(001) | Sim | Indicativo de intermediador/marketplace |
| CodItm | Number(004,0) | Sim | Código do intermediador da transação |
| CgcItm | Number(014,0) | Sim | CNPJ do intermediador da transação |
| DocIdeItm | String(014) | Sim | CNPJ do intermediador da transação |
| CadItm | String(060) | Sim | Identificador cadastrado no intermediador |
| IdeExt | Number(009,0) | Sim | Número Identificador Externo |
| CtrExt | String(020) | Sim | Número do Contrato Externo |
| CodInt | Number(002,0) | Sim | Código da integração |
| VicSdt | Number(015,2) | Sim | Somatório do valor do ICMS-ST desonerado |
| VdiFcs | Number(015,2) | Sim | Somatório do valor diferido do ICMS relativo ao FCP |
| EfiFcs | Number(015,2) | Sim | Somatório do valor efetivo do ICMS relativo ao FCP |
| DesArm | String(001) | Sim | Identifica se é uma transf. saldo para um armazenador registrado junto ao INDEA |
| DesRev | String(001) | Sim | Identifica se o destino é revenda/prestador serviço registrado junto ao INDEA |
| DocUre | Number(014,0) | Sim | CNPJ da Unidade de Recebimento de Embalagens Vazias |
| DocIdeUre | String(014) | Sim | CNPJ da Unidade de Recebimento de Embalagens Vazias |
| CodCli | Number(009,0) | Sim | Código do Cliente |
| CodPrp | Number(009,0) | Sim | Código da propriedade |
| FilScp | Number(005,0) | Sim | Código da filial SCP onde será escriturado o documento |
| QtmBic | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico |
| VmoIcm | Number(015,2) | Sim | Soma dos valores do ICMS monofásico |
| QtmBir | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Retido |
| VmoIcr | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Retido |
| QtmBif | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Diferido |
| VmoIcf | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Diferido |
| QtmBid | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Destacado |
| VmoIcd | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Destacado |
| CodImr | Number(009,0) | Sim | Identificação do imóvel |
| SeqLci | Number(009,0) | Sim | Identificador de registro |
| TipFat | Number(001,0) | Sim | Tipo faturamento NFCom |
| FinEmi | Number(001,0) | Sim | Finalidade emissão NFCom |
| TipGua | Number(001,0) | Sim | Tipo de Guia Agro |
| UfGuia | String(002) | Sim | UF de emissão da guia |
| SerGui | String(009) | Sim | Série de emissão da guia |
| NumGui | Number(009,0) | Sim | Número da guia |
| CodImo | String(020) | Sim | Código da unidade imobiliária NFS-e |
| CodObr | String(020) | Sim | Código da obra |
| ImoCli | String(020) | Sim | Código da unidade imobiliária do Cliente NFS-e |
| TpoGov | Number(001,0) | Sim | Tipo de Operação com Entes Governamentais ou outros serviços sobre bens imóveis |
| IndSpf | String(001) | Sim | Indicativo se o serviço é prestado fisicamente |
| CodIop | String(006) | Sim | Código indicador da operação de fornecimento para NFS-e |
| CodDes | Number(009,0) | Sim | Código do Destinatário do serviço prestado |
| VinOmb | Number(001,0) | Sim | Vínculo da Operação à Movimentação Temporária de Bens |
| NumDoi | String(020) | Sim | Número da Declaração de Importação |
| PaiRes | String(004) | Sim | Código do país resultante |
| DatPrv | Date | Sim | Data previsão entrega |
| AplAze | Number(001,0) | Sim | Tipo de aplicação da alíquota zero da CBS |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

### E140TNFIndice1

**Tipo:** Não unico

Campos:
- CodEmp

---

## Relacionamentos

### IR_E140TNF_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140TNF_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

