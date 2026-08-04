# E020SNF

## Descrição

Tabelas - Séries de Notas Fiscais

---

## Resumo

- Campos: 39
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| DesSnf | String(030) | Não | Descrição da série de notas fiscais |
| AbrSnf | String(010) | Não | Abreviatura da série de notas fiscais |
| UltNum | Number(009,0) | Sim | Número da última nota fiscal emitida pela filial |
| UltDat | Date | Sim | Data da última nota fiscal emitida pela filial |
| NumNfd | Number(009,0) | Sim | Faixa de número das últimas NF impressas |
| NumNfa | Number(009,0) | Sim | Últimas emissões de NF até número... |
| QtdItp | Number(003,0) | Sim | Quantidade máxima de itens de produtos previsto para a nota fiscal |
| QtdIts | Number(003,0) | Sim | Quantidade máxima de itens de serviços previsto para a nota fiscal |
| QtdPar | Number(003,0) | Sim | Quantidade de parcelas permitidas pela série de NF |
| AplSnf | String(001) | Não | Aplicação da série de nota fiscal |
| UltPre | Number(009,0) | Sim | Número do último número de nota fiscal pré-impresso |
| ModRel | String(012) | Sim | Código do modelo de emissão de notas fiscais |
| ModDup | String(012) | Sim | Código do modelo de emissão de duplicatas |
| UltDup | Number(010,0) | Sim | Número da última duplicata gerada |
| CodEdc | String(003) | Sim | Espécie de documento para fins fiscais |
| VenDbs | Date | Sim | Data base da saída de mercadoria para nota fiscal |
| VenDbv | Date | Sim | Data base para cálculo dos vencimento dos títulos a serem gerados |
| CodSel | String(020) | Sim | Código da Série Legal |
| CodSsl | String(002) | Sim | Código da Subsérie Legal |
| UtiImp | String(001) | Sim | Indicativo se a série é utilizada para impostos (integração) |
| CodEqu | Number(003,0) | Sim | Código Equipamento Fiscal Padrão |
| IndNma | String(001) | Sim | Indicativo se permite controlar a numeração das notas fiscais de saída manualmente |
| DisAut | Number(002,0) | Sim | Tipo de dispositivo autorizado para a série de nota fiscal |
| DirNel | String(250) | Sim | Diretório onde deve ser gravado o arquivo de exportação da nota fiscal eletrônica |
| QtdPos | Number(002,0) | Sim | Quantidade de posições do número da nota fiscal desta série |
| DirCte | String(250) | Sim | Diretório onde deve ser gravado o arquivo de exportação do conhecimento de transporte eletrônico |
| DirNes | String(250) | Sim | Diretório onde deve ser gravado o arquivo de exportação da nota fiscal eletrônica de serviço |
| ExcVar | String(001) | Não | Indica se o uso desta série é exclusiva do sistema de varejo |
| IndIsv | String(001) | Sim | Indicativo se a série é utilizada para intermediação de serviços no Retaguarda |
| SerInt | Number(003,0) | Sim | Código da série utilizada para integração. |
| SitSnf | String(001) | Sim | Situação da série fiscal para uso em cupons fiscais eletrônicos (SAT) |
| CodInt | Number(003,0) | Sim | Código para integração NFS-e |
| CodSnp | String(003) | Sim | Código da próxima série de notas fiscais |
| DblNfe | String(250) | Sim | Diretório para a geração dos boletos relativos à nota fiscal |
| RegEsp | String(001) | Sim | Exportar na EFD como Nota Fiscal emitida por regime especial ou norma específica |
| DblImp | String(250) | Sim | Diretório para gravação dos boletos relativos a nota fiscal para impressão |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E020SNF_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

