# R038HFB

## Descrição

Histórico da Ficha Básica Colaborador

---

## Resumo

- Campos: 107
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatHis | Date | Não | Data e Hora do Histórico da Ficha Básica do Colaborador |
| SeqHis | Number(015,0) | Não | Sequência do Histórico da Ficha Básica |
| TipAlt | String(001) | Sim | Tipo de Operação de Origem do Histórico |
| NomFun | String(040) | Sim | Nome do Colaborador |
| ApeFun | String(050) | Sim | Apelido do Colaborador |
| TipSex | String(001) | Sim | Sexo do Colaborador |
| RacCor | Number(002,0) | Sim | Código da Raça/Etnia |
| EstCiv | Number(001,0) | Sim | Estado Civil |
| GraIns | Number(002,0) | Sim | Grau de Instrução |
| DatNas | Date | Sim | Data de Nascimento |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| NumCtp | Number(009,0) | Sim | Número da Carteira de Trabalho |
| SerCtp | String(005) | Sim | Série da Carteira de Trabalho |
| DigCar | String(002) | Sim | Dígito da Carteira de Trabalho |
| EstCtp | String(002) | Sim | UF da Carteira de Trabalho |
| DexCtp | Date | Sim | Data de Expedição da Carteira de Trabalho |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| DcdPis | Date | Sim | Data de Cadastramento no PIS/PASEP |
| TipApo | Number(001,0) | Sim | Tipo da Aposentadoria |
| DatApo | Date | Sim | Data da Aposentadoria |
| MovSef | String(002) | Sim | Código de Movimento Sefip para Aposentadoria |
| IrrIse | String(001) | Sim | IR Isento |
| ApoIda | String(001) | Sim | Aposentadoria Apenas por Idade |
| EmtCar | String(001) | Sim | Carnê INSS |
| NumIns | Number(011,0) | Sim | Número da Inscrição no INSS |
| CodDef | Number(002,0) | Sim | Código da Deficiência |
| DefFis | String(001) | Sim | Deficiente Habilitado ou Reabilitado |
| BenRea | String(001) | Sim | Beneficiário reabilitado(S/N) |
| NmFun1 | String(050) | Sim | Nome do Colaborador |
| NmFun2 | String(050) | Sim | Nome do Colaborador |
| NmFun3 | String(050) | Sim | Nome do Colaborador |
| NmFun4 | String(050) | Sim | Nome do Colaborador |
| CodPro | Number(009,0) | Sim | Número do processo judicial |
| AnoChe | Number(004,0) | Sim | Ano de Chegada |
| VisEst | Number(002,0) | Sim | Classificação da condição do estrangeiro no Brasil |
| DvlEst | Date | Sim | Data de Validade da Carteira de Estrangeiro |
| RegEst | String(014) | Sim | Carteira de Estrangeiro |
| DvlCtp | Date | Sim | Data de Validade da Carteira de Trabalho (Estrangeiro) |
| DocEst | Number(002,0) | Sim | Tipo de Documento de Estrangeiro |
| DatChe | Date | Sim | Data de chegada ao Brasil |
| NumPsp | String(020) | Sim | Número Passaporte para controle Alfandegado. |
| DatAdm | Date | Sim | Data de Admissão |
| TipAdm | Number(002,0) | Sim | Tipo de Admissão |
| TipCon | Number(002,0) | Sim | Tipo de Contrato |
| TipOpc | String(001) | Sim | Optante do FGTS |
| DatOpc | Date | Sim | Data de Opção do FGTS |
| ConFgt | Number(011,0) | Sim | Conta do FGTS |
| ModPag | String(001) | Sim | Modo de Pagamento do Salário |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| ConBan | Number(012,0) | Sim | Conta Bancária |
| DigBan | String(003) | Sim | Dígito da Conta Bancária |
| PerPag | String(001) | Sim | Período de Pagamento |
| RecAdi | String(001) | Sim | Recebe Adiantamento de Salário |
| Rec13s | String(001) | Sim | Recebe 13° Salário |
| LisRai | String(001) | Sim | Lista Colaborador na RAIS |
| EmiCar | String(001) | Sim | Emitir Cartão Ponto Para o Colaborador |
| CodCha | String(006) | Sim | Código da Chapeira |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| OutCon | String(001) | Sim | Outro Contrato de Trabalho |
| OutTet | String(001) | Sim | Teto INSS no Outro Contrato |
| OutEmp | Number(004,0) | Sim | Código da Empresa no Outro Contrato |
| OutTip | Number(001,0) | Sim | Tipo do Colaborador no Outro Contrato |
| OutCad | Number(009,0) | Sim | Código do Cadastro no Outro Contrato |
| PerDes | Number(005,2) | Sim | Percentual de Desempenho |
| PerIss | Number(004,2) | Sim | Percentual de ISS |
| FaiIns | Number(002,0) | Sim | Faixa de Contribuição Carnê |
| OpcAtu | String(001) | Sim | Atualização Automática Classe |
| DctIns | Number(001,0) | Sim | Desconta INSS |
| CadFol | String(015) | Sim | Cadastro na Folha |
| CatTer | String(001) | Sim | Categoria do Contribuinte |
| FatTpo | Number(004,2) | Sim | Fator do Tempo de Serviço |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável |
| TipRes | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| CadRes | Number(009,0) | Sim | Cadastro do Responsável |
| TipTer | Number(003,0) | Sim | Tipo de Terceiro |
| CauAdv | String(030) | Sim | Tipo de Causa do Terceiro Advogado |
| InsCur | Number(002,0) | Sim | Tipo de Instrutor de Curso |
| AssPpr | Number(001,0) | Sim | Assinalamento do Colaborador p/ PPR |
| DatPpr | Date | Sim | Data Assinalamento PPR |
| VerInt | String(001) | Sim | Consistência Interjornada |
| ConTov | String(001) | Sim | Considerar Admissão p/ Turn-Over |
| ApuPfs | String(001) | Sim | Apuração do Professor |
| TipPfs | String(001) | Sim | Tipo do Professor |
| RatPfs | String(001) | Sim | Tipo de Rateio do Professor |
| GpsTri | Date | Sim | Início da GPS Trimestral |
| DedCar | String(001) | Sim | Dedução Carnê |
| CodFor | Number(009,0) | Sim | Código Fornecedor |
| RatEve | String(001) | Sim | Ratear Eventos da Ficha Financeira |
| PerTra | Number(005,2) | Sim | Percentual Base INSS Transportista |
| PerIrt | Number(005,2) | Sim | % Base IR Transportista |
| DedIns | Number(004,2) | Sim | % Desconto INSS |
| TipSrv | Number(001,0) | Sim | Tipo de Serviço para Transporte Coletivo |
| BusHor | Number(001,0) | Sim | Buscar Horário na Data. |
| RecGra | String(001) | Sim | Colaborador recebe gratificação |
| CodIdn | Number(015,0) | Sim | Código de identificação do colaborador |
| TpCtBa | Number(001,0) | Sim | Tipo Conta |
| CodLim | Number(004,0) | Sim | Código Limite de Isenção ISS Terceiro |
| RetTrp | String(001) | Sim | Transportador com Retenção Sest/Senat |
| DepIrf | Number(002,0) | Sim | Número de Dependentes do IR |
| DepSaf | Number(002,0) | Sim | Número de Dependentes do Salário Família |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatHis
- SeqHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
