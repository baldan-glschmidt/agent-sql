# E900MEO

## Descrição

OP/OS - Movimento de Estoque

---

## Resumo

- Campos: 17
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Código da origem do produto/serviço fabricado na OP |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| SeqMeo | Number(009,0) | Não | Sequência da movimentação de estoque ocorrida na OP/OS |
| TipMeo | String(003) | Não | Tipo de movimentação de estoque ocorrida na OP/OS |
| CodPro | String(014) | Não | Código do produto movimentado |
| CodDer | String(007) | Não | Código da derivação do produto movimentado |
| CodDep | String(010) | Não | Código do depósito movimentado |
| DatMov | Date | Não | Data da movimentação de estoque |
| SeqMov | Number(006,0) | Sim | Sequência da movimentação de estoque |
| QtdMov | Number(014,5) | Sim | Quantidade da movimentação de estoque associada à OP |
| SeqIcp | Number(004,0) | Sim | Sequência da incorporação de produto geradora do movimento de estoque |
| CodEtg | Number(004,0) | Sim | Código do estágio gerador do movimento de estoque |
| SeqSpr | Number(004,0) | Sim | Sequência do subproduto gerador do movimento de estoque |
| SeqEoq | Number(005,0) | Sim | Sequência do movimento de OP gerador do movimento de estoque |
| SeqCmp | Number(004,0) | Sim | Sequência do componente gerador do movimento de estoque |
| CodEtq | String(032) | Sim | Código da etiqueta gerado pela Senior X |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- SeqMeo

---

## Índices

### E900MEOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqEoq
- CodPro
- CodDer
- TipMeo

### E900MEOIndice2

**Tipo:** Não unico

Campos:
- DatMov
- CodEmp

---

## Relacionamentos

### IR_E900MEO_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900MEO_009

**Tabela:** E210MVP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |
| CodDep | CodDep |
| DatMov | DatMov |
| SeqMov | SeqMov |

