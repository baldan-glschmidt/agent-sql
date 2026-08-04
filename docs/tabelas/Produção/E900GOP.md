# E900GOP

## Descrição

O.P./O.S. - Guias O.P. p/ Derivação

---

## Resumo

- Campos: 18
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| NumGop | Number(004,0) | Não | Número da Guia de Produção |
| CodPro | String(014) | Não | Código do Produto |
| CodDer | String(007) | Não | Código da Derivação |
| QtdPrv | Number(014,5) | Não | Quantidade Prevista da Guia |
| QtdRe1 | Number(014,5) | Sim | Quantidade Realizada 1ª Qualidade |
| QtdRe2 | Number(014,5) | Sim | Quantidade Realizada 2ª Qualidade |
| QtdRe3 | Number(014,5) | Sim | Quantidade Realizada 3ª Qualidade |
| QtdRfg | Number(014,5) | Sim | Quantidade Realizada de Refugos na Produção |
| QtdIql | Number(014,5) | Sim | Quantidade Retirada p/ Inspeção de Qualidade |
| UniMed | String(003) | Não | Unidade Medida do produto da OP |
| SeqIpd | Number(004,0) | Sim | Item do Pedido (Quando OP p/ atender pedido) |
| CodTns | String(005) | Não | Código da Transação p/ movimentação de estoques |
| CodDep | String(010) | Não | Código do Depósito p/ armazenar produto |
| CodLot | String(050) | Sim | Lote de fabricação do Produto produzido (Acabado/Intermediário) |
| CodCcu | String(009) | Sim | Código do Centro de Custos |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- NumGop

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900GOP_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900GOP_012

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

### IR_E900GOP_014

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

