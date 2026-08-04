# E000DOW

## Descrição

Tabelas - Integrações - Distribuição de lote/série de itens de ordens de separação/recebimento

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumOrd | String(020) | Não | Número da ordem de separação/recebimento |
| SeqIto | Number(004,0) | Não | Sequência do item da ordem de separação/recebimento |
| SeqDls | Number(006,0) | Não | Sequência de movimento de item |
| CodDep | String(010) | Não | Código do depósito a ser baixado o estoque do produto do pedido |
| DatVlt | Date | Sim | Data de validade do produto no depósito |
| CodLot | String(050) | Sim | Código do lote de fabricação do produto |
| NumSep | String(050) | Sim | Número de série do produto |
| QtdOrd | Number(014,5) | Sim | Quantidade do item na ordem de separação/recebimento |
| QtdFis | Number(014,5) | Sim | Quantidade física do item no depósito |
| ObsDls | String(250) | Sim | Texto da observação |
| DatFab | Date | Sim | Data de fabricação do lote |

---

## Chave Primária

- CodEmp
- CodFil
- NumOrd
- SeqIto
- SeqDls

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
