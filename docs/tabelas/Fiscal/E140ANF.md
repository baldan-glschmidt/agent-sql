# E140ANF

## Descrição

Tabelas - Notas Fiscais de Saída - NFCom

---

## Resumo

- Campos: 32
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| TipFat | Number(001,0) | Sim | Tipo faturamento NFCom |
| FinEmi | Number(001,0) | Sim | Finalidade emissão NFCom |
| EmpNsb | Number(004,0) | Não | Código da empresa da nota de comunicação substituída |
| FilNsb | Number(005,0) | Não | Código da Filial da nota de comunicação substituída |
| SnfNsb | String(003) | Não | Código da Série da nota de comunicação substituída |
| NumNsb | Number(009,0) | Não | Número da nota de comunicação substituída |
| MotNsb | Number(002,0) | Sim | Motivo da substituição |
| IndSpr | String(001) | Sim | Serviço Pré-Pago |
| IndMrd | String(001) | Sim | Indicador de Sessão de Meios de Rede |
| TipSrc | Number(002,0) | Sim | Tipo de serviço utilizado |
| NumCtr | String(012) | Sim | Número do contrato do assinante |
| CtrIni | Date | Sim | Data de início do contrato |
| CtrFin | Date | Sim | Data de término do contrato |
| NumTer | String(012) | Sim | Número do terminal principal do serviço contratado |
| UfsTer | String(002) | Sim | Sigla do estado |
| DatCmp | Date | Sim | Ano e mês referência do faturamento |
| DatVec | Date | Sim | Data de vencimento da fatura |
| UsoIni | Date | Sim | Data de período de uso Inicial |
| UsoFim | Date | Sim | Data de período de uso final |
| CodBar | String(048) | Sim | Linha digitável do código de barras |
| DebAut | String(020) | Sim | Código de autorização débito em conta |
| CodBan | String(005) | Sim | Número do banco para débito em conta |
| CodAge | String(010) | Sim | Número da agência bancária para débito em conta |
| CodPix | String(2000) | Sim | URL do QRCode do PIX da fatura |
| EmpCof | Number(004,0) | Não | Código da empresa da nota de comunicação de cofaturamento |
| FilCof | Number(005,0) | Não | Código da Filial da nota de comunicação de cofaturamento |
| SnfCof | String(003) | Não | Código da Série da nota de comunicação de cofaturamento |
| NumCof | Number(009,0) | Não | Número da nota de comunicação de cofaturamento |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

### E140ANFIndice1

**Tipo:** Não unico

Campos:
- CodEmp

---

## Relacionamentos

### IR_E140ANF_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140ANF_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

