# R350ADM

## Descrição

S-2200 - eSocial - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador

---

## Resumo

- Campos: 181
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqAdm | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de Inscrição do Contribuinte |
| CfjIns | String(014) | Sim | Número de Inscrição do Contribuinte |
| CpfTra | Number(011,0) | Sim | Número do CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado |
| NomTra | String(070) | Sim | Nome do trabalhador |
| SexTra | String(001) | Sim | Sexo do trabalhador |
| RacCor | Number(001,0) | Sim | Raça e cor do trabalhador |
| EstCiv | Number(001,0) | Sim | Estado civil do trabalhador |
| GraIns | Number(002,0) | Sim | Grau de instrução do trabalhador |
| PriEmp | String(001) | Sim | Indica se trata-se do primeiro emprego do trabalhador |
| NomSoc | String(070) | Sim | Nome social do colaborador para travesti ou transexual |
| DatNas | Date | Sim | Data de nascimento do trabalhador |
| CodMun | Number(007,0) | Sim | Código do município |
| SigEst | String(002) | Sim | Sigla da Unidade da Federação |
| PaiNas | Number(003,0) | Sim | Código do país de nascimento do trabalhador |
| PaiNac | Number(003,0) | Sim | Código do país de nacionalidade do trabalhador |
| NomMae | String(070) | Sim | Nome da mãe do trabalhador |
| NomPai | String(070) | Sim | Nome do Pai do Trabalhador |
| NumCtp | String(011) | Sim | Número da carteira de trabalho e Previdência Social do trabalhador - CTPS |
| SerCtp | String(005) | Sim | Número de série da CTPS |
| EstCtp | String(002) | Sim | UF da expedição da CTPS |
| NumRIC | Number(014,0) | Sim | Número do RIC |
| OrgRic | String(020) | Sim | Órgão emissor do documento |
| DatRIC | Date | Sim | Data da expedição do documento |
| NumIde | String(014) | Sim | Número do RG |
| OrgIde | String(020) | Sim | Órgão emissor do documento |
| DatIde | Date | Sim | Data da expedição do documento |
| NumRNE | String(014) | Sim | Número de inscrição no Registro Nacional de Estrangeiros |
| OrgRNE | String(020) | Sim | Órgão emissor do documento. |
| DatRNE | Date | Sim | Data da expedição do documento |
| NumOrc | String(014) | Sim | Número de Inscrição no Órgão de Classe |
| OrgOrc | String(020) | Sim | Órgão emissor do documento |
| DatOrc | Date | Sim | Data da expedição do documento |
| ValOrc | Date | Sim | Data de validade |
| NumCNH | String(012) | Sim | Número da CNH |
| DatCNH | Date | Sim | Data da expedição do documento |
| EstCNH | String(002) | Sim | Estado da Federação emissor da CNH |
| ValCNH | Date | Sim | Data de Validade |
| PriCNH | Date | Sim | Data da primeira habilitação |
| CatCNH | String(002) | Sim | Categoria da Carteira de Habilitação |
| TipLog | String(004) | Sim | Tipo de Logradouro |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| BaiLog | String(060) | Sim | Nome do bairro/distrito |
| CEPLog | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunLog | Number(007,0) | Sim | Código do município |
| EstLog | String(002) | Sim | Sigla da Unidade da Federação |
| PaiLog | Number(003,0) | Sim | Código do país |
| CidLog | String(050) | Sim | Nome da Cidade |
| PosLog | String(012) | Sim | Código de Endereçamento Postal - estrangeiro |
| DatChe | Date | Sim | Data de chegada do trabalhador ao Brasil, em caso de estrangeiro |
| ClaEst | Number(002,0) | Sim | Classificação da condição do trabalhador estrangeiro no Brasil |
| CasBra | String(001) | Sim | Condição de casado com brasileiro(s) em caso de trabalhador estrangeiro |
| FilBra | String(001) | Sim | Se o trabalhador estrangeiro tem filhos com brasileiro |
| TmpRes | Number(001,0) | Sim | Tempo de residência do trabalhador imigrante |
| ConIng | Number(001,0) | Sim | Condição de ingresso do trabalhador imigrante |
| DefFis | String(001) | Sim | Def. Física |
| DefVis | String(001) | Sim | Deficiência Visual |
| DefAud | String(001) | Sim | Deficiência Auditiva |
| DefMen | String(001) | Sim | Deficiência Mental |
| DefInt | String(001) | Sim | Deficiência intelectual. |
| TraRea | String(001) | Sim | Reabilitado |
| CotDef | String(001) | Sim | Preenche cota pessoas com deficiência habilitadas ou beneficiários reabilitados |
| ObsDef | String(255) | Sim | Observação |
| TelPri | String(013) | Sim | Telefone Principal |
| TelAlt | String(013) | Sim | Telefone Alternativo |
| EmaPri | String(060) | Sim | E-Mail Principal |
| EmaAlt | String(060) | Sim | E-Mail Alternativo |
| MatTra | String(030) | Sim | Matrícula do Trabalhador |
| RegTra | Number(001,0) | Sim | Tipo de regime trabalhista |
| RegPre | Number(002,0) | Sim | Tipo de regime previdenciário |
| RecPre | String(040) | Sim | Número do recibo do evento S-2190 |
| CadIni | String(001) | Sim | Indicar se o evento se refere a cadastramento inicial de vínculo ou se refere a uma admissão |
| DatAdm | Date | Sim | Data de admissão ou, em caso de sucessão, data de admissão no primeiro empregador |
| TipAdm | Number(001,0) | Sim | Tipo de admissão do trabalhador |
| IndAdm | Number(001,0) | Sim | Indicativo Admissão |
| RegJor | Number(001,0) | Sim | Regime de Jornada do empregado |
| NatAti | Number(001,0) | Sim | Natureza da atividade |
| DatBas | Number(002,0) | Sim | Mês relativo à data base da categoria profissional do trabalhador. |
| SinCat | Number(014,0) | Sim | CNPJ do sindicado ao qual o trabalhador encontra-se filiado |
| CfjSin | String(014) | Sim | CNPJ do sindicado ao qual o trabalhador encontra-se filiado |
| OpcFGT | Number(001,0) | Sim | Opção pelo FGTS |
| DatFGT | Date | Sim | Data de opção pelo FGTS do trabalhador |
| HipLeg | Number(001,0) | Sim | Hipótese legal para contratação de trabalhador temporário |
| JusCtr | String(999) | Sim | Justificativa da hipótese legal para a contratação de trabalho temporário |
| IncCtr | Number(001,0) | Sim | Tipo de inclusão de contrato |
| TInTmp | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do tomador de serviços |
| NInTmp | String(014) | Sim | Número de inscrição do tomador de serviços |
| TInEst | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do estabelecimento |
| NInEst | String(014) | Sim | Número de inscrição do estabelecimento |
| CPFSub | Number(011,0) | Sim | Cpf Colaborador substituido |
| IndPrv | Number(001,0) | Sim | Indicativo do Provimento |
| TipPrv | Number(002,0) | Sim | Tipo de Provimento |
| DatNom | Date | Sim | Data da nomeação do servidor |
| DatPos | Date | Sim | Data da posse do servidor |
| DatExe | Date | Sim | Data da entrada em exercício pelo servidor |
| PanSeg | Number(002,0) | Sim | Tipo de plano de segregação da massa |
| TetRgp | String(001) | Sim | Indicar se o servidor está sujeito ao teto do RGPS |
| IndAbo | String(001) | Sim | Indicar se o servidor recebe abono permanência |
| DatAbo | Date | Sim | Data de início do abono de permanência |
| ProDJu | String(020) | Sim | Número do processo da decisão judicial |
| CarEso | String(030) | Sim | Código do Cargo |
| DesCar | String(100) | Sim | Descrição do cargo |
| CodCbo | String(006) | Sim | Cbo 2002 do Cargo |
| IngSer | Date | Sim | Data do ingresso do servidor no cargo |
| CodFun | String(030) | Sim | Código da Função |
| DesFun | String(100) | Sim | Descrição da função |
| CboFun | String(006) | Sim | Cbo 2002 da Função |
| AcuCaF | String(001) | Sim | Indicar se cargo, emprego ou função pública é acumulável |
| CodCat | Number(004,0) | Sim | Código da categoria |
| SalFix | Number(014,2) | Sim | Salário fixo do trabalhador |
| UndFix | Number(001,0) | Sim | Unidade de pagamento da parte fixa da remuneração |
| DesVar | String(999) | Sim | Descrição do salário variável e como este é calculado |
| TipCon | Number(001,0) | Sim | Tipo de contrato de trabalho |
| TerCon | Date | Sim | Data do Término do contrato |
| ClaAss | String(001) | Sim | Indicativo se o contrato contém cláusula assecuratória |
| ObjDet | String(255) | Sim | Objetivo do término de contrato por prazo determinado |
| TInLoc | Number(001,0) | Sim | Tipo de inscrição do estabelecimento |
| NInLoc | String(014) | Sim | Número de inscrição do estabelecimento |
| DesLoc | String(080) | Sim | Descrição complementar do local de trabalho |
| LogDom | String(004) | Sim | Tipo de Logradouro |
| DesDom | String(080) | Sim | Descrição do logradouro |
| NumDom | String(010) | Sim | Número do logradouro |
| CplDom | String(030) | Sim | Complemento do logradouro |
| BaiDom | String(090) | Sim | Nome do bairro/distrito |
| CepDom | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunDom | Number(007,0) | Sim | Código do município |
| EstDom | String(002) | Sim | Sigla da Unidade da Federação |
| HorSem | Number(004,2) | Sim | Quantidade média de horas relativas à jornada semanal do trabalhador |
| TipJor | Number(002,0) | Sim | Tipo de Jornada |
| VinCTP | Number(002,0) | Sim | Contrato a Tempo Parcial |
| HorNot | String(001) | Sim | Jornada semanal possui horário noturno (no todo ou em parte). |
| DesJor | String(999) | Sim | Descrição do tipo de jornada |
| JorTmp | String(001) | Sim | Contr. de trab. em regime de tempo parcial, cuja jornada não exceda 25 horas semanais |
| SinFil | Number(014,0) | Sim | CNPJ do sindicato ao qual o trabalhador encontra-se filiado (1) |
| CfjFil | String(014) | Sim | CNPJ do sindicato ao qual o trabalhador encontra-se filiado (1) |
| SinFi2 | Number(014,0) | Sim | CNPJ do sindicato ao qual o trabalhador encontra-se filiado (2) |
| CfjFi2 | String(014) | Sim | CNPJ do sindicato ao qual o trabalhador encontra-se filiado (2) |
| NumPro | String(021) | Sim | Número do processo judicial |
| TInAnt | Number(001,0) | Sim | Tipo de inscrição do empregador anterior |
| ProCel | String(021) | Sim | Número do processo trabalhista celetista |
| EmpAnt | Number(014,0) | Sim | CNPJ/CPF do empregador anterior |
| CfjAnt | String(014) | Sim | CNPJ/CPF do empregador anterior |
| MatAnt | String(030) | Sim | Matrícula do trabalhador no empregador anterior |
| DatTrf | Date | Sim | Data de transferência do empregado para o empregador declarante |
| ObsAnt | String(255) | Sim | Observação |
| DatAfa | Date | Sim | Data de início do afastamento |
| MotAfa | Number(002,0) | Sim | Motivo de afastamento temporário |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| CodVin | Number(002,0) | Sim | Código do Vínculo |
| EnvVal | String(001) | Sim | Envio Válido |
| OriRei | String(001) | Sim | Identifica registro originado na reintegração |
| TipIea | Number(001,0) | Sim | Tipo de Inscrição do Empregador de Contratação Indireta do Aprendiz (CNPJ/CPF) |
| NumIea | Number(015,0) | Sim | Número da Inscrição do Contratante Indireto do Aprendiz |
| CfjIea | String(014) | Sim | Número da Inscrição do Contratante Indireto do Aprendiz |
| DatDem | Date | Sim | Data do último dia trabalhado para o respectivo vínculo |
| CPFAnt | Number(011,0) | Sim | CPF do trabalhador |
| MatCPF | String(030) | Sim | Matrícula Anterior |
| DatCPF | Date | Sim | Data de Alteração do CPF |
| ObsCPF | String(255) | Sim | Observação da Alteração de CPF |
| DatCes | Date | Sim | Data de Início da Cessão |
| IndCtr | Number(001,0) | Sim | Indicativo de Contratação |
| NumQua | Number(014,0) | Sim | CNPJ Entidade Qualificadora |
| CfjQua | String(014) | Sim | CNPJ Entidade Qualificadora |
| NumPra | Number(014,0) | Sim | CNPJ Atividades Práticas |
| CfjPra | String(014) | Sim | CNPJ Atividades Práticas |
| MAntJd | String(030) | Sim | Matrícula do funcionário na anotação judicial |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqAdm

---

## Índices

### R350ADMIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
