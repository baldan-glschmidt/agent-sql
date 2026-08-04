# E070FAG

## Descrição

Filial - Parâmetros para Assistência Técnica e Garantia

---

## Resumo

- Campos: 19
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de saída |
| TnsPnf | String(005) | Sim | Transação para notas fiscais de produtos |
| TnsSnf | String(005) | Sim | Transação para notas fiscais de serviços |
| TnsPpv | String(005) | Sim | Transação para pedidos de produtos |
| TnsSpv | String(005) | Sim | Transação para pedidos de serviços |
| SnfSrv | String(003) | Sim | Código da série da nota fiscal de saída de serviço |
| CodSer | String(014) | Sim | Código do serviço padrão para a geração da nota de cobrança |
| TprAtp | String(004) | Sim | Tabela de preço de produto para assistência técnica |
| TprAts | String(004) | Sim | Tabela de preço de serviço para assistência técnica |
| DepAtv | String(010) | Sim | Depósito de assistência técnica para armazenar os produtos com defeito. |
| OnfEpc | Number(004,0) | Sim | Operação de nota fiscal para notas fiscais de entrada para conserto. |
| OnfRpc | Number(004,0) | Sim | Operação de nota fiscal para notas fiscais de remessa para conserto. |
| OnfRce | Number(004,0) | Sim | Operação de nota fiscal para notas fiscais de retorno de conserto externo. |
| OnfRcc | Number(004,0) | Sim | Operação de nota fiscal para notas fiscais de retorno de conserto para cliente. |
| OnfTef | Number(004,0) | Sim | Operação de nota fiscal para transferência entre filiais. |
| MdrDat | String(012) | Sim | Modelo de relatório para impressão do documento da assistência técnica. |
| FilUat | String(001) | Sim | Indica se a filial utiliza assistência técnica integrada com o varejo da Senior. |

---

## Chave Primária

- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070FAG_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

