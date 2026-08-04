# E140ECO

## Descrição

Vendas - Notas Fiscais de Saída - Controle dos eventos do ECONF

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqEve | Number(004,0) | Não | Sequência do evento |
| TipEve | Number(006,0) | Não | Tipo de evento |
| CodTpt | String(003) | Não | Código do tipo do título movimentado |
| NumTit | String(015) | Não | Número do título a receber |
| SeqMov | Number(004,0) | Não | Sequência de movimento do título |
| TipFpg | Number(002,0) | Não | Tipo de Pagamento para controle do Acerto |
| VlrMov | Number(015,2) | Não | Valor do Movimento do título |
| DatMov | Date | Não | Data do Movimento do título |
| FilPag | Number(005,0) | Não | Código da filial de pagamento do título |

---

## Chave Primária

- IdeUni

---

## Índices

### E140ECOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodTpt
- NumTit
- SeqMov

### E140ECOIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv
- TipEve
- SeqEve

---

## Relacionamentos

### IR_E140ECO_005

**Tabela:** E140CCE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| TipEve | TipEve |
| SeqEve | SeqEve |

### IR_E140ECO_013

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| FilPag | CodFil |

