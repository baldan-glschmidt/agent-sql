# E140RCV

## Descrição

Vendas - Complementos de Venda - Nota Fiscal de Saída

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqRcv | Number(003,0) | Não | Sequência do item |
| TipDoc | Number(001,0) | Sim | Tipo do documento |
| TipReg | Number(002,0) | Sim | Tipo de registro |
| DatVnd | Date | Sim | Data da venda |
| VlrVnd | Number(015,2) | Sim | Valor da venda |
| CodRep | Number(009,0) | Sim | Código do representante |
| SeqIte | Number(003,0) | Sim | Sequência do item no documento de venda |
| IndCan | Number(001,0) | Sim | Indicativo se o registro está cancelado |
| RcvExt | String(020) | Sim | Identificador externo de complemento de venda |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqRcv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140RCV_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

