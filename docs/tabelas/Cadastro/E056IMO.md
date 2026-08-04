# E056IMO

## Descrição

Cadastros - Tributos - Unidade Imobiliária

---

## Resumo

- Campos: 51
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodImo | String(020) | Não | Código da unidade imobiliária |
| NomImo | String(100) | Não | Nome da unidade imobiliária |
| TipUni | Number(002,0) | Sim | Indica o tipo da unidade imobiliária |
| DesImo | String(250) | Não | Descrição resumida sobre as informações relevantes da unidade imobiliária |
| NatImo | Number(001,0) | Sim | Indica a natureza do empreendimento |
| TipImo | String(001) | Sim | Tipo do imóvel (DIMOB) |
| CepImo | Number(008,0) | Sim | CEP do imóvel |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP do imóvel |
| EndImo | String(100) | Sim | Endereço do imóvel |
| NumEnd | String(060) | Sim | Número do endereço de entrega do cliente |
| CplEnd | String(200) | Sim | Complemento do endereço do imóvel |
| BaiImo | String(075) | Sim | Bairro do imóvel |
| CidImo | String(060) | Sim | Cidade do imóvel |
| SigUfs | String(002) | Sim | Sigla do estado do imóvel |
| CodPai | String(004) | Sim | Código do país do imóvel |
| RegTri | String(001) | Não | Indica o regime tributário aplicável sobre o imóvel |
| CodPri | String(004) | Sim | Código da tabela de presunção IRPJ |
| CodPrc | String(004) | Sim | Código da tabela de presunção CSLL |
| SitImo | String(001) | Não | Situação do imóvel |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| TipImv | Number(002,0) | Sim | Tipo imóvel |
| AreUco | Number(015,2) | Sim | Área útil construída |
| AreTco | Number(015,2) | Sim | Área total construída |
| AreTer | Number(015,2) | Sim | Área terreno |
| QtdGar | Number(003,0) | Sim | Quantidade garagem |
| QtdDor | Number(003,0) | Sim | Quantidade dormitórios |
| QtdBan | Number(003,0) | Sim | Quantidade banheiros |
| InsImf | String(030) | Sim | Código fornecido pela prefeitura para a identificação da obra ou para fins de recolhimento do IPTU |
| ImoCib | String(008) | Sim | Código do Cadastro Imobiliário Brasileiro - CIB |
| IndIpt | Number(001,0) | Sim | Indicador se o imóvel possui IPTU |
| NumIpt | String(060) | Sim | Número do IPTU |
| IndInc | Number(001,0) | Sim | Indicador se o imóvel possui INCRA |
| EspImo | String(002) | Sim | Espécie do Imóvel |
| DesOut | String(060) | Sim | Descrição da Espécie do Imóvel |
| EnqImo | String(002) | Sim | Enquadramento do Imóvel |
| CarReg | String(060) | Sim | Cartório de Registro do Imóvel |
| MatTra | String(060) | Sim | Matrícula ou Transcrição |
| IndRed | String(001) | Sim | Indicador de Redutor Social |
| CodPro | String(014) | Sim | Produto Ligado ao Imóvel |
| VlrImo | Number(015,2) | Sim | Valor da Unidade Imobiliária |
| TipIns | String(002) | Sim | Tipo do Instrumento |
| DesIns | String(060) | Sim | Descrição do Instrumento |
| DatIns | Date | Sim | Data do Instrumento |
| ObsImo | String(200) | Sim | Observação local imóvel |
| AreTot | Number(015,2) | Sim | Área total do terreno |

---

## Chave Primária

- CodEmp
- CodImo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
