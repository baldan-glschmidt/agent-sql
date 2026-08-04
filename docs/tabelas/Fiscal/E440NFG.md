# E440NFG

## Descrição

Compras - Notas Fiscais de Entrada - Dados Gerais - Extensão

---

## Resumo

- Campos: 34
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| CprIrf | String(001) | Sim | Indicativo de como aconteceu a retenção de IRRF |
| SegGer | Number(005,0) | Sim | Segundo e milissegundo da geração do registro |
| IndDev | String(030) | Sim | Número do DAR do INDEA |
| FasDev | String(030) | Sim | Número do DAR do FASE |
| VdiFcs | Number(015,2) | Sim | Somatório do valor diferido do ICMS relativo ao FCP |
| EfiFcs | Number(015,2) | Sim | Somatório do valor efetivo do ICMS relativo ao FCP |
| VicSdt | Number(015,2) | Sim | Somatório do valor do ICMS-ST desonerado |
| OriArm | String(001) | Sim | Identifica se é uma transf. saldo de um armazenador registrado junto ao INDEA |
| FilScp | Number(005,0) | Sim | Código da filial SCP onde será escriturado o documento |
| QtmBic | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico |
| VmoIcm | Number(015,2) | Sim | Soma dos valores do ICMS monofásico |
| QtmBir | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Retido |
| VmoIcr | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Retido |
| QtmBif | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Diferido |
| VmoIcf | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Diferido |
| QtmBid | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Destacado |
| VmoIcd | Number(015,2) | Sim | Soma dos valores do ICMS Monofásico Destacado |
| CodImr | Number(009,0) | Sim | Identificação do imóvel |
| SeqLci | Number(009,0) | Sim | Identificador de registro |
| TipAei | String(001) | Sim | Indicativo do tipo de pessoa do adquirente ou do encomendante (Jurídica ou Física) |
| TipFat | Number(001,0) | Sim | Tipo faturamento NFCom |
| FinEmi | Number(001,0) | Sim | Finalidade emissão NFCom |
| TipCte | Number(001,0) | Sim | Informação do tipo do CT-e |
| ChvSub | String(050) | Sim | Chave de acesso do Conhecimento de Transporte Eletrônico Substituído |
| DatPrv | Date | Sim | Data previsão entrega |
| TipGua | Number(001,0) | Sim | Tipo de Guia Agro |
| UfGuia | String(002) | Sim | UF de emissão da guia |
| SerGui | String(009) | Sim | Série de emissão da guia |
| NumGui | Number(009,0) | Sim | Número da guia |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
