# E900ROP

## Descrição

O.P./O.S. - Agrupamentos de O.Ps./O.Ss. p/ Derivação (Reprocesso/Sumarização)

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| OrpRpc | Number(009,0) | Não | Número da Ordem de Produção/Serviço de Agrupamento |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Não | Código da Derivação |
| QtdPrv | Number(014,5) | Não | Quantidade Prevista por Derivação |
| UniMed | String(003) | Não | Unidade de Medida do produto/serviço da O.P./O.S. |
| SeqCmd | Number(007,0) | Não | Sequência da Derivação na Máscara |
| ClaRop | String(001) | Não | Indicativo se a ordem trata um reprocesso ou sumarização de O.Ps./O.Ss. |

---

## Chave Primária

- CodEmp
- CodOri
- OrpRpc
- NumOrp
- CodPro
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900ROP_003

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900ROP_005

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E900ROP_007

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

