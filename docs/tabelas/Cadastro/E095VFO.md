# E095VFO

## Descrição

Cadastros - Fornecedores - Histórico de Alteração Fiscal do Fornecedor

---

## Resumo

- Campos: 60
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do fornecedor |
| DatAtu | Date | Não | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Não | Hora/minuto da última atualização do cadastro |
| SeqAtu | Number(003,0) | Não | Sequência da atualização |
| NomFor | String(100) | Não | Nome do fornecedor |
| ApeFor | String(050) | Sim | Nome fantasia do fornecedor - descontinuado |
| TipFor | String(001) | Não | Tipo de Fornecedor |
| TipMer | String(001) | Não | Tipo de Mercado do fornecedor |
| CodRam | String(005) | Sim | Código do ramo de atividade |
| InsEst | String(025) | Sim | Inscrição estadual do fornecedor |
| InsMun | String(016) | Sim | Inscrição municipal do fornecedor |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| CodGre | Number(009,0) | Sim | Código do grupo de empresas |
| CodSuf | String(010) | Sim | Código na suframa |
| EndFor | String(100) | Sim | Endereço do fornecedor |
| CplEnd | String(200) | Sim | Complemento do endereço do fornecedor (sala, andar, etc.) |
| BaiFor | String(075) | Sim | Bairro do fornecedor |
| CepFor | Number(008,0) | Sim | CEP do fornecedor |
| CidFor | String(060) | Sim | Cidade do fornecedor |
| SigUfs | String(002) | Sim | Estado do fornecedor |
| CodCli | Number(009,0) | Sim | Código do fornecedor como cliente |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| SitFor | String(001) | Não | Situação do fornecedor |
| CodPai | String(004) | Sim | Código do país do fornecedor |
| ForRep | Number(009,0) | Sim | Código do fornecedor como representante |
| ForTra | Number(009,0) | Sim | Código do fornecedor como transportadora |
| DatGer | Date | Sim | Data de geração |
| CodTri | String(005) | Sim | Código de tributação para emissão de DARF/DIRF |
| GerDir | String(001) | Sim | Indicativo se devem ser exportados os dados do fornecedor para DIRF |
| QtdDep | Number(004,0) | Sim | Quantidade de dependentes do Fornecedor |
| RecPis | String(001) | Sim | Indicativo se as notas fiscais do fornecedor poderão ter recuperação de PIS |
| PerPid | Number(008,4) | Sim | Percentual de recuperação de PIS diferenciado para o fornecedor |
| TriIss | String(001) | Sim | Indicativo se o fornecedor tributa ISS |
| RecCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de Cofins |
| PerCod | Number(008,4) | Sim | Percentual de recuperação de Cofins diferenciado |
| RetCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de Cofins |
| RetCsl | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de CSLL |
| RetPis | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de PIS |
| RetOur | String(001) | Sim | Indicativo se as notas fiscais poderão ter Outras Retenções |
| RecIpi | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de IPI |
| RecIcm | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de ICMS |
| TriIcm | String(001) | Sim | Indicativo se o fornecedor tem tributação de ICMS ou não |
| TriIpi | String(001) | Sim | Indicativo se o fornecedor tem tributação de IPI ou não |
| RetPro | String(001) | Sim | Indicativo se o fornecedor controla retenções de PIS, Cofins, CSLL, IRRF, e Outras Retenções por produto |
| RetIrf | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de IRRF |
| IndFor | String(001) | Sim | Indicativo do tipo do fornecedor |
| LimRet | String(001) | Sim | Indicativo de como é utilizado o valor limite para cálculos de retenção para o fornecedor nas notas fiscais de entrada |
| NumRge | String(013) | Sim | Número do documento de identidade (RG) do fornecedor |
| DatFis | Date | Sim | Data da última atualização da data fiscal |
| DatFat | Date | Sim | Data da última alteração da data fiscal |
| UsuFat | Number(010,0) | Sim | Usuário da última alteração da data fiscal |
| HorFat | Number(005,0) | Sim | Hora da última alteração da data fiscal |
| IndCoo | String(001) | Sim | Indicativo se cliente/fornecedor é cooperado. |
| NumNis | String(011) | Sim | Número de Inscrição do Segurado - NIS, NIT e PIS/PASEP |
| OrgEmi | String(020) | Sim | Órgão Emissor do RG |
| DatExd | Date | Sim | Data de Expedição do RG |
| DatNas | Date | Sim | Data de Nascimento do Fornecedor |
| NumCbo | Number(006,0) | Sim | Classificação Brasileira de Ocupação - CBO |
| CatFor | Number(003,0) | Sim | Categoria Recibo de Pagamento Autônomo |

---

## Chave Primária

- CodFor
- DatAtu
- HorAtu
- SeqAtu

---

## Índices

### E095VFOIndice1

**Tipo:** Não unico

Campos:
- CgcCpf
- InsEst
- DatAtu
- HorAtu
- SeqAtu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
