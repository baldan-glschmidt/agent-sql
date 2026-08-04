# E440CCP

## Descrição

Notas Fiscais de Entrada - eventos de documentos eletrônicos - Produtos do Documento

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqEve | Number(004,0) | Não | Sequência do evento |
| TipEve | Number(006,0) | Não | Tipo do evento |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| QtdInf | Number(014,5) | Sim | Quantidade Informada do item do evento |
| VlrIbs | Number(013,2) | Sim | Valor IBS |
| VlrCbs | Number(013,2) | Sim | Valor CBS |
| SnfNfv | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- CodSnf
- NumNfc
- TipEve
- SeqEve
- SeqIpc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440CCP_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E440CCP_004

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

