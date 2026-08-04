# E210MEA_TMP

## Descrição

Estoques - Movimento de estoque agrupado - Temporária

---

## Resumo

- Campos: 13
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodDep | String(010) | Sim | Código do depósito |
| DatEmi | Date | Não |  |
| TnsEst | String(005) | Sim | Código da transação |
| QtdMov | Number(014,5) | Sim | Quantidade do movimento |
| SeqAgr | Number(009,0) | Sim | Sequência do agrupamento |
| SeqPmv | Number(009,0) | Sim | Sequência da pendência |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
