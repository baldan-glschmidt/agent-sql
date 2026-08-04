# E440TSV

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Produtos - NF Taxas Serviço

---

## Resumo

- Campos: 14
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| CodItx | Number(004,0) | Não | Código do item de taxa |
| TipPtx | Number(001,0) | Não | Tipo da taxa |
| DatIni | Date | Não | Data Inicial da Vigência |
| DatFim | Date | Não | Data Final da Vigência |
| FilIsv | Number(005,0) | Não | Filial da nota de cobrança de serviço |
| SnfIsv | String(003) | Não | Série da nota de cobrança de serviço |
| NfvIsv | Number(009,0) | Não | Número da nota de cobrança de serviço |
| SeqIsv | Number(003,0) | Não | Sequência do Item da nota de cobrança de serviço |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc
- CodItx
- TipPtx
- DatIni
- DatFim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440TSV_009

**Tabela:** E440TAX

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |
| CodItx | CodItx |
| TipPtx | TipPtx |
| DatIni | DatIni |
| DatFim | DatFim |

