# R350EMP

## Descrição

S-1000 - eSocial - Informações do Empregador

---

## Resumo

- Campos: 59
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| SeqEmp | Number(009,0) | Não | Sequência |
| CodFil | Number(006,0) | Não | Código da Filial |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| IniVal | Date | Sim | Data de início da validade das informações prestadas no evento |
| FimVal | Date | Sim | Data final da validade das informações |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| NoFiVa | Date | Sim | Data final da nova validade das informações |
| NomRaz | String(100) | Sim | Informar o nome do contribuinte ou razão social |
| ClaTri | Number(002,0) | Sim | Código Correspondente à Classificação Tributária do Contribuinte |
| NatJur | Number(004,0) | Sim | Código da natureza jurídica do contribuinte |
| IndCoo | Number(001,0) | Sim | Indicativo de Cooperativa |
| IndCon | Number(001,0) | Sim | Indicativo de Construtora |
| DesFol | Number(001,0) | Sim | Desoneração da Folha de Pagamento |
| RegEle | Number(001,0) | Sim | Registro Eletrônico |
| SisAfi | String(006) | Sim | Número SIAFI |
| SigMin | String(070) | Sim | Identificação do Ministério/Lei que concedeu o Certificado |
| NumCer | String(040) | Sim | Número do Certificado de entidade social, portaria ou Lei específica |
| DatEmi | Date | Sim | Data de emissão do certificado/publicação da Lei |
| DatVen | Date | Sim | Data de vencimento do certificado |
| NumPro | String(040) | Sim | Número do protocolo de pedido de renovação |
| DatPro | Date | Sim | Data do protocolo de renovação |
| DatPub | Date | Sim | Data de publicação no Diário Oficial da União |
| PagPub | Number(005,0) | Sim | Página no DOU referente à publicação do documento de concessão do certificado |
| NomCon | String(070) | Sim | Nome do contato na empresa |
| CpfCon | Number(011,0) | Sim | CPF do contato |
| TelCon | String(013) | Sim | Número do telefone com DDD do contato |
| EmaCon | String(060) | Sim | Endereço eletrônico do contato |
| ExiAco | Number(001,0) | Sim | Indicativo da existência de acordo internacional para isenção de multa |
| LayOut | String(006) | Sim | Leiaute |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| SitPJu | Number(002,0) | Sim | Indicativo de Situação Pessoa Jurídica |
| SitPFi | Number(002,0) | Sim | Indicativo de Situação Pessoa Física |
| RegPPS | String(001) | Sim | Regime Próprio de Previdência Social (S,N) |
| EstFed | String(004) | Sim | Estado da Federação |
| CodFed | Number(007,0) | Sim | Código da Cidade da Federação |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Determina se envio é válido |
| FinLuc | String(001) | Sim | Indicativo de entidade educativa/prática desportiva que tenha por objetivo a assistência ao adolescente e à educação profissional (art. 430, inciso II, CLT). |
| TraTem | String(001) | Sim | Indicativo de Empresa de Trabalho Temporário (Lei n 6.019/1974), com registro no Ministério do Trabalho. |
| RegTem | String(030) | Sim | Número do registro da Empresa de Trabalho Temporário no Ministério do Trabalho. |
| TipOrg | Number(001,0) | Sim | Tipo de Órgão Público |
| InsEFR | Number(014,0) | Sim | CNPJ do Ente Federativo Responsável - EFR |
| CfjEfr | String(014) | Sim | CNPJ do Ente Federativo Responsável - EFR |
| NomEnt | String(100) | Sim | Nome do Ente Federativo ao qual o órgão está vinculado |
| TipPod | Number(001,0) | Sim | Poder a que se refere o subeto |
| ValSup | Number(014,2) | Sim | Valor do subteto do Ente Federativo |
| OpcPRu | Number(002,0) | Sim | Opção pelo produtor rural de tributação da contribuição previdenciária |
| DatTra | Date | Sim | Data que ocorreu a transformação de Sociedade Sem Fins Lucrativos, para Socidade de Fins Lucrativos |
| PisCof | String(001) | Sim | Indicador de tributação sobre a folha de pagamento - PIS e PASEP |
| PerIrr | String(001) | Sim | Indicador de pertencimento do IRRF, IN RFB 2239/2024 |

---

## Chave Primária

- NumEmp
- FilEmp
- SeqEmp

---

## Índices

### R350EMPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
