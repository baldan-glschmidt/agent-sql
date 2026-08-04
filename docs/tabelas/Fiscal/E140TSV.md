# E140TSV

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Produtos - NF Taxas Serviço

---

## Resumo

- Campos: 13
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota de devolução |
| SeqIpv | Number(003,0) | Não | Sequência do Item da nota de devolução |
| CodItx | Number(004,0) | Não | Código do item de taxa |
| TipPtx | Number(001,0) | Não | Tipo da taxa |
| DatIni | Date | Não | Data inicial vigência |
| DatFim | Date | Não | Data Final vigência |
| FilIsv | Number(005,0) | Não | Filial da nota de cobrança de serviço |
| SnfIsv | String(003) | Não | Série da nota de cobrança de serviço |
| NfvIsv | Number(009,0) | Não | Número da nota de cobrança de serviço |
| SeqIsv | Number(003,0) | Não | Sequência do Item da nota de cobrança de serviço |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv
- CodItx
- TipPtx
- DatIni
- DatFim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140TSV_008

**Tabela:** E140TAX

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIpv | SeqIpv |
| CodItx | CodItx |
| TipPtx | TipPtx |
| DatIni | DatIni |
| DatFim | DatFim |

