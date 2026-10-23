# R122CEX

## Descrição

Candidatos Externos

---

## Resumo

- Campos: 180
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| NomCan | String(040) | Sim | Nome do Candidato |
| ForCon | Number(001,0) | Sim | Forma Contato |
| EstCiv | Number(001,0) | Sim | Estado Civil |
| CodNac | Number(003,0) | Sim | Nacionalidade |
| GraIns | Number(002,0) | Sim | Grau de Instrução |
| FilMen | Number(002,0) | Sim | Número de Filhos Menores |
| CatVei | Number(001,0) | Sim | Categoria do Veículo |
| SitCex | Number(002,0) | Sim | Situação Candidato |
| CodPai | Number(004,0) | Sim | Código do País |
| CodEst | String(004) | Sim | Estado |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| CodBai | Number(004,0) | Sim | Código do Bairro |
| CodRad | Number(002,0) | Sim | Código da Região Administrativa |
| NomRad | String(040) | Sim | Nome da Região Administrativa |
| DatNas | Date | Sim | Data Nascimento |
| AltCan | Number(005,2) | Sim | Altura candidato em centímetros |
| PesCan | Number(006,3) | Sim | Peso do candidato em quilos |
| AnoVei | Number(004,0) | Sim | Ano do Veículo |
| NumCnh | String(020) | Sim | Número da Carteira de Habilitação |
| CatCnh | String(004) | Sim | Categoria da Carteira de Habilitação |
| DatCnh | Date | Sim | Data da Expedição da CNH |
| VenCnh | Date | Sim | Data de Vencimento da Carteira de Habilitação |
| DatAdm | Date | Sim | Data Admissão Candidato |
| CodRfo | Number(003,0) | Sim | Fonte Recrutamento |
| CodRlc | Number(003,0) | Sim | Tipo Relação Indicação |
| EmpCon | Number(008,0) | Sim | Empresa Cônjuge |
| DatInc | Date | Sim | Data Cadastramento |
| CodRlr | Number(003,0) | Sim | Religião Candidato |
| CodQua | Number(003,0) | Sim | Qualificação |
| NumCtp | Number(009,0) | Sim | Número Carteira de Trabalho |
| SerCtp | String(005) | Sim | Série Carteira Trabalho |
| EstCtp | String(002) | Sim | Estado da Carteira de Trabalho |
| DatCtp | Date | Sim | Data Expedição Cart.Trabalho |
| CodCep | Number(008,0) | Sim | Código CEP |
| EmpInd | Number(004,0) | Sim | Empresa Indicação Interna |
| TipInd | Number(001,0) | Sim | Tipo Colaborador da Indicação Interna |
| CadInd | Number(009,0) | Sim | Cadastro Indicação Interna |
| NumCur | Number(009,0) | Sim | Número Curriculum Vitae |
| EstCon | Number(004,0) | Sim | Código da Estrutura do Cargo do Cônjuge |
| CarCon | String(024) | Sim | Cargo Cônjuge |
| NumEmp | Number(004,0) | Sim | Empresa p/Admissão |
| TipCol | Number(001,0) | Sim | Tipo Colaborador para Admissão |
| NumCad | Number(009,0) | Sim | Cadastro para Admissão do Colaborador |
| PaiNas | Number(004,0) | Sim | Código do País Nascimento |
| EstNas | String(004) | Sim | Estado Nascimento |
| CidNas | Number(007,0) | Sim | Cidade Nascimento - Naturalidade |
| CpfCan | Number(011,0) | Sim | CPF Candidato |
| PisCan | Number(011,0) | Sim | PIS/PASEP Candidato |
| OutRen | Number(011,2) | Sim | Outros Rendimentos |
| PreSal | Number(011,2) | Sim | Pretensão Salarial (mensal) |
| SisCar | Number(002,0) | Sim | Sistema Cargo |
| TipSex | String(001) | Sim | Tipo Sexo |
| TelCo1 | String(020) | Sim | Telefone Contato 1 |
| AbrTur | String(015) | Sim | Abrangência Turno |
| IdeCan | String(016) | Sim | Número da Carteira de Identidade |
| AbrHor | String(015) | Sim | Abrangência Horário |
| AbrLoc | String(1500) | Sim | Abrangência de Local |
| AbrEmp | String(025) | Sim | Abrangência de Empresa |
| EndCan | String(040) | Sim | Endereço Candidato |
| PesCon | String(030) | Sim | Pessoa Contato 1 |
| NomCjg | String(040) | Sim | Nome do Cônjuge |
| DatNjg | Date | Sim | Data Nascimento Cônjuge |
| NomPai | String(040) | Sim | Nome do Pai |
| DatNpa | Date | Sim | Data Nascimento Pai |
| NomMae | String(070) | Sim | Nome da Mãe |
| DatNma | Date | Sim | Data Nascimento Mãe |
| TelCo2 | String(020) | Sim | Telefone Contato 2 |
| ObsCan | String(1950) | Sim | Observações do Recrutador |
| EndNum | String(006) | Sim | Número |
| PesCo2 | String(030) | Sim | Pessoa Contato 2 |
| NumEle | String(013) | Sim | Número do Título de Eleitor |
| ZonEle | String(003) | Sim | Zona do Título de Eleitor |
| SecEle | String(004) | Sim | Seção do Título de Eleitor |
| NumRes | String(013) | Sim | Número do Certificado de Reservista |
| CatRes | String(005) | Sim | Categoria do Certificado de Reservista |
| EndCpl | String(025) | Sim | Complemento Endereço |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| EstCid | String(002) | Sim | Estado do Orgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| CodPrf | Number(004,0) | Sim | Conselho Profissional |
| RegCon | String(020) | Sim | Registro no Conselho Profissional |
| AnoChe | Number(004,0) | Sim | Ano Chegada |
| VisEst | Number(002,0) | Sim | Classificação da condição do estrangeiro no Brasil |
| RegEst | String(014) | Sim | Carteira de Estrangeiro |
| DvlEst | Date | Sim | Data de Validade da Carteira de Estrangeiro |
| DvlCar | Date | Sim | Data de Validade da Carteira de Trabalho (Estrangeiro) |
| EmaCan | String(100) | Sim | Endereço do Correio Eletrônico(Email) Candidato |
| DefFis | String(001) | Sim | Deficiente Habilitado ou Reabilitado |
| DcdPis | Date | Sim | Data de Cadastramento no PIS/PASEP |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do cargo que o candidato ocupará |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do organograma onde o candidato irá trabalhar |
| RacCor | Number(002,0) | Sim | Código da Raça/Etnia |
| OriCad | String(001) | Sim | Origem do Cadastro Candidato (W=Web, S=Sistema) |
| SenCan | String(040) | Sim | Senha do Candidato para WEB |
| GraInP | Number(002,0) | Sim | Grau de Instrução Pai |
| GraInM | Number(002,0) | Sim | Grau de Instrução Mãe |
| GraInC | Number(002,0) | Sim | Grau de Instrução Cônjuge |
| EstCiP | Number(001,0) | Sim | Estado Civil Pai |
| EstCiM | Number(001,0) | Sim | Estado Civil Mãe |
| EstCiC | Number(001,0) | Sim | Estado Civil Cônjuge |
| DatVal | Date | Sim | Data de Validade do Currículo |
| CodDef | Number(002,0) | Sim | Código da Deficiência |
| CplCan | String(1900) | Sim | Informações complementares do currículo |
| UltAtu | Date | Sim | Últ. Atualização do Candidato |
| DatLib | Date | Sim | Data da Liberação do Agendamento |
| HorLib | Number(005,0) | Sim | Hora da Liberação do Agendamento |
| MotLib | String(080) | Sim | Motivo da Liberação do Agendamento |
| UsuLib | Number(010,0) | Sim | Código do Usuário que Liberou o Agendamento |
| StaPng | Number(001,0) | Sim | Status do Agendamento |
| AbrFil | String(025) | Sim | Abrangência de filial |
| EmpFil | Number(004,0) | Sim | Empresa da filial onde o candidato irá trabalhar |
| CodFil | Number(006,0) | Sim | Código da filial onde o candidato irá trabalhar |
| DigCar | String(002) | Sim | Dígito da Carteira de Trabalho |
| CodHie | Number(003,0) | Sim | Hierarquia pretendida |
| CodIdn | Number(015,0) | Sim | Código de identificação do colaborador |
| NomArq | String(250) | Sim | Arquivo |
| EmpTre | Number(004,0) | Sim | Empresa do Participante |
| TipTre | Number(001,0) | Sim | Tipo do Participante (3=Parceiro) |
| CadTre | Number(009,0) | Sim | Cadastro como Participante |
| CodPes | Number(009,0) | Sim | Código da Pessoa |
| DddCo1 | Number(003,0) | Sim | Código DDD do telefone 1 |
| DdiCo1 | Number(003,0) | Sim | Código DDI do telefone 1 |
| DddCo2 | Number(003,0) | Sim | Código DDD do telefone 2 |
| DdiCo2 | Number(003,0) | Sim | Código DDI do telefone 2 |
| ObjCan | String(9000) | Sim | Objetivos de carreira e qualificações do candidato |
| VisCur | String(001) | Sim | Define a visibilidade do currículo no processo de triagem |
| NomBai | String(040) | Sim | Nome do Bairro |
| EmiEst | String(020) | Sim | Órgão emissor do registro de estrangeiro |
| DatEst | Date | Sim | Data de expedição do registro de estrangeiro |
| CasBra | String(001) | Sim | Casado com Brasileiro |
| FilCbr | String(001) | Sim | Filhos Brasileiros |
| DatNat | Date | Sim | Data de Naturalização |
| AltSen | Number(001,0) | Sim | Candidato deve alterar a senha no próximo login no Currículo Web (0-Não, 1-Sim) |
| DatChe | Date | Sim | Data de chegada ao Brasil |
| TipLgr | String(005) | Sim | Tipo de Logradouro |
| DexCon | Date | Sim | Data de Expedição do registro profissional |
| DatCon | Date | Sim | Data de vencimento do registro profissional |
| OrgCnh | String(020) | Sim | Órgão Emissor da CNH |
| EstCnh | String(002) | Sim | UF Órgão Emissor CNH |
| PriCnh | Date | Sim | Data Primeira Habilitação |
| NumRic | Number(014,0) | Sim | Registro Identidade Civil |
| EmiRic | String(020) | Sim | Orgão Emissor do RIC |
| EstRic | String(002) | Sim | Estado do Orgão Emissor  do RIC |
| DexRic | Date | Sim | Data de Expedição do RIC |
| CidRic | Number(007,0) | Sim | Cidade de Emissão do RIC |
| EstPos | Number(003,0) | Sim | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Sim | Posto de Trabalho onde o candidato irá trabalhar |
| NumPsp | String(020) | Sim | Número do Passaporte |
| EmiPsp | String(006) | Sim | Emissor do Passaporte |
| EstPsp | String(004) | Sim | Estado do Passaporte |
| DemPsp | Date | Sim | Data de Emissão do Passaporte |
| DvaPsp | Date | Sim | Data de Validade do Passaporte |
| PaiPsp | Number(004,0) | Sim | País de emissão do Passaporte |
| NomSoc | String(070) | Sim | Nome Social do Candidato |
| PodVis | Number(001,0) | Sim | Candidato pode ser visualizado conforme aceite dos termos de uso |
| CamAux1 | String(001) | Sim | Campo Auxiliar 1 |
| NomCom | String(080) | Sim | Nome Completo |
| UsaRFa | String(001) | Sim | Utiliza Reconhecimento Facial |
| NumPor | String(016) | Sim | Número da Portaria de Naturalização |
| TmpRes | Number(001,0) | Sim | Tempo de residência do trabalhador imigrante |
| DatTer | Date | Sim | Data de término da residência do trabalhador |
| BenRea | String(001) | Sim | Candidato reabilitado da deficiência (S/N) |
| USU_TemPar | String(001) | Sim | Tem parentes na Baldan? |
| USU_TraBal | String(001) | Sim | Já Trabalhou na Baldan? |
| USU_GraPar | Number(002,0) | Sim | Grau de Parentesco |
| USU_NomPar | String(050) | Sim | Nome do Parente |
| USU_NomSet | String(030) | Sim | Qual Setor Trabalhou? |
| USU_QueInd | String(030) | Sim | Quem fez a indicação? |
| USU_CodPrf | Number(004,0) | Sim | Conselho Profissional |
| USU_RegCon | String(020) | Sim | Registro no Conselho Profissional |
| USU_UtiApa | String(001) | Sim | Utiliza Aparelho? |
| USU_DesApa | String(030) | Sim | Descrição do Aparelho |
| USU_TemExp | String(001) | Sim | Tem Experiência? |
| USU_TemApo | String(001) | Sim | É Aposentado? |
| USU_PriEmp | String(001) | Sim | Primeiro Emprego |
| USU_IdaCan | Number(003,0) | Sim | Idade do Candidato |
| USU_PosHab | String(001) | Sim | Possui Habilitação |

---

## Chave Primária

- NumCan

---

## Índices

### R122CEXIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

### R122CEXIndice3

**Tipo:** Não unico

Campos:
- CpfCan

---

## Relacionamentos

Nenhum relacionamento cadastrado.
