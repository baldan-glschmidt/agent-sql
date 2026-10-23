# R350ADA

## Descrição

S-2205 - eSocial - Alteração de Dados Cadastrais do Trabalhador

---

## Resumo

- Campos: 86
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
| SeqAda | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código que identifica a versão de leiaute utilizado para geração do arquivo |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CodCat | Number(004,0) | Sim | Código da categoria |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| DatAlt | Date | Sim | Data Alteração das Informações |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| NomTra | String(070) | Sim | Nome do trabalhador |
| SexTra | String(001) | Sim | Sexo do trabalhador |
| RacCor | Number(001,0) | Sim | Raça e Cor do trabalhador |
| EstCiv | Number(001,0) | Sim | Estado civil do trabalhador |
| GraIns | Number(002,0) | Sim | Grau de instrução do trabalhador |
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
| NumRIC | String(014) | Sim | Número do Registro de Identidade Único (RIC) |
| OrgRIC | String(020) | Sim | Órgão emissor do RIC |
| DatRIC | Date | Sim | Data da expedição do RIC |
| NumIde | String(014) | Sim | Número do RG |
| OrgIde | String(020) | Sim | Órgão emissor da identidade |
| DatIde | Date | Sim | Data da expedição do RG |
| NumRNE | String(014) | Sim | Número de inscrição no Registro Nacional de Estrangeiros |
| OrgRNE | String(020) | Sim | Órgão emissor do RNE |
| DatRNE | Date | Sim | Data da expedição do documento |
| NumOrC | String(014) | Sim | Número de Inscrição no Órgão de Classe (OC) |
| OrgOrC | String(020) | Sim | Órgão emissor do documento Órgão de Classe (OC) |
| DatOrC | Date | Sim | Data da expedição do documento Órgão de Classe (OC) |
| ValOrC | Date | Sim | Data de validade do documento Órgão de Classe (OC) |
| NumCNH | String(012) | Sim | Número da CNH |
| DatCNH | Date | Sim | Data da expedição do documento CNH |
| EstCNH | String(002) | Sim | Estsado da federação emissor CNH |
| ValCNH | Date | Sim | Data de validade do documento CNH |
| PriCNH | Date | Sim | Data da primeira habilitação |
| CatCNH | String(002) | Sim | Categoria da CNH |
| TipLog | String(004) | Sim | Tipo de Logradouro |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| BaiLog | String(090) | Sim | Nome do bairro |
| CEPLog | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunLog | Number(007,0) | Sim | Código do município do trabalhador |
| EstLog | String(002) | Sim | Sigla da Unidade da Federação |
| PaiLog | Number(003,0) | Sim | Código do país |
| CidLog | String(050) | Sim | Nome da Cidade |
| PosLog | String(012) | Sim | Código de Endereçamento Postal |
| DatChe | Date | Sim | Data de chegada do trabalhador ao Brasil |
| ClaEst | Number(002,0) | Sim | Classificação da condição do trabalhador estangeiro no Brasil |
| CasBra | String(001) | Sim | Condição de casado com brasileiro(s) |
| FilBra | String(001) | Sim | Se o trabalhador estrangeiro tem filhos com brasileiro |
| TmpRes | Number(001,0) | Sim | Tempo de residência do trabalhador imigrante |
| ConIng | Number(001,0) | Sim | Condição de ingresso do trabalhador imigrante |
| DefFis | String(001) | Sim | Indicar se o trabalhador possui deficiência física |
| DefVis | String(001) | Sim | Indicar se o trabalhador possui deficiência visual |
| DefAud | String(001) | Sim | Indicar se o trabalhador possui deficiência auditiva |
| DefMen | String(001) | Sim | Indicar se o trabalhador possui deficiência mental |
| DefInt | String(001) | Sim | Deficiência intelectual. |
| TraRea | String(001) | Sim | Informar se o trabalhador é reabilitado |
| ObsDef | String(255) | Sim | Observação Deficiência |
| TelPri | String(013) | Sim | Número de telefone do trabalhador |
| TelAlt | String(013) | Sim | Número de telefone alternativo do trabalhador |
| EmaPri | String(060) | Sim | Endereço eletrônico |
| EmaAlt | String(060) | Sim | Endereço eletrônico alternativo |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| CotDef | String(001) | Sim | Preenche cota pessoas com deficiência habilitadas ou beneficiários reabilitados |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqAda

---

## Índices

### R350ADAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
