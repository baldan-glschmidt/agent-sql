# E140IDE

## Descrição

Vendas - Informações de Documentos Eletrônicos

---

## Resumo

- Campos: 32
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SitDoe | Number(002,0) | Sim | Situação do documento eletrônico |
| SitDea | Number(002,0) | Sim | Situação do documento eletrônico anterior |
| ChvDoe | String(050) | Sim | Chave do documento eletrônico |
| NumDfs | Number(015,0) | Sim | Número da nota fiscal de serviço na prefeitura |
| CodVer | String(100) | Sim | Código de verificação do documento eletrônico |
| NumPrt | String(100) | Sim | Número do protocolo de autorização do documento eletrônico |
| DatAut | Date | Sim | Data de autorização do documento eletrônico |
| HorAut | Number(005,0) | Sim | Hora da autorização do documento eletrônico |
| UsuEmi | Number(010,0) | Não | Usuario que realizou a emissão do documento eletrônico |
| NumPrc | String(100) | Sim | Número do protocolo de cancelamento do documento eletrônico |
| DatCan | Date | Sim | Data de autorização para cancelamento do documento eletrônico |
| HorCan | Number(005,0) | Sim | Hora da autorização do cancelamento do documento eletrônico |
| UsuCan | Number(010,0) | Sim | Usuario que solicitou o cancelamento do documento eletrônico |
| NumPri | String(100) | Sim | Número do protocolo de inutilização do documento eletrônico |
| DatInu | Date | Sim | Data de autorização da Inutilização do documento eletrônico |
| HorInu | Number(005,0) | Sim | Hora da autorização de inutilização do documento eletrônico |
| UsuInu | Number(010,0) | Sim | Usuário que solicitou inutilização do documento eletrônico |
| ReaPed | String(001) | Sim | Indica que o pedido será reabilitado no ret. do canc. de doc. eletrônicos |
| ReaPfa | String(001) | Sim | Indica que a pré-fatura será reabilitada no ret. do canc. de doc. eletrônicos |
| ReaTck | String(001) | Sim | Indica que o ticket será reabilitado no ret. do canc. de doc. eletrônicos |
| ReaCol | String(001) | Sim | Indica que a coleta será reabilitada no ret. do canc. de doc. eletrônicos |
| TipCtg | Number(001,0) | Sim | Tipo de contingência em que o documento foi autorizado |
| ChvCtg | String(050) | Sim | Chave eletrônica gerada pela contingência |
| DatCtg | Date | Sim | Data de entrada em contingência |
| HorCtg | Number(005,0) | Sim | Hora de entrada em contingência |
| MotCtg | Number(006,0) | Sim | Código do motivo da entrada em contingência |
| ObsCtg | String(250) | Sim | Observações do motivo referente a entrada em contingência |
| SegCba | String(036) | Sim | Segundo código de barras do documento autorizado em contingência |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

### E140IDEIndice1

**Tipo:** Não unico

Campos:
- ChvDoe
- SitDoe

### E140IDEIndice2

**Tipo:** Não unico

Campos:
- ChvDoe

---

## Relacionamentos

Nenhum relacionamento cadastrado.
