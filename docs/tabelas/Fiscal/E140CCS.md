# E140CCS

## Descrição

Vendas - Notas Fiscais de Saída - Controle de eventos de documentos eletrônicos - Serviços do Documento

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
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
| SeqIsv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| QtdInf | Number(014,5) | Sim | Quantidade Informada do item do evento |
| VlrIbs | Number(013,2) | Sim | Valor IBS |
| VlrCbs | Number(013,2) | Sim | Valor CBS |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- TipEve
- SeqEve
- SeqIsv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140CCS_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E140CCS_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

