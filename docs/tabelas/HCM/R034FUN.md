# R034FUN

## Descrição

Ficha Básica Colaborador

---

## Resumo

- Campos: 194
- Chave Primária: 3 campo(s)
- Índices: 11
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| NomFun | String(040) | Sim | Nome do Colaborador |
| ApeFun | String(050) | Sim | Apelido do Colaborador |
| DatAdm | Date | Sim | Data de Admissão |
| TipAdm | Number(002,0) | Sim | Tipo de Admissão |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| CodTap | Number(003,0) | Sim | Tipo de atuação do Colaborador no Posto de trabalho |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Posto de Trabalho em que o Colaborador atua |
| CodEtb | Number(002,0) | Sim | Código Estabilidade |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| CodTma | Number(001,0) | Sim | Código da Turma da Escala |
| TurInt | Number(009,0) | Sim | Código da Turma de Intervalo |
| CodFil | Number(006,0) | Sim | Código da Filial |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodCcu | String(018) | Sim | Centro Custo |
| TipCon | Number(002,0) | Sim | Tipo de Contrato |
| TipSex | String(001) | Sim | Sexo do Colaborador |
| EstCiv | Number(001,0) | Sim | Estado Civil |
| GraIns | Number(002,0) | Sim | Grau de Instrução |
| DatNas | Date | Sim | Data de Nascimento |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| AnoChe | Number(004,0) | Sim | Ano de Chegada |
| VisEst | Number(002,0) | Sim | Classificação da condição do estrangeiro no Brasil |
| RegEst | String(014) | Sim | Carteira de Estrangeiro |
| DvlEst | Date | Sim | Data de Validade da Carteira de Estrangeiro |
| DvlCtp | Date | Sim | Data de Validade da Carteira de Trabalho (Estrangeiro) |
| NumCtp | Number(009,0) | Sim | Número da Carteira de Trabalho |
| SerCtp | String(005) | Sim | Série da Carteira de Trabalho |
| EstCtp | String(002) | Sim | UF da Carteira de Trabalho |
| DexCtp | Date | Sim | Data de Expedição da Carteira de Trabalho |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| DcdPis | Date | Sim | Data de Cadastramento no PIS/PASEP |
| SocSin | String(001) | Sim | Sócio do Sindicato |
| PagSin | String(001) | Sim | Contribuição Sindical no Ano |
| TipOpc | String(001) | Sim | Optante do FGTS |
| DatOpc | Date | Sim | Data de Opção do FGTS |
| ConFgt | Number(011,0) | Sim | Conta do FGTS |
| PerJur | Number(001,0) | Sim | Percentual de Juros do FGTS |
| DepIrf | Number(002,0) | Sim | Número de Dependentes do IR |
| DepSaf | Number(002,0) | Sim | Número de Dependentes do Salário Família |
| ModPag | String(001) | Sim | Modo de Pagamento do Salário |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| ConBan | Number(012,0) | Sim | Conta Bancária |
| DigBan | String(003) | Sim | Dígito da Conta Bancária |
| PerPag | String(001) | Sim | Período de Pagamento |
| TipApo | Number(001,0) | Sim | Tipo da Aposentadoria |
| DatApo | Date | Sim | Data da Aposentadoria |
| ValSup | Number(011,2) | Sim | Valor Suplementar |
| EscVtr | Number(005,0) | Sim | Código da Escala do Vale Transporte |
| PonEmb | Number(004,0) | Sim | Ponto de embarque |
| RecAdi | String(001) | Sim | Recebe Adiantamento de Salário |
| Rec13s | String(001) | Sim | Recebe 13° Salário |
| LisRai | String(001) | Sim | Lista Colaborador na RAIS |
| EmiCar | String(001) | Sim | Emitir Cartão Ponto Para o Colaborador |
| CodCha | String(006) | Sim | Código da Chapeira |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatInc | Date | Sim | Data de Inclusão p/ Ficha Registro |
| HorInc | Number(005,0) | Sim | Hora de Inclusão p/ Ficha Registro |
| SalSim | Number(013,4) | Sim | Valor do Salário Simulado |
| DatSim | Date | Sim | Data da Última Simulação de Salário |
| OutCon | String(001) | Sim | Outro Contrato de Trabalho |
| OutTet | String(001) | Sim | Teto INSS no Outro Contrato |
| OutEmp | Number(004,0) | Sim | Código da Empresa no Outro Contrato |
| OutTip | Number(001,0) | Sim | Tipo do Colaborador no Outro Contrato |
| OutCad | Number(009,0) | Sim | Código do Cadastro no Outro Contrato |
| UltCal | Number(005,0) | Sim | Indicador do Ultimo Processamento que o Colaborador Participou |
| SitRec | String(001) | Sim | Situação do Último Processamento |
| ConRho | Number(001,0) | Sim | Colaborador Considerado p/ Cálculo no Ronda |
| PerDes | Number(005,2) | Sim | Percentual de Desempenho |
| ValSal | Number(013,4) | Sim | Valor do Último Salário |
| CplSal | Number(013,4) | Sim | Valor do Último Salário Complementar |
| DatSal | Date | Sim | Data da Última Alteração Salarial |
| CodMot | Number(003,0) | Sim | Motivo da Última Alteração de Salário |
| TipSal | Number(001,0) | Sim | Tipo do Último Salário |
| CodEst | Number(004,0) | Sim | Código da Última Estrutura Salarial |
| ClaSal | String(005) | Sim | Última Classe Salarial |
| NivSal | String(005) | Sim | Último Nível Salarial |
| DatAfa | Date | Sim | Data do Último Afastamento |
| HorAfa | Number(005,0) | Sim | Hora do Último Afastamento |
| CauDem | Number(002,0) | Sim | Causa de Demissão |
| DatPos | Date | Sim | Data da Última Alteração de Posto |
| DatCar | Date | Sim | Data da Última Alteração de Cargo |
| MotCar | Number(003,0) | Sim | Motivo da Última Alteração de Cargo |
| DatEsc | Date | Sim | Data da Última Alteração de Escala |
| DatLoc | Date | Sim | Data da Última Alteração de Local |
| DatCcu | Date | Sim | Data da Última Alteração de Centro de Custo |
| DatFil | Date | Sim | Data da Última Alteração de Filial |
| CadFil | Number(009,0) | Sim | Novo Cadastro na Alteração de Filial |
| EmpFil | Number(006,0) | Sim | Nova Empresa na Alteração de Filial |
| DatEtb | Date | Sim | Data da Última Alteração de Estabilidade |
| DatAdi | Date | Sim | Data da Última Alteração de Adicionais |
| PerIns | Number(005,2) | Sim | Percentual de Insalubridade |
| PerPer | Number(005,2) | Sim | Percentual de Periculosidade |
| ApoEsp | Number(002,0) | Sim | Número de Anos p/ Aposentadoria Especial |
| PerIss | Number(004,2) | Sim | Percentual de ISS |
| HorBas | Number(004,0) | Sim | Horário Base (Segunda  a Sexta) |
| HorSab | Number(004,0) | Sim | Horário no Sábado |
| HorSem | Number(010,0) | Sim | Horas Semanais |
| HorDsr | Number(010,0) | Sim | Horas DSR |
| DepSld | Number(011,2) | Sim | Valor do Depósito do Saldo do FGTS |
| JamSld | Number(011,2) | Sim | Valor do JAM do Saldo do FGTS |
| DatSld | Date | Sim | Data do Saldo do FGTS |
| FaiIns | Number(002,0) | Sim | Faixa de Contribuição Carnê |
| OpcAtu | String(001) | Sim | Atualização Automática Classe |
| EmtCar | String(001) | Sim | Carnê INSS |
| NumIns | Number(011,0) | Sim | Número da Inscrição no INSS |
| DctIns | Number(001,0) | Sim | Desconta INSS |
| CadFol | String(015) | Sim | Cadastro na Folha |
| DInCra | Date | Sim | Data da Última Alteração de Crachá |
| HInCra | Number(005,0) | Sim | Hora da Última Alteração de Crachá |
| EliMar | Number(001,0) | Sim | Eliminar Marcações |
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
| DefFis | String(001) | Sim | Deficiente Habilitado ou Reabilitado |
| PerRea | Number(008,5) | Sim | % Reajuste |
| GpsTri | Date | Sim | Início da GPS Trimestral |
| RacCor | Number(002,0) | Sim | Código da Raça/Etnia |
| DedCar | String(001) | Sim | Dedução Carnê |
| CodFor | Number(009,0) | Sim | Código Fornecedor |
| RatEve | String(001) | Sim | Ratear Eventos da Ficha Financeira |
| PerTra | Number(005,2) | Sim | Percentual Base INSS Transportista |
| PerIrt | Number(005,2) | Sim | % Base IR Transportista |
| CodDef | Number(002,0) | Sim | Código da Deficiência |
| CatSef | Number(002,0) | Sim | Categoria Sefip |
| DedIns | Number(004,2) | Sim | % Desconto INSS |
| DigCar | String(002) | Sim | Dígito da Carteira de Trabalho |
| MovSef | String(002) | Sim | Código de Movimento Sefip para Aposentadoria |
| BenRea | String(001) | Sim | Beneficiário reabilitado(S/N) |
| CodGLo | Number(002,0) | Sim | Grupo de Localização |
| TipSrv | Number(001,0) | Sim | Tipo de Serviço para Transporte Coletivo |
| BusHor | Number(001,0) | Sim | Buscar Horário na Data. |
| NmFun1 | String(050) | Sim | Nome do Colaborador |
| NmFun2 | String(050) | Sim | Nome do Colaborador |
| NmFun3 | String(050) | Sim | Nome do Colaborador |
| NmFun4 | String(050) | Sim | Nome do Colaborador |
| RecGra | String(001) | Sim | Colaborador recebe gratificação |
| DocEst | Number(002,0) | Sim | Tipo de Documento de Estrangeiro |
| CodIdn | Number(015,0) | Sim | Código de identificação do colaborador |
| SisCes | Number(001,0) | Sim | Sistema Cesantía |
| OpcCes | Date | Sim | Opção Cesantía |
| TpCtBa | Number(001,0) | Sim | Tipo Conta |
| CodLim | Number(004,0) | Sim | Código Limite de Isenção ISS Terceiro |
| IrrIse | String(001) | Sim | IR Isento |
| ApoIda | String(001) | Sim | Aposentadoria Apenas por Idade |
| RetTrp | String(001) | Sim | Transportador com Retenção Sest/Senat |
| CodVin | Number(002,0) | Sim | Código do Vínculo |
| DatVin | Date | Sim | Data da Última Alteração de Vínculo |
| DatSin | Date | Sim | Data da Última Alteração de Sindicato |
| CodPes | Number(009,0) | Sim | Código da Pessoa |
| DatEvt | Date | Sim | Data da Última Alteração da Escala VTR |
| TemHCt | Number(001,0) | Sim | Colaborador Possui Histórico de Contrato |
| StaHCt | Number(001,0) | Sim | Status do Histórico de Contrato |
| DatHCt | Date | Sim | Data da última alteração do histórico de contrato |
| NumPsp | String(020) | Sim | Número Passaporte para controle Alfandegado. |
| DatChe | Date | Sim | Data de chegada ao Brasil |
| DatSef | Date | Sim | Data da Última Alteração de Categoria SEFIP |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| GesPon | String(001) | Sim | Gestão do Ponto |
| CodPro | Number(009,0) | Sim | Número do processo judicial |
| CateSo | Number(004,0) | Sim | Código da categoria eSocial |
| DatCes | Date | Sim | Data da última alteração da categoria eSocial |
| CotDef | String(001) | Sim | Preenche cota pessoas com deficiência habilitadas ou beneficiários reabilitados |
| ForPro | String(255) | Sim | Formação do profissional responsável pelo treinamento/capacitação |
| CodCbo | String(006) | Sim | CBO referente à formação do profissional responsável p/ treinamento/capacitação |
| StaAlf | Number(001,0) | Sim | Status da permissão para o local alfandegado |
| DatRei | Date | Sim | Data de Reintegração |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |
| DeSusp | String(001) | Sim | Desconsiderar Período de Suspensão |
| GpoLit | String(001) | Sim | Gestão do Ponto Lite |
| CodOpe | Number(004,0) | Sim | Código de Operação da Conta Bancária |
| USU_ObsRh | String(150) | Sim | Observac?es do RH |
| USU_CobRef | String(001) | Sim | Cobrar Refeic?o |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

### R034FUNIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NomFun

### R034FUNIndice3

**Tipo:** Não unico

Campos:
- NumPis
- NumEmp

### R034FUNIndice4

**Tipo:** Não unico

Campos:
- NumCpf

### R034FUNIndice5

**Tipo:** Não unico

Campos:
- CodEsc

### R034FUNIndice6

**Tipo:** Não unico

Campos:
- NumEmp
- CodFil
- NomFun

### R034FUNIndice7

**Tipo:** Não unico

Campos:
- SitAfa

### R034FUNIndice8

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatAdm

### R034FUNIndice9

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- SitAfa

### R034FUNIndice10

**Tipo:** Não unico

Campos:
- CodPes

### R034FUNIndice11

**Tipo:** Não unico

Campos:
- NumCpf
- NumCad

### R034FUNIndice12

**Tipo:** Não unico

Campos:
- NomFun

---

## Relacionamentos

### IR_R034FUN_007

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitAfa | CodSit |

### IR_R034FUN_014

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

### IR_R034FUN_017

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

