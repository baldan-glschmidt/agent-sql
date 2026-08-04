# E069SEG

## Descrição

Cadastros - Seguradoras

---

## Resumo

- Campos: 56
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodSeg | Number(009,0) | Não | Código da Seguradora |
| NomSeg | String(100) | Não | Nome da Seguradora |
| ApeSeg | String(050) | Não | Nome fantasia da seguradora |
| InsEst | String(025) | Sim | Inscrição estadual da seguradora |
| InsMun | String(016) | Sim | Inscrição municipal da seguradora |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ da seguradora |
| DocIdeSeg | String(014) | Sim | Número do CNPJ da seguradora |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| EndNet | String(200) | Sim | Endereço do site da seguradora |
| FonFor | String(020) | Sim | Número do telefone - 1 |
| FonFo2 | String(020) | Sim | Número do telefone - 2 |
| FonFo3 | String(020) | Sim | Número do telefone - 3 |
| FaxFor | String(020) | Sim | Número do FAX da seguradora |
| CodCor | Number(009,0) | Sim | Código do corretor da seguradora |
| CodCli | Number(009,0) | Sim | Código da seguradora como cliente |
| CodFor | Number(009,0) | Sim | Código da seguradora como fornecedor |
| CodGre | Number(009,0) | Sim | Código do grupo de empresas |
| EndFor | String(100) | Sim | Endereço da seguradora |
| CplEnd | String(200) | Sim | Complemento do endereço da seguradora (sala, andar, etc.) |
| BaiFor | String(075) | Sim | Bairro da seguradora |
| CepFor | Number(008,0) | Sim | CEP da seguradora |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade da seguradora |
| CidFor | String(060) | Sim | Cidade da seguradora |
| SigUfs | String(002) | Sim | Estado da seguradora |
| CodPai | String(004) | Sim | Código do país da seguradora |
| CxaPst | Number(006,0) | Sim | Número da caixa postal da seguradora |
| SitSeg | String(001) | Não | Situação da seguradora |
| CodMot | Number(006,0) | Sim | Código do motivo da situação da seguradora |
| ObsMot | String(250) | Sim | Observação do motivo da situação da seguradora |
| UsuMot | Number(010,0) | Sim | Usuário responsável pelo motivo da situação da seguradora |
| DatMot | Date | Sim | Data do motivo da situação da seguradora |
| HorMot | Number(005,0) | Sim | Hora do motivo da situação da seguradora |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| UsuCad | Number(010,0) | Sim | Usuário responsável pelo cadastramento |
| DatCad | Date | Sim | Data do cadastramento da seguradora |
| HorCad | Number(005,0) | Sim | Hora/minuto do cadastramento da seguradora |
| PerSlp | Number(005,2) | Sim | Percentual de participação para sugestão nas vendas de serviços financeiros |
| VlrSlp | Number(011,2) | Sim | Valor de participação para sugestão nas vendas de serviços financeiros |
| RegSus | String(030) | Sim | Cadastro SUSEP |
| ProSus | String(030) | Sim | Número do processo na SUSEP |
| CerGar | String(060) | Sim | Certificado Garantia padrão da seguradora |
| ApoSeg | String(060) | Sim | Apólice Seguro padrão da seguradora |
| PerCom | Number(005,2) | Sim | Percentual de comissão para cobrança da seguradora |
| DatRep | Date | Sim | Data do repasse da comissão pela seguradora |
| QtdRev | Number(004,0) | Sim | Quantidade de parcelas para repasse ao vendedor |
| QtdRef | Number(004,0) | Sim | Quantidade de parcelas para repasse a filial |
| PerRep | Number(005,2) | Sim | Percentual de comissão para pagar ao representante |
| MinPar | Number(002,0) | Sim | Quantidade mínima de parcelas para venda do seguro Parcela Protegida |
| ImgSeg | Image | Sim | Imagem do Logo da Seguradora para impressão na apólice. |
| NenSeg | String(060) | Sim | Número do Endereço da Seguradora |
| ProGar | String(030) | Sim | Processo para garantia estendida. |
| ProPar | String(030) | Sim | Processo para parcela protegida. |
| ProSfr | String(030) | Sim | Código do processo de seguro furto e roubo na seguradora. |

---

## Chave Primária

- CodEmp
- CodSeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
