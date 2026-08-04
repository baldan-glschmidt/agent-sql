# E900RIN

## Descrição

OP/OS - Remessa/Retorno Serviços Terceiros - Ligação Item Nota Fiscal Venda

---

## Resumo

- Campos: 14
- Chave Primária: 12 campo(s)
- Índices: 1
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Código da Origem do Produto |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SeqRot | Number(004,0) | Não | Sequência da Operação no Estágio (Quando Movimento por Operações) |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Não | Derivação do Produto |
| SeqSet | Number(004,0) | Não | Sequência da Remessa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| ProFim | String(001) | Sim | Indicativo se é produto final |
| QtdFat | Number(014,5) | Sim | Quantidade em itens faturados |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqRot
- CodPro
- CodDer
- SeqSet
- CodFil
- CodSnf
- NumNfv
- SeqIpv

---

## Índices

### E900RINIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv

---

## Relacionamentos

### IR_E900RIN_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E900RIN_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900RIN_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E900RIN_006

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E900RIN_010

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

