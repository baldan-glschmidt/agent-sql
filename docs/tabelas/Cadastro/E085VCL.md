# E085VCL

## Descrição

Cadastros - Clientes - Histórico de Alteração Fiscal do Cliente

---

## Resumo

- Campos: 73
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| DatAtu | Date | Não | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Não | Hora/minuto da última atualização do cadastro |
| SeqAtu | Number(003,0) | Não | Sequência da atualização |
| NomCli | String(100) | Não | Nome do cliente |
| ApeCli | String(050) | Sim | Nome fantasia do cliente - descontinuado |
| TipCli | String(001) | Não | Tipo do cliente |
| TipMer | String(001) | Não | Tipo de mercado do cliente |
| TipEmc | Number(001,0) | Sim | Tipo Empresa do cliente para geração de título de COFINS |
| CliCon | String(001) | Não | Indicativo se o cliente é contribuinte |
| CodRam | String(005) | Sim | Código do ramo de atividade |
| InsEst | String(025) | Sim | Inscrição estadual do cliente |
| InsMun | String(016) | Sim | Inscrição municipal do cliente |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do cliente |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do cliente |
| CodGre | Number(009,0) | Sim | Código do grupo de empresas |
| ZonFra | Number(001,0) | Sim | Indicativo de qual é o benefício fiscal do cliente |
| CodSuf | String(010) | Sim | Número do cliente junto à Suframa |
| EndCli | String(100) | Sim | Endereço do cliente |
| CplEnd | String(200) | Sim | Complemento do endereço do cliente (sala, andar, etc.) |
| CepCli | Number(008,0) | Sim | CEP do cliente |
| BaiCli | String(075) | Sim | Bairro do cliente |
| CidCli | String(060) | Sim | Cidade do cliente |
| SigUfs | String(002) | Sim | Sigla do estado do cliente |
| CodPai | String(004) | Sim | Código do país do cliente |
| EndEnt | String(100) | Sim | Endereço de entrega do cliente |
| CplEnt | String(200) | Sim | Complemento do endereço de entrega do cliente |
| CepEnt | Number(008,0) | Sim | CEP do endereço de entrega do cliente |
| CidEnt | String(060) | Sim | Cidade do endereço de entrega do cliente |
| EstEnt | String(002) | Sim | Estado do endereço de entrega do cliente |
| InsEnt | String(025) | Sim | Inscrição estadual do endereço de entrega |
| EndCob | String(100) | Sim | Endereço de cobrança do cliente |
| CplCob | String(200) | Sim | Complemento do endereço de cobrança do cliente |
| CepCob | Number(008,0) | Sim | CEP do endereço de cobrança do cliente |
| CidCob | String(060) | Sim | Cidade do endereço de cobrança do cliente |
| EstCob | String(002) | Sim | Estado do endereço de cobrança do cliente |
| CgcCob | Number(014,0) | Sim | Número do CNPJ de cobrança |
| DocIdeCob | String(014) | Sim | Número do CNPJ de cobrança |
| CodFor | Number(009,0) | Sim | Código do cliente como fornecedor |
| CliRep | Number(009,0) | Sim | Código do cliente como representante |
| CliTra | Number(009,0) | Sim | Código do cliente como transportadora |
| DatVct | Date | Sim | Data do vencimento do cadastro do cliente |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| SitCli | String(001) | Não | Situação do cliente |
| BloCre | String(001) | Sim | Indicativo se o motivo bloqueia crédito para o cliente (Faturamento) |
| TriIcm | String(001) | Sim | Indicativo se o cliente tem tributação de ICMS ou não |
| TriIpi | String(001) | Sim | Indicativo se o cliente tem tributação de IPI ou não |
| BaiEnt | String(075) | Sim | Bairro de entrega do cliente |
| BaiCob | String(075) | Sim | Bairro de cobrança do cliente |
| DatGer | Date | Sim | Data de geração |
| TriPis | String(001) | Sim | Indicativo se o cliente tem tributação de PIS ou não |
| TriCof | String(001) | Sim | Indicativo se o cliente tem tributação de COFINS ou não |
| RetCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de Cofins |
| RetCsl | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de CSLL |
| RetPis | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de PIS |
| RetOur | String(001) | Sim | Indicativo se as notas fiscais poderão ter Outras Retenções |
| DatSuf | Date | Sim | Data de validade do registro do SUFRAMA |
| RetPro | String(001) | Sim | Indicativo se o cliente controla retenções de PIS, Cofins, CSLL, IRRF, e Outras Retenções por produto |
| RetIrf | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de IRRF |
| LimRet | String(001) | Sim | Indicativo de como é utilizado o valor limite para cálculos de retenção para o cliente nas notas fiscais de saída |
| CalFun | String(001) | Sim | Indicativo se calcula Funrural nas notas fiscais de saídas. |
| DatFis | Date | Sim | Data da última atualização da data fiscal |
| DatFat | Date | Sim | Data da última alteração da data fiscal |
| HorFat | Number(005,0) | Sim | Hora da última alteração da data fiscal |
| UsuFat | Number(010,0) | Sim | Usuário da última alteração da data fiscal |
| IndCoo | String(001) | Sim | Indicativo se cliente/fornecedor é cooperado. |
| NatRet | Number(002,0) | Sim | Indicador de natureza da retenção na fonte de PIS e Cofins |
| NatPis | Number(005,0) | Sim | Natureza da receita do PIS |
| NatCof | Number(005,0) | Sim | Natureza da receita do COFINS |
| DatSpc | Date | Sim | Data da última consulta do SPC |
| CidSpc | String(060) | Sim | Cidades de pesquisa e de Intercâmbio do SPC |
| InfSpc | Number(001,0) | Sim | Informação levantada junto ao SPC |
| UsuSpc | Number(010,0) | Sim | Usuário da última alteração das informações do SPC |

---

## Chave Primária

- CodCli
- DatAtu
- HorAtu
- SeqAtu

---

## Índices

### E085VCLIndice1

**Tipo:** Não unico

Campos:
- CgcCpf
- InsEst
- DatAtu
- HorAtu
- SeqAtu

### E085VCLIndice2

**Tipo:** Não unico

Campos:
- DocIde
- InsEst
- DatAtu
- HorAtu
- SeqAtu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
