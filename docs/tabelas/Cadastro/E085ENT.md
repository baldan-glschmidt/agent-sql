# E085ENT

## Descrição

Cadastros - Clientes - Endereços de Entrega

---

## Resumo

- Campos: 43
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| SeqEnt | Number(005,0) | Não | Sequência de endereços de entrega |
| EndEnt | String(100) | Não | Endereço de entrega do cliente |
| CplEnt | String(200) | Sim | Complemento do endereço de entrega do cliente |
| PrxEnt | String(120) | Sim | Ponto de referência ou proximidade do endereço de entrega |
| ZipEnt | String(014) | Sim | Código da cidade do endereço de entrega do cliente externo - ZIP CODE |
| CepEnt | Number(008,0) | Sim | CEP do endereço de entrega do cliente |
| IniEnt | Number(008,0) | Sim | Faixa inicial do CEP do endereço de entrega do cliente |
| CidEnt | String(060) | Sim | Cidade do endereço de entrega do cliente |
| EstEnt | String(002) | Sim | Estado do endereço de entrega do cliente |
| PaiEnt | String(004) | Sim | Código do país de entrega do cliente |
| InsEnt | String(025) | Sim | Inscrição estadual do endereço de entrega |
| BaiEnt | String(075) | Sim | Bairro de entrega do cliente |
| CodRoe | String(003) | Sim | Código da Rota |
| SeqRoe | Number(004,0) | Sim | Sequência |
| CgcEnt | Number(014,0) | Sim | Número do CNPJ/CPF de Entrega |
| DocIdeEnt | String(014) | Sim | Número do CNPJ/CPF de Entrega |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| SitReg | String(001) | Sim | Situação do registro |
| CodSro | String(003) | Sim | Código da Sub Rota |
| EenEnt | String(018) | Sim | Código do endereço de entrega do cliente |
| NenEnt | String(060) | Sim | Número do Endereço de Entrega do Cliente |
| AcrDia | Number(005,2) | Sim | Percentual de acréscimo na diária paga ao motorista |
| VlrAcr | Number(015,2) | Sim | Valor de acréscimo na diária paga ao motorista |
| NomCli | String(100) | Sim | Nome do cliente de entrega |
| EmpFre | Number(004,0) | Sim | Código da empresa |
| TabFre | String(004) | Sim | Código da tabela de preço frete |
| DatIni | Date | Sim | Data início de validade da tabela de preço |
| LocEnt | Number(008,0) | Sim | Código da localização do local para entrega do frete |
| SeqFlc | Number(004,0) | Sim | Sequência da localização do frete |
| FilFlc | Number(005,0) | Sim | Código da filial |
| FaxEnt | String(020) | Sim | Número do fax de contato no endereço de entrega |
| FonEnt | String(020) | Sim | Número do telefone de contato no endereço de entrega |
| CelEnt | String(020) | Sim | Número do telefone celular de contato no endereco de entrega |
| EmaEnt | String(100) | Sim | E-Mail de contato no endereço de entrega |
| TipEnt | String(001) | Sim | Tipo do cliente |
| IndOba | Number(001,0) | Sim | Indicativo de Prestação de Serviços em Obra de Construção Civil |
| NroCno | String(014) | Sim | Número de inscrição do cadastro nacional de obra (CNO) |
| VlrLat | String(100) | Sim | Valor da Latitude |
| VlrLon | String(100) | Sim | Valor da Longitude |
| TipEnd | Number(002,0) | Sim | Tipo do Endereço de Entrega |

---

## Chave Primária

- CodCli
- SeqEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085ENT_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

