# R350SVI

## Descrição

S-2300 - eSocial - Trabalhador Sem Vínculo de Emprego/Estatutário - Início

---

## Resumo

- Campos: 146
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
| SeqSvi | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| NomTra | String(070) | Sim | Nome do Trabalhador |
| SexTra | String(001) | Sim | Sexo do Trabalhador |
| RacCor | Number(001,0) | Sim | Raça e cor do trabalhador |
| EstCiv | Number(001,0) | Sim | Estado civil do trabalhador |
| GraIns | Number(002,0) | Sim | Grau de instrução do trabalhador |
| NomSoc | String(070) | Sim | Nome social do colaborador para travesti ou transexual |
| DatNas | Date | Sim | Data de nascimento |
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
| OrgRIC | String(020) | Sim | Órgão emissor do documento |
| DatRic | Date | Sim | Data da expedição do documento |
| NumIde | String(014) | Sim | Número do RG |
| OrgIde | String(020) | Sim | Orgão emissor do RG |
| DatIde | Date | Sim | Data de expedição do RG |
| NumRNE | String(014) | Sim | Número de inscrição no Registro Nacional de Estrangeiros |
| OrgRNE | String(020) | Sim | Órgão emissor do documento |
| DatRNE | Date | Sim | Data da expedição do documento |
| NumOrC | String(014) | Sim | Número de Inscrição no Órgão de Classe |
| OrgOrC | String(020) | Sim | Órgão emissor do documento |
| DatOrC | Date | Sim | Data da expedição do documento |
| ValOrC | Date | Sim | Data de validade do documento |
| NumCNH | String(012) | Sim | Número da CNH |
| DatCNH | Date | Sim | Data da expedição do documento |
| EstCNH | String(002) | Sim | Estado da Federação emissor da CNH |
| ValCNH | Date | Sim | Data de validade do documento |
| PriCNH | Date | Sim | Data da primeira habilitação |
| CatCNH | String(002) | Sim | Categoria da CNH |
| TipLog | String(005) | Sim | Tipo de Logradouro |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| BaiLog | String(060) | Sim | Nome do bairro/distrito |
| CEPLog | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunLog | Number(007,0) | Sim | Código do município |
| EstLog | String(002) | Sim | Sigla da Unidade da Federação |
| PaiLog | Number(003,0) | Sim | Código do país |
| CidLog | String(030) | Sim | Nome da cidade |
| PosLog | String(012) | Sim | Código de Endereçamento Postal |
| DatChe | Date | Sim | Data de chegada do trabalhador ao Brasil |
| ClaEst | Number(002,0) | Sim | Classificação da condição do trabalhador estrangeiro Brasil |
| CasBra | String(001) | Sim | Condição de casado com brasileiro(s) em caso de trabalhador estrangeiro |
| FilBra | String(001) | Sim | Se o trabalhador estrangeiro tem filhos com brasileiro |
| TmpRes | Number(001,0) | Sim | Tempo de residência do trabalhador imigrante |
| ConIng | Number(001,0) | Sim | Condição de ingresso do trabalhador imigrante |
| DefFis | String(001) | Sim | Indicar se o trabalhador possui deficiência física |
| DefVis | String(001) | Sim | Indicar se o trabalhador possui deficiência visual |
| DefAud | String(001) | Sim | Indicar se o trabalhador possui deficiência auditiva |
| DefMen | String(001) | Sim | Deficiência Mental |
| DefInt | String(001) | Sim | Deficiência intelectual. |
| TraRea | String(001) | Sim | Informar se o trabalhador é reabilitado. |
| ObsDef | String(255) | Sim | Observações |
| TelPri | String(013) | Sim | Número de telefone do trabalhador |
| TelAlt | String(013) | Sim | Número de telefone alternativo do trabalhador |
| EmaPri | String(060) | Sim | Endereço eletrônico |
| EmaAlt | String(060) | Sim | Endereço eletrônico |
| MatTra | String(030) | Sim | Matrícula do Trabalhador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| DatIni | Date | Sim | Data de início das atividades |
| NumPro | String(020) | Sim | Número do processo da decisão judicial |
| NatAti | Number(001,0) | Sim | Natureza da atividade |
| CodCar | String(030) | Sim | Código do Cargo |
| DesCar | String(100) | Sim | Descrição do cargo |
| CodCbo | String(006) | Sim | Cbo 2002 do Cargo |
| CodFun | String(030) | Sim | Código da função |
| DesFun | String(100) | Sim | Descrição da função |
| CboFun | String(006) | Sim | Cbo 2002 da Função |
| SalFix | Number(014,2) | Sim | Salário fixo do trabalhador |
| UndFix | Number(001,0) | Sim | Unidade de pagamento da parte fixa da remuneração |
| DesVar | String(999) | Sim | Descrição Salário Variável |
| OpcFGT | Number(001,0) | Sim | Indicativo de opção pelo FGTS |
| DatFGT | Date | Sim | Informar a data de opção pelo FGTS do trabalhador |
| CatAnt | Number(004,0) | Sim | Código da categoria origem do trabalhador |
| TipAnt | Number(001,0) | Sim | Tipo de Inscrição |
| EmpAnt | Number(014,0) | Sim | Número de inscrição do empregador anterior |
| CfjAnt | String(014) | Sim | Número de inscrição do empregador anterior |
| AdmAnt | Date | Sim | Data de admissão do trabalhador no empregador origem |
| MatAnt | String(030) | Sim | Matrícula do trabalhador na empresa de origem |
| OnuCes | Number(001,0) | Sim | Ônus cessão |
| RemCar | String(001) | Sim | Indicar se o servidor optou pela remuneração do cargo efetivo |
| NatEst | String(001) | Sim | Natureza do Estágio |
| NivEst | Number(001,0) | Sim | Nível |
| AreAtu | String(100) | Sim | Área de atuação do estagiário |
| ApoSeg | String(030) | Sim | Número da Apólice de Seguro |
| VlrBol | Number(014,2) | Sim | Valor da bolsa, se o estágio for remunerado |
| DatTer | Date | Sim | Data prevista para o término do estágio |
| EmpEns | Number(014,0) | Sim | CNPJ da instituição de ensino |
| CfjEns | String(014) | Sim | CNPJ da instituição de ensino |
| NomEns | String(100) | Sim | Nome do contribuinte ou a razão social |
| EndEns | String(080) | Sim | Descrição do logradouro instituição de ensino |
| NumEns | String(010) | Sim | Número do logradouro |
| BaiEns | String(090) | Sim | Nome do bairro/distrito |
| CEPEns | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunEns | Number(007,0) | Sim | Código do município |
| EstEns | String(002) | Sim | Sigla da Unidade da Federação |
| EmpAge | Number(014,0) | Sim | CNPJ do agente de integração |
| CfjAge | String(014) | Sim | CNPJ do agente de integração |
| NomAge | String(100) | Sim | Nome do contribuinte (pessoa física) ou a razão social (pessoa jurídica) |
| EndAge | String(100) | Sim | Descrição do logradouro |
| NumAge | String(010) | Sim | Número do logradouro |
| BaiAge | String(060) | Sim | Nome do bairro/distrito |
| CEPAge | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunAge | Number(007,0) | Sim | Código do Município |
| EstAge | String(002) | Sim | Sigla da Unidade da Federação |
| CpfSup | Number(011,0) | Sim | CPF do responsável pela supervisão do estagiário |
| NomSup | String(070) | Sim | Nome do Supervisor do Estágio |
| RegTra | Number(001,0) | Sim | Tipo de regime trabalhista |
| RegPre | Number(002,0) | Sim | Tipo de regime previdenciário |
| CadIni | String(001) | Sim | Indica se o evento se refere a cadastramento inicial ou início de TSVE |
| DatAfa | Date | Sim | Data de início do afastamento |
| MotAfa | Number(002,0) | Sim | Motivo de afastamento temporário |
| DatDem | Date | Sim | Data de término do TSVE |
| CPFAnt | Number(011,0) | Sim | CPF do trabalhador |
| MatCPF | String(030) | Sim | Matrícula Anterior |
| DatCPF | Date | Sim | Data de Alteração do CPF |
| ObsCPF | String(255) | Sim | Observação da Alteração de CPF |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Determina se o envio é válido |
| TinLoc | Number(001,0) | Sim | Tipo de inscrição do estabelecimento |
| NinLoc | Number(014,0) | Sim | Número de inscrição do estabelecimento |
| CfjLoc | String(014) | Sim | Número de inscrição do estabelecimento |
| DesLoc | String(080) | Sim | Descrição complementar do local de trabalho |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqSvi

---

## Índices

### R350SVIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
