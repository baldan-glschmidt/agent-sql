# E090VRE

## Descrição

Cadastros - Representantes - Histórico de Alteração Fiscal do Representante

---

## Resumo

- Campos: 34
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRep | Number(009,0) | Não | Código do representante |
| DatAtu | Date | Não | Data da última alteração do representante |
| HorAtu | Number(005,0) | Não | Hora/minuto da última atualização do cadastro |
| SeqAtu | Number(003,0) | Não | Sequência da atualização |
| NomRep | String(100) | Não | Nome do representante |
| ApeRep | String(050) | Sim | Nome fantasia do representante - descontinuado |
| TipRep | String(001) | Não | Tipo do representante |
| InsEst | String(025) | Sim | Inscrição estadual do representante |
| InsMun | String(016) | Sim | Número da Inscrição Municipal |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do representante |
| DocIdeRep | String(014) | Sim | Número do CNPJ ou CPF do representante |
| EndRep | String(100) | Não | Endereço do representante |
| CplEnd | String(200) | Sim | Complemento do endereço (sala, andar, etc.) |
| CepRep | Number(008,0) | Sim | CEP do endereço do representante |
| BaiRep | String(075) | Sim | Bairro do representante |
| CidRep | String(060) | Sim | Cidade do representante |
| SigUfs | String(002) | Sim | Estado do representante |
| SitRep | String(001) | Não | Situação do representante |
| QtdDep | Number(002,0) | Sim | Quantidade de dependentes para imposto de renda |
| DatNas | Date | Sim | Data do nascimento |
| NumRge | String(013) | Sim | Número do RG |
| OrgRge | String(006) | Sim | Órgão emissor do RG |
| DatRge | Date | Sim | Data de emissão do RG |
| RepCli | Number(009,0) | Sim | Código do representante como cliente |
| RepFor | Number(009,0) | Sim | Código do representante como fornecedor |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| CalIrf | String(001) | Sim | Indicativo se o cálculo de IRRF é por empresa |
| CalIss | String(001) | Sim | Indicativo se o cálculo de ISS é por empresa |
| CalIns | String(001) | Sim | Indicativo se o cálculo de INSS é por empresa |
| GerTit | String(001) | Sim | Gera título a pagar no pagamento da comissão do representante (S- Gera\N - Gera preparação tes.) |
| DatFis | Date | Sim | Data da última atualização da data fiscal |
| DatFat | Date | Sim | Data da última alteração da data fiscal |
| UsuFat | Number(010,0) | Sim | Usuário da última alteração da data fiscal |
| HorFat | Number(005,0) | Sim | Hora da última alteração da data fiscal |

---

## Chave Primária

- CodRep
- DatAtu
- HorAtu
- SeqAtu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
