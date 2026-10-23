# R034CPL

## Descrição

Ficha Complementar

---

## Resumo

- Campos: 115
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| FicReg | Number(009,0) | Sim | Número da Ficha Registro |
| CodPai | Number(004,0) | Sim | Código do País |
| CodEst | String(004) | Sim | Estado |
| CodCid | Number(007,0) | Sim | Cidade |
| CodBai | Number(004,0) | Sim | Bairro |
| CodRad | Number(002,0) | Sim | Código da Região Administrativa |
| NomRad | String(040) | Sim | Nome da Região Administrativa |
| EndCep | Number(008,0) | Sim | CEP |
| TipLgr | String(005) | Sim | Tipo de Logradouro |
| EndRua | String(100) | Sim | Endereço Residencial |
| EndNum | String(006) | Sim | Número |
| EndCpl | String(025) | Sim | Complemento Endereço |
| NumTel | String(020) | Sim | Número do Telefone |
| PaiNas | Number(004,0) | Sim | Código do País Nascimento |
| EstNas | String(004) | Sim | Estado Nascimento |
| CciNas | Number(007,0) | Sim | Cidade de Nascimento |
| DocIdn | Number(002,0) | Sim | Tipo de Documento de Identificação |
| NumCid | String(016) | Sim | Número da Carteira de Identidade |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| CidEmi | Number(007,0) | Sim | Cidade de Emissão do Documento |
| EstCid | String(002) | Sim | Estado do Orgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| ZonEle | String(003) | Sim | Zona do Título de Eleitor |
| SecEle | String(004) | Sim | Seção do Título de Eleitor |
| NumEle | String(013) | Sim | Número do Título de Eleitor |
| NumCnh | String(020) | Sim | Número da Carteira de Habilitação |
| CatCnh | String(004) | Sim | Categoria da Carteira de Habilitação |
| DatCnh | Date | Sim | Data da Expedição da CNH |
| VenCnh | Date | Sim | Data de Validade da Carteira de Habilitação |
| NumRes | String(013) | Sim | Número do Certificado de Reservista |
| CatRes | String(005) | Sim | Categoria do Certificado de Reservista |
| CodPrf | Number(004,0) | Sim | Conselho Profissional |
| RegCon | String(020) | Sim | Registro no Conselho Profissional |
| DurCon | Number(004,0) | Sim | Duração do Contrato de Trabalho |
| ProCon | Number(004,0) | Sim | Prorrogação do Contrato de Trabalho |
| ProExm | Date | Sim | Data do Próximo Exame Médico |
| UltExm | Date | Sim | Data do Último Exame Médico |
| CodQua | Number(003,0) | Sim | Código de Qualificação |
| EstPad | Number(004,0) | Sim | Estrutura Salarial Padrão |
| ClaSal | String(005) | Sim | Classe Salarial Padrão |
| NivSal | String(005) | Sim | Nível da Classe Salarial Padrão |
| MatIpe | Number(008,0) | Sim | Número de Matrícula no IPE |
| AltIpe | Date | Sim | Data de Alteração no IPE |
| SitIpe | Number(002,0) | Sim | Situação no IPE |
| TipPsa | String(015) | Sim | Tipo do Plano de Saúde |
| CodPsa | String(020) | Sim | Código do Plano de Saúde |
| MatPsa | Number(015,0) | Sim | Número da Matrícula no Plano Saúde |
| IncPsa | Date | Sim | Data de Inclusão no Plano de Saúde |
| ExcPsa | Date | Sim | Data de Exclusão no Plano de Saúde |
| CodRlr | Number(003,0) | Sim | Código da Religião |
| CodCas | Number(003,0) | Sim | Determina a qual casta o colaborador pertence |
| NumRam | String(015) | Sim | Número do Ramal |
| PreTrb | String(050) | Sim | Nome do Prédio Onde o Colaborador Trabalha |
| AndTrb | String(005) | Sim | Andar do Prédio Onde o Colaborador Trabalha |
| NroArm | String(005) | Sim | Número do Armário |
| IniArm | Date | Sim | Início da Utilização do Armário |
| FimArm | Date | Sim | Fim da Utilização do Armário |
| EmaPar | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) Particular |
| EmaCom | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) Comercial |
| CatVei | Number(001,0) | Sim | Categoria do Veículo |
| SitReg | String(001) | Sim | Situação do registro no conselho profissional |
| NomCom | String(080) | Sim | Nome Completo |
| DatVen | Date | Sim | Data de vencimento do registro profissional |
| DddTel | Number(003,0) | Sim | Código DDD do Telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do Telefone |
| NmDdi2 | Number(003,0) | Sim | Código DDI do Telefone 2 |
| NmDdd2 | Number(003,0) | Sim | Código DDD do Telefone 2 |
| NmTel2 | String(020) | Sim | Número do Telefone 2 |
| NmRam2 | String(015) | Sim | Número do Ramal 2 |
| NifExt | String(030) | Sim | Número de Identificação Fiscal no Exterior |
| SenCan | String(040) | Sim | Senha do Candidato para WEB |
| MaSPsa | String(020) | Sim | Número da Matrícula no Plano Saúde |
| NasViv | String(020) | Sim | Declaração de Nascido Vivo |
| CarSus | String(016) | Sim | Cartão Nacional Saúde |
| TipCer | String(001) | Sim | Tipo da Certidão Civil |
| DemCiv | Date | Sim | Data de Emissão da Certidão Civil |
| MatCCv | String(032) | Sim | Matrícula Certidão Civil |
| MatCiv | String(015) | Sim | Termo/Matrícula da Certidão Civil |
| LivCiv | String(006) | Sim | Livro da Certidão Civil |
| FolCiv | String(006) | Sim | Folha da Certidão Civil |
| CarCiv | String(020) | Sim | Cartório de Registro da Certidão Civil |
| EstCiv | String(002) | Sim | Estado da Certidão Civil |
| CidCiv | Number(007,0) | Sim | Cidade da Certidão Civil |
| NumPsp | String(020) | Sim | Número do Passaporte |
| EmiPsp | String(006) | Sim | Emissor do Passaporte |
| EstPsp | String(004) | Sim | Estado do Passaporte |
| DemPsp | Date | Sim | Data de Emissão do Passaporte |
| DvaPsp | Date | Sim | Data de Validade do Passaporte |
| PaiPsp | Number(004,0) | Sim | País de emissão do Passaporte |
| NumPor | String(016) | Sim | Número da Portaria de Naturalização |
| DatPor | Date | Sim | Data de Naturalização |
| NumRic | Number(014,0) | Sim | Registro Identidade Civil |
| EstRic | String(002) | Sim | Estado do Orgão Emissor  do RIC |
| EmiRic | String(020) | Sim | Orgão Emissor do RIC |
| CidRic | Number(007,0) | Sim | Cidade de Emissão do RIC |
| DexRic | Date | Sim | Data de Expedição do RIC |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| DatExp | Date | Sim | Data de Expedição do registro profissional |
| OrgCnh | String(020) | Sim | Órgão Emissor da CNH |
| AltSen | Number(001,0) | Sim | Candidato deve alterar a senha no próximo login no Currículo Web (0-Não, 1-Sim) |
| EstCnh | String(002) | Sim | UF Órgão Emissor CNH |
| PriCnh | Date | Sim | Data Primeira Habilitação |
| TerCon | Date | Sim | Data Término Contrato |
| RegMte | String(030) | Sim | Número do Registro Profissional no MTE |
| NomSoc | String(070) | Sim | Nome Social do Colaborador |
| ClaAss | String(001) | Sim | Indicativo se o contrato contém cláusula assecuratória |
| ObjDet | String(255) | Sim | Objetivo do término de contrato por prazo determinado |
| USU_MatPod | Number(014,0) | Sim | Numero da Matricula no Plano Odontologico |
| USU_IncPod | Date | Sim | Data da Inclus?o no Plano Odontologico |
| USU_ExcPod | Date | Sim | Data da Exclus?o no Plano Odontologico |
| USU_CodCcu | String(009) | Sim | Centro Custo |
| USU_TitCar | String(030) | Sim | Titulo do Cargo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

### R034CPLIndice2

**Tipo:** Não unico

Campos:
- NumCid

### R034CPLIndice3

**Tipo:** Não unico

Campos:
- CodCid

---

## Relacionamentos

### IR_R034CPL_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

