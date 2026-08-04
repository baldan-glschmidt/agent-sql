# E090REP

## Descrição

Cadastros - Representantes

---

## Resumo

- Campos: 59
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRep | Number(009,0) | Não | Código do representante |
| NomRep | String(100) | Não | Nome do representante |
| ApeRep | String(050) | Não | Nome fantasia do representante |
| SenRep | String(020) | Sim | Senha Criptografada do Representante |
| TipRep | String(001) | Não | Tipo do representante |
| InsEst | String(025) | Sim | Inscrição estadual do representante |
| InsMun | String(016) | Sim | Número da Inscrição Municipal |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do representante |
| DocIdeRep | String(014) | Sim | Número do CNPJ ou CPF do representante |
| EndRep | String(100) | Não | Endereço do representante |
| CplEnd | String(200) | Sim | Complemento do endereço (sala, andar, etc.) |
| ZipCod | String(014) | Sim | Código da cidade do representante externo - ZIP CODE |
| CepRep | Number(008,0) | Sim | CEP do endereço do representante |
| BaiRep | String(075) | Sim | Bairro do representante |
| CidRep | String(060) | Sim | Cidade do representante |
| SigUfs | String(002) | Sim | Estado do representante |
| FonRep | String(020) | Sim | Número do telefone - 1 |
| FonRe2 | String(020) | Sim | Número do telefone - 2 |
| FonRe3 | String(020) | Sim | Número do telefone - 3 |
| FaxRep | String(020) | Sim | Número do FAX do representante |
| CxaPst | Number(006,0) | Sim | Número da caixa postal do representante |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| DatCad | Date | Sim | Data do cadastramento do representante |
| DatAtu | Date | Sim | Data da última alteração do representante |
| SitRep | String(001) | Não | Situação do representante |
| QtdDep | Number(002,0) | Sim | Quantidade de dependentes para imposto de renda |
| CalIrf | String(001) | Sim | Indicativo se o cálculo de IRRF é por empresa |
| CalIss | String(001) | Sim | Indicativo se o cálculo de ISS é por empresa |
| CalIns | String(001) | Sim | Indicativo se o cálculo de INSS é por empresa |
| FirInd | String(001) | Sim | Indicativo se o cálculo de IRRF será feito como o da Pessoa Física |
| GerTit | String(001) | Sim | Forma de pagamento da comissão do portador |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do representante |
| ObsMot | String(250) | Sim | Observação do motivo da situação do representante |
| UsuMot | Number(010,0) | Sim | Usuário responsável pelo motivo da situação do representante |
| DatMot | Date | Sim | Data do motivo da situação do representante |
| HorMot | Number(005,0) | Sim | Hora do motivo da situação do representante |
| DatNas | Date | Sim | Data do nascimento |
| NumRge | String(013) | Sim | Número do RG |
| OrgRge | String(006) | Sim | Órgão emissor do RG |
| DatRge | Date | Sim | Data de emissão do RG |
| RepCli | Number(009,0) | Sim | Código do representante como cliente |
| RepFor | Number(009,0) | Sim | Código do representante como fornecedor |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| CodCdi | Number(003,0) | Sim | Código do canal de distribuição padrão do representante |
| EenRep | String(018) | Sim | Código do endereço do representante |
| HorAtu | Number(005,0) | Sim | Hora da Atualização do Registro |
| NenRep | String(060) | Sim | Número do Endereço do Representante |
| UsuCad | Number(010,0) | Sim | Usuário responsável pelo cadastramento |
| HorCad | Number(005,0) | Sim | Hora/minuto do cadastramento do representante |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| NumIdf | String(040) | Sim | Número de identificação fiscal |
| IntWmw | String(001) | Sim | Indicativo se registro deve integrar com o WMW |
| SitWmw | String(001) | Sim | Situação do registro no WMW |
| USU_numcad | Number(009,0) | Sim | Numenro Cadastro Folha |
| USU_SitCat | String(001) | Sim | Situacao Representante Catalogo Eletronico |
| USU_senrep | String(010) | Sim | Senha Catalogo |
| USU_RepDed | String(001) | Sim | Representante Dedicado |

---

## Chave Primária

- CodRep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
