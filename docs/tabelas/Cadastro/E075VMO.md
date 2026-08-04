# E075VMO

## Descrição

Tributos - Notas Fiscais de Saída Acabado - INOVAR-AUTO

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeVmo | Number(009,0) | Não | Identificação |
| SeqNfs | Number(009,0) | Não | Sequencia |
| IdeMon | Number(009,0) | Não | Identificação Montadora |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| NumNfi | Number(009,0) | Não | Número inicial da nota fiscal |
| DatEmi | Date | Não | Data da emissão |
| QtdVen | Number(011,2) | Sim | Quantidade de venda |
| VlrCtb | Number(015,2) | Sim | Valor contábil |
| ParDed | Number(015,2) | Sim | Parcela dedutível |
| CstIcm | String(003) | Sim | Situação Tributária ICMS |
| TipNfs | Number(002,0) | Sim | Tipo Nota Fiscal |
| UtiPer | String(001) | Sim | Utilizada Período |

---

## Chave Primária

- IdeVmo
- SeqNfs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
