# E085FIS

## Descrição

Cadastros - Clientes - Dados Pessoa Física

---

## Resumo

- Campos: 114
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| EstCiv | Number(001,0) | Sim | Estado civil do cliente |
| RegCas | Number(001,0) | Sim | Regime de casamento |
| CodSex | String(003) | Sim | Código do sexo |
| DatNas | Date | Sim | Data do nascimento do cliente |
| CidNat | String(060) | Sim | Nome da cidade de naturalidade |
| CodPai | String(004) | Sim | Nome do país de nacionalidade do cliente |
| NroDep | Number(002,0) | Sim | Quantidade de dependentes |
| NumRge | String(013) | Sim | Número do RG (Identidade) |
| OrgRge | String(006) | Sim | Órgão emissor do RG |
| DatRge | Date | Sim | Data de emissão do RG |
| NumPte | String(015) | Sim | Número do passaporte |
| DatEpt | Date | Sim | Data de emissão do passaporte |
| DatVpt | Date | Sim | Data de vencimento do passaporte |
| NomPai | String(030) | Sim | Nome do pai do cliente |
| NomMae | String(030) | Sim | Nome da mãe do cliente |
| EmpTra | String(030) | Sim | Nome da empresa onde trabalha |
| TipOcu | Number(002,0) | Sim | Tipo de ocupação |
| TipTra | Number(001,0) | Sim | Tipo da empresa onde trabalha o cliente |
| AdmTra | Date | Sim | Data de admissão do cliente/sócio |
| EndTra | String(040) | Sim | Endereço da empresa onde trabalha o cliente |
| BaiTra | String(075) | Sim | Bairro da empresa onde trabalha o cliente |
| CepTra | Number(008,0) | Sim | CEP da empresa onde trabalha o cliente |
| CidTra | String(060) | Sim | Cidade da empresa onde trabalha o cliente |
| EstTra | String(002) | Sim | Estado da empresa onde trabalha o cliente |
| FonTra | String(020) | Sim | Número do telefone da empresa onde trabalha o cliente |
| RamTra | Number(004,0) | Sim | Ramal do telefone onde trabalha o cliente |
| CrtTra | String(020) | Sim | Dados da carteira profissional do cliente |
| CarTra | String(020) | Sim | Cargo exercido na empresa pelo cliente |
| SalTra | Number(015,2) | Sim | Salário do cliente na empresa onde trabalha |
| OriOut | String(020) | Sim | Origem de outros rendimentos do cliente |
| VlrOut | Number(015,2) | Sim | Valor de outros rendimentos do cliente |
| NomCng | String(100) | Sim | Nome do cônjuge |
| NasCng | Date | Sim | Data de nascimento do cônjuge |
| CpfCng | Number(012,0) | Sim | Número do CPF do cônjuge |
| RgeCng | String(012) | Sim | Número do RG do cônjuge |
| OrgCng | String(006) | Sim | Órgão emissor do RG do cônjuge |
| DatCng | Date | Sim | Data de emissão do RG do cônjuge |
| EmpCng | String(030) | Sim | Empresa onde trabalha o cônjuge |
| AdmCng | Date | Sim | Data de admissão do cônjuge |
| EndCng | String(040) | Sim | Endereço da empresa onde trabalha o cônjuge do cliente |
| BaiCng | String(075) | Sim | Bairro onde trabalha o cônjuge do cliente |
| CepCng | Number(008,0) | Sim | CEP onde trabalha o cônjuge do cliente |
| CidCng | String(060) | Sim | Cidade onde trabalha o cônjuge do cliente |
| EstCng | String(002) | Sim | Estado onde trabalha o cônjuge do cliente |
| FonCng | String(020) | Sim | Número do telefone da empresa onde trabalha o cônjuge |
| RamCng | Number(004,0) | Sim | Ramal do fone onde trabalha o cônjuge do cliente |
| CrtCng | String(020) | Sim | Dados da carteira profissional do cônjuge |
| CarCng | String(020) | Sim | Cargo exercido na empresa pelo cônjuge |
| SalCng | Number(015,2) | Sim | Salário do cônjuge na empresa onde trabalha |
| TipMor | Number(001,0) | Sim | Tipo de moradia do cliente |
| TpoMor | Date | Sim | Mês e ano da mudança para a moradia atual (reside desde) |
| VlrAlu | Number(015,2) | Sim | Valor das despesas com moradia |
| RefCm1 | String(060) | Sim | Referência comercial - 1 |
| RefCm2 | String(060) | Sim | Referência comercial - 2 |
| RefPe1 | String(060) | Sim | Referência pessoal - 1 |
| RefPe2 | String(060) | Sim | Referência pessoal - 2 |
| RefBc1 | String(060) | Sim | Referência bancária - 1 |
| RefBc2 | String(060) | Sim | Referência bancária - 2 |
| UltCpr | String(040) | Sim | Nome da loja onde efetuou a última compra a crédito |
| UltFin | String(040) | Sim | Nome do banco ou financeira onde já fez empréstimo |
| DatSpc | Date | Sim | Data da última consulta do SPC |
| CidSpc | String(060) | Sim | Cidades de pesquisa e de Intercâmbio do SPC |
| InfSpc | Number(001,0) | Sim | Informação levantada junto ao SPC |
| NomInv | String(040) | Sim | Nome invertido do cliente |
| CarCre | String(020) | Sim | Nome do cartão de crédito que possui |
| NumCre | String(020) | Sim | Número do cartão de crédito |
| ValCre | Date | Sim | Data de validade do cartão de crédito |
| VctCre | Number(002,0) | Sim | Dia do vencimento do cartão de crédito |
| NomCre | String(030) | Sim | Nome do cliente no cartão de crédito |
| DepCre | String(030) | Sim | Nome do dependente no cartão de crédito |
| NasCre | Date | Sim | Data de Nascimento do dependente do cartão de crédito |
| GraCre | Number(001,0) | Sim | Grau de parentesco do dependente do cartão de crédito |
| EmpAnt | String(040) | Sim | Nome da empresa anterior onde o cliente trabalhou |
| TemAnt | Number(004,0) | Sim | Tempo de trabalho na empresa anterior (em anos) |
| FonAnt | String(020) | Sim | Número do telefone da empresa anterior |
| RamAnt | Number(005,0) | Sim | Número do ramal do telefone da empresa anterior |
| ResAnt | String(060) | Sim | Residência anterior do cliente |
| NomAva | String(030) | Sim | Nome do avalista do cliente |
| CpfAva | Number(012,0) | Sim | Número do CPF do avalista do cliente |
| EndAva | String(060) | Sim | Endereço do avalista do cliente |
| CepAva | Number(008,0) | Sim | CEP do avalista do cliente |
| CidAva | String(060) | Sim | Nome da cidade do avalista do cliente |
| EstAva | String(002) | Sim | Estado do avalista do cliente |
| FonAva | String(020) | Sim | Número de Telefone |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| EenTra | String(018) | Sim | Código do endereço da empresa onde trabalha o cliente |
| EenCng | String(018) | Sim | Código do endereço onde trabalha o cônjuge do cliente |
| EenAva | String(018) | Sim | Código do endereço do avalista do cliente |
| EstNat | String(002) | Sim | Estado de nascimento do cliente |
| NenTra | String(060) | Sim | Número Endereço de Trabalho do Cliente |
| CplTra | String(200) | Sim | Complemento do endereço de trabalho do cliente (sala, andar, etc.) |
| EsnCng | String(002) | Sim | Estado de nascimento do cônjuge |
| CdnCng | String(060) | Sim | Nome da cidade de naturalidade do cônjuge |
| NenCng | String(060) | Sim | Número Endereço de Trabalho do Cônjuge |
| CplCng | String(200) | Sim | Complemento do endereço do cônjuge (sala, andar, etc.) |
| FonPe1 | String(020) | Sim | Número do telefone da referencia pessoal 1 |
| FonPe2 | String(020) | Sim | Número do telefone da referencia pessoal 2 |
| FonCm1 | String(020) | Sim | Número do telefone da referencia comercial 1 |
| FonCm2 | String(020) | Sim | Número do telefone da referencia comercial 2 |
| FonBc1 | String(020) | Sim | Número do telefone da referencia bancária 1 |
| FonBc2 | String(020) | Sim | Número do telefone da referencia bancária 2 |
| NenAva | String(060) | Sim | Número Endereço de Trabalho do Avalista |
| BaiAva | String(075) | Sim | Bairro onde mora o avalista |
| PosAut | String(001) | Sim | Indicativo se o cliente possui automóvel |
| QtcPos | Number(004,0) | Sim | Quantidade de Consultas de Crédito Positivas |
| QtcNeg | Number(004,0) | Sim | Quantidade de Consultas de Crédito Negativas |
| CibNat | Number(007,0) | Sim | Código da cidade de naturalidade da pessoa |
| CibCng | Number(007,0) | Sim | Código da cidade de naturalidade do conjuge |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| PaiCng | String(030) | Sim | Nome do pai do cônjuge |
| MaeCng | String(030) | Sim | Nome da mãe do cônjuge |

---

## Chave Primária

- CodCli

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085FIS_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

