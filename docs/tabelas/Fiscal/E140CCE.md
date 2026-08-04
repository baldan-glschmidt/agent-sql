# E140CCE

## Descrição

Vendas - Notas Fiscais de Saída - Controle de eventos de documentos eletrônicos

---

## Resumo

- Campos: 44
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqEve | Number(004,0) | Não | Sequência do evento |
| TipEve | Number(006,0) | Não | Tipo do evento |
| DesEve | String(100) | Sim | Descrição do evento |
| DatEve | Date | Sim | Data do evento |
| HorEve | Number(005,0) | Sim | Hora do evento |
| UsuEve | Number(010,0) | Sim | Usuário solicitante do evento |
| CodOrg | Number(002,0) | Sim | Código do órgão de recepção do evento |
| DesCor | String(999) | Sim | Descritivo da correção a ser considerada |
| SitCce | Number(002,0) | Não | Situação do evento (eventos de Cancelamento de NF-e e Carta de Correção) |
| NumPrt | String(017) | Sim | Número do protocolo de autorização ou recebimento |
| DatAut | Date | Sim | Data do protocolo de autorização |
| HorAut | Number(005,0) | Sim | Hora do protocolo de autorização |
| JusEve | String(254) | Sim | Justificativa do evento |
| NomMot | String(100) | Sim | Nome do motorista |
| CgcCpf | Number(012,0) | Sim | Número do CPF do motorista |
| NumPrc | String(017) | Sim | Protocolo do pedido de cancelamento de prorrogação de suspensão de ICMS |
| DatPro | Date | Sim | Data do protocolo de recebimento do evento de prorrogação de suspensão de ICMS |
| HorPro | Number(005,0) | Sim | Hora do protocolo de recebimento do evento de prorrogação de suspensão de ICMS |
| DatPrc | Date | Sim | Data do protocolo de cancelamento do evento de prorrogação de suspensão de ICMS |
| HorPrc | Number(005,0) | Sim | Hora do protocolo de cancelamento do evento de prorrogação de suspensão de ICMS |
| IdeEve | String(100) | Sim | Identificação do evento |
| EveOri | String(100) | Sim | Identificação do evento de origem emitido pelo contribuinte |
| ChvNrf | String(050) | Sim | Chave Eletrônica da Nota Fiscal Referenciada no Evento |
| SeqEnt | Number(004,0) | Sim | Sequência do registro de entrega |
| RelSeq | Number(004,0) | Sim | Sequência do Evento Relacionado. |
| RelTip | Number(006,0) | Sim | Tipo do Evento Relacionado. |
| DatIte | Date | Sim | Data da Tentativa da Entrega |
| HorIte | Number(005,0) | Sim | Hora da Tentativa da Entrega |
| MotIte | Number(001,0) | Sim | Motivo do insucesso de entrega CT-e |
| NrtIte | Number(003,0) | Sim | Número da Tentativa de Entrega que não Teve Insucesso |
| LatIte | Number(008,6) | Sim | Latitude do ponto da entrega |
| LngIte | Number(009,6) | Sim | Longitude do ponto da entrega |
| HasIte | String(028) | Sim | Hash da Tentativa de Entrega |
| DatHas | Date | Sim | Data da Geração do Hash da Tentativa de Entrega |
| HorHas | Number(005,0) | Sim | Hora da Geração do Hash da Tentativa de Entrega |
| TipAut | String(001) | Sim | Tipo de autorização para o evento do ator interessado |
| TipCat | String(001) | Sim | Indicativo do tipo de pessoa do autorizado (Jurídica ou Física) |
| CgcAut | Number(014,0) | Sim | CNPJ ou CPF do autorizado para o evento do ator interessado |
| DocIdeAut | String(014) | Sim | CNPJ ou CPF do autorizado para o evento do ator interessado |
| DatPrv | Date | Sim | Data previsão de entrega |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- TipEve
- SeqEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140CCE_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E140CCE_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

