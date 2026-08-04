# E039POR

## Descrição

Cadastros - Portadores

---

## Resumo

- Campos: 75
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPor | String(004) | Não | Código interno do portador (carteira, representante, advogado, bancos, etc..) |
| DesPor | String(030) | Não | Descrição do portador |
| AbrPor | String(010) | Não | Sigla do portador |
| CodBan | String(003) | Sim | Número do banco na FEBRABAN |
| CodAge | String(007) | Sim | Número da agência do banco |
| NumCco | String(014) | Sim | Número da conta interna do portador |
| FloBan | Number(002,0) | Sim | Float bancário |
| CodIn1 | String(003) | Sim | Código da primeira instrução padrão para o portador |
| CodIn2 | String(003) | Sim | Código da segunda instrução padrão para o portador |
| NumArb | Number(009,0) | Sim | Número de controle do arquivo de remessa para banco |
| ExpArb | Number(005,0) | Sim | Código do layout CNAB de exportação para bancos |
| ImpArb | Number(005,0) | Sim | Código do layout CNAB de importação de bancos |
| DirCrm | String(250) | Sim | Diretório padrão para arquivos de remessa para banco |
| DirCrt | String(250) | Sim | Diretório padrão para arquivos de retorno para banco |
| NumCce | String(020) | Sim | Número do convênio da empresa com o Banco para cobrança escritural |
| NumArp | Number(009,0) | Sim | Número de controle do arquivo de remessa para banco do PE (Pagamento Eletrônico) |
| NumCnv | String(020) | Sim | Número do convênio da empresa com o Banco para pagamento eletrônico |
| ExpArp | Number(005,0) | Sim | Código do layout FEBRABAN de exportação para bancos do PE (Pagamento Eletrônico) |
| ImpArp | Number(005,0) | Sim | Código do layout FEBRABAN de importação para bancos do PE (Pagamento Eletrônico) |
| NumAgr | Number(009,0) | Sim | Número do agrupamento para de remessa do PE |
| TaxPer | String(002) | Sim | Código da taxa de comissão de permanência |
| ModBlo | String(012) | Sim | Código do modelo de emissão de bloqueto bancário |
| ModBla | String(012) | Sim | Código do modelo de emissão de bloqueto bancário agrupado |
| RecUnn | Number(011,0) | Sim | Número do último nosso número utilizado |
| PerRem | Number(005,2) | Sim | Percentual de rateio do total de títulos na remessa para banco da Cobrança |
| PriRem | Number(006,0) | Sim | Prioridade do portador no rateio da remessa para banco da Cobrança |
| DirPrm | String(250) | Sim | Diretório padrão para arquivos de remessa para banco PE |
| DirPrt | String(250) | Sim | Diretório padrão para arquivos de retorno para banco PE |
| ImpArd | Number(005,0) | Sim | Código do layout de importação para bancos do DDA (Débito Direto Autorizado) |
| IndBpc | String(001) | Sim | Indicativo se bloqueia envio de títulos para proteção ao crédito |
| DirDda | String(250) | Sim | Diretório padrão para arquivos de retorno para banco DDA |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| TipJrs | String(001) | Sim | Indicativo se o juros de mora é simples ou composto |
| SisCob | Number(001,0) | Sim | Indicativo de qual o sistema de cobrança para impressão do boleto |
| TarAut | String(001) | Sim | Indicativo para mostrar se a tarifa deve ser gerada automática ou manualmente. |
| MinTed | Number(015,2) | Sim | Valor mínimo para que o tipo de pagamento seja TED |
| BaiLoj | String(001) | Sim | Indicativo se títulos do portador podem ser baixados na loja |
| ExiNma | String(001) | Sim | Exige identificação do número do malote |
| FrmCad | String(001) | Sim | Determina a forma de cadastramento do título no banco se é com ou sem registro |
| TipDoc | String(001) | Sim | Determina o tipo do documento se é tradicional ou escritural |
| EmiDoc | String(001) | Sim | Determina o emissor do título, banco, cliente, etc |
| TipDis | String(001) | Sim | Determina o distribuidor do título, banco, cliente, etc |
| DefAct | String(001) | Sim | Determina o aceite do documento |
| CodBxa | String(001) | Sim | Código baixa/devolução |
| PrzBxa | Number(003,0) | Sim | Prazo baixa/devolução |
| CobCad | String(001) | Sim | Instruções de cobrança cadastradas no banco |
| PrtTra | String(003) | Sim | Paramêtro de Transmissão |
| CodCpo | String(004) | Sim | Código do Compromisso |
| TipAmb | Number(001,0) | Sim | Ambiente de homologação ou produção |
| TipInb | Number(001,0) | Sim | Tipo da emnpresa para o banco |
| CgcEmp | Number(014,0) | Sim | Número do CNPJ ou CPF da empresa |
| DocIdeEmp | String(014) | Sim | Número do CNPJ ou CPF da empresa |
| TipEmb | Number(001,0) | Sim | Tipo da emissão do boleto |
| TipDib | Number(001,0) | Sim | Tipo da distribuição do boleto |
| BloTit | String(001) | Sim | Bloquear alterações nos títulos |
| ImpBol | String(001) | Sim | Indicativo se irá imprimir o documento de cobrança automaticamente |
| CodTrs | String(015) | Sim | Informação cedida pelo banco que identifica o arquivo remessa do cliente |
| CobPix | String(001) | Sim | Indicativo se irá gerar PIX QR Code de cobrança pelo ERP Banking |
| CrtPix | String(002) | Não | Carteira para cobrança via PIX |
| TipPix | Number(001,0) | Sim | Tipo de Chave para cobrança via PIX |
| ChvPix | String(250) | Sim | Chave para cobrança via PIX |
| BnkCob | String(001) | Sim | Indicativo se gerará a cobrança escritural pelo ERP Banking |
| BnkCrt | String(002) | Não | Carteira para os títulos em cobrança escritural no ERP Banking |
| BnkHib | String(001) | Sim | Indicativo se gera boleto híbrido (cobrança escritural e PIX) |
| ModPix | String(012) | Sim | Código do modelo do relatório PIX |
| USU_NumCont | String(020) | Sim | Numero do Contrato |
| USU_NumRem | Number(009,0) | Sim | Numero da Remessa |
| USU_EmaMail | String(150) | Sim | E-mail para Envio de Minutas |
| USU_tippor | Number(001,0) | Sim | Tipo de Portador |
| USU_EntFut | String(001) | Sim | Aceita título de nota de entrega futura |
| USU_QtdDia | Number(004,0) | Sim | Prazo (dias) |
| USU_AceCpf | String(001) | Sim | Aceita título de cliente pessoa fisica |

---

## Chave Primária

- CodEmp
- CodPor

---

## Índices

### USU_E039POR1

**Tipo:** Não unico

Campos:
- CodPor
- CodEmp
- FloBan

---

## Relacionamentos

### IR_E039POR_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

