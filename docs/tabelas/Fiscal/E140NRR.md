# E140NRR

## Descrição

Vendas - Nota referenciada de reembolso da NFS-e

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqNrr | Number(003,0) | Não | Sequencia da nota fiscal referenciada |
| ChvDoe | String(050) | Sim | Chave do documento eletrônico |
| DatEmi | Date | Sim | Data da emissão da nota fiscal referenciada |
| DatCmp | Date | Sim | Data da competência da nota fiscal referenciada |
| CodFor | Number(009,0) | Sim | Código do fornecedor do documento referenciado |
| RaiDfe | Number(007,0) | Sim | Código do município emissor do documento fiscal que não se encontra no repositório nacional |
| TipNre | Number(001,0) | Sim | Tipo de Nota de Reembolso |
| TipChd | Number(001,0) | Sim | Tipo da Chave do DFe |
| NumNre | String(255) | Sim | Número do documento de reembolso |
| DesNre | String(255) | Sim | Descrição do documento de reembolso |
| TipRee | Number(002,0) | Sim | Tipo de reembolso |
| DesRee | String(150) | Sim | Descrição do reembolso |
| VlrRee | Number(015,2) | Sim | Valor do reembolso |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqNrr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140NRR_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140NRR_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

