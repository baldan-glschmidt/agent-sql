# R033PES

## Descrição

Pessoas - Cadastro de Pessoas

---

## Resumo

- Campos: 97
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| NomPes | String(040) | Sim | Nome da Pessoa |
| ApePes | String(050) | Sim | Apelido da Pessoa |
| TipSex | String(001) | Sim | Sexo da Pessoa |
| EstCiv | Number(001,0) | Sim | Estado Civil |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| DatNas | Date | Sim | Data de Nascimento |
| CciNas | Number(007,0) | Sim | Cidade de Nascimento |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| GraIns | Number(002,0) | Sim | Grau de Instrução |
| DefFis | String(001) | Sim | Deficiente Habilitado ou Reabilitado |
| CodDef | Number(002,0) | Sim | Código da Deficiência |
| BenRea | String(001) | Sim | Beneficiário reabilitado(S/N) |
| RacCor | Number(002,0) | Sim | Código da Raça/Etnia |
| SitReg | String(001) | Sim | Situação do registro no conselho profissional |
| NomCom | String(080) | Sim | Nome Completo |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| DcdPis | Date | Sim | Data de Cadastramento no PIS/PASEP |
| NumCid | String(016) | Sim | Número da Carteira de Identidade |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| EstCid | String(002) | Sim | Estado do Orgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| CidEmi | Number(007,0) | Sim | Cidade de Emissão do Documento |
| NumCtp | Number(009,0) | Sim | Número da Carteira de Trabalho |
| SerCtp | String(005) | Sim | Série da Carteira de Trabalho |
| DigCar | String(002) | Sim | Dígito da Carteira de Trabalho |
| DexCtp | Date | Sim | Data de Expedição da Carteira de Trabalho |
| EstCtp | String(002) | Sim | UF da Carteira de Trabalho |
| NumEle | String(013) | Sim | Número do Título de Eleitor |
| ZonEle | String(003) | Sim | Zona do Título de Eleitor |
| SecEle | String(004) | Sim | Seção do Título de Eleitor |
| NumCnh | String(020) | Sim | Número da Carteira de Habilitação |
| CatCnh | String(004) | Sim | Categoria da Carteira de Habilitação |
| DatCnh | Date | Sim | Data da Expedição da CNH |
| VenCnh | Date | Sim | Data de Vencimento da Carteira de Habilitação |
| NumRes | String(013) | Sim | Número do Certificado de Reservista |
| CatRes | String(005) | Sim | Categoria do Certificado de Reservista |
| EmaCom | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) Comercial |
| EmaPar | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) Particular |
| NumTel | String(020) | Sim | Número do Telefone |
| NumRam | String(015) | Sim | Número do Ramal |
| NumCel | String(020) | Sim | Número do Celular |
| TelCom | String(020) | Sim | Número do Telefone Comercial |
| DatAlt | Date | Sim | Data da última alteração |
| HorAlt | Number(005,0) | Sim | Hora da última alteração |
| CodUsu | Number(010,0) | Sim | Código do Usuário que efetuou o cadastramento |
| DddCel | Number(003,0) | Sim | Código DDD do celular |
| DdiCel | Number(003,0) | Sim | Código DDI do celular |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| DddCom | Number(003,0) | Sim | Código DDD do telefone comercial |
| DdiCom | Number(003,0) | Sim | Código DDI do telefone comercial |
| InsCur | Number(002,0) | Sim | Tipo de Instrutor de Curso |
| NasViv | String(020) | Sim | Declaração de Nascido Vivo |
| CarSus | String(016) | Sim | Cartão Nacional Saúde |
| NumRic | Number(014,0) | Sim | Registro Identidade Civil |
| TipCer | String(001) | Sim | Tipo de Certidão Civil |
| DemCiv | Date | Sim | Data de Emissão da Certidão Civil |
| MatCiv | String(015) | Sim | Termo de Certidão Civil |
| LivCiv | String(006) | Sim | Livro da Certidão Civil |
| FolCiv | String(006) | Sim | Folha da Certidão Civil |
| CarCiv | String(020) | Sim | Cartório de Registro da Certidão Civil |
| EstCer | String(002) | Sim | Estado da Certidão Civil |
| CidCiv | Number(007,0) | Sim | Cidade da Certidão Civil |
| NumPsp | String(020) | Sim | Número do Passaporte |
| EmiPsp | String(006) | Sim | Emissor do Passaporte |
| EstPsp | String(004) | Sim | Estado do Passaporte |
| DemPsp | Date | Sim | Data de Emissão do Passaporte |
| DvaPsp | Date | Sim | Data de Validade do Passaporte |
| PaiPsp | Number(004,0) | Sim | País de Emissão do Passaporte |
| NumPor | String(016) | Sim | Número da Portaria de Naturalização |
| DatPor | Date | Sim | Data de Naturalização |
| EstRic | String(002) | Sim | Estado do Orgão Emissor do RIC |
| EmiRic | String(020) | Sim | Orgão Emissor do RIC |
| CidRic | Number(007,0) | Sim | Cidade de Emissão do RIC |
| DexRic | Date | Sim | Data de Expedição do RIC |
| MatCCv | String(032) | Sim | Matrícula Certidão Civil |
| RegCon | String(020) | Sim | Registro no Conselho Profissional |
| CodPrf | Number(004,0) | Sim | Conselho Profissional |
| DexCon | Date | Sim | Data de Expedição do registro profissional |
| DatCon | Date | Sim | Data de vencimento do registro profissional |
| OrgCnh | String(020) | Sim | Órgão Emissor da CNH |
| EstCnh | String(002) | Sim | UF Órgão Emissor CNH |
| PriCnh | Date | Sim | Data da Primeira Habilitação |
| EmpAux | Number(004,0) | Sim | USO EXCLUSIVO SENIOR |
| TipAux | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CadAux | Number(009,0) | Sim | USO EXCLUSIVO SENIOR |
| DepAux | Number(002,0) | Sim | USO EXCLUSIVO SENIOR |
| ColAti | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CanAux | Number(007,0) | Sim | USO EXCLUSIVO SENIOR |
| DatAux | Date | Sim | USO EXCLUSIVO SENIOR |
| FunPro | String(020) | Sim | Número do fundo de provisão |
| NumSeg | String(025) | Sim | Número do seguro social |
| DocIde | String(020) | Sim | Documento de identificação |
| NomSoc | String(070) | Sim | Nome Social da Pessoa |
| ForPro | String(255) | Sim | Formação do profissional responsável pelo treinamento/capacitação |
| CodCbo | String(006) | Sim | CBO referente à formação do profissional responsável p/ treinamento/capacitação |

---

## Chave Primária

- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
