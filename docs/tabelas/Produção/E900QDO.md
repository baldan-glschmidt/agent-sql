# E900QDO

## Descrição

O.P./O.S. - Quantidades para Produto/Serviço e Derivação

---

## Resumo

- Campos: 30
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Não | Código da Derivação |
| QtdPrv | Number(014,5) | Não | Quantidade Prevista por Derivação |
| QtdRe1 | Number(014,5) | Sim | Quantidade Realizada 1ª Qualidade |
| QtdRe2 | Number(014,5) | Sim | Quantidade Realizada 2ª Qualidade |
| QtdRe3 | Number(014,5) | Sim | Quantidade Realizada 3ª Qualidade |
| QtdRfg | Number(014,5) | Sim | Quantidade Realizada de Refugos |
| QtdIql | Number(014,5) | Sim | Quantidade Retirada p/ Inspeção de Qualidade |
| UniMed | String(003) | Não | Unidade de Medida do produto da OP |
| SeqIpd | Number(004,0) | Sim | Item do Pedido (quando O.P./O.S. atende Pedido específico) |
| SeqCmd | Number(007,0) | Não | Sequência da Derivação na Máscara |
| CodTns | String(005) | Não | Código da Transação p/ Movimentação de Estoque |
| CodDep | String(010) | Sim | Código do Depósito p/ armazenar o Produto |
| CodLot | String(050) | Sim | Lote de fabricação do Produto Produzido (Acabado/Intermediário) |
| CodCcu | String(009) | Sim | Código do Centro de Custo |
| SepIni | String(050) | Sim | Número de Série Inicial (intervalo) dos Produtos da OP |
| SepFim | String(050) | Sim | Número de Série Final (intervalo) dos Produtos da OP |
| GerCga | String(001) | Sim | Considerado na Cálculo da Carga de Recursos p/ o Período (S=Sim, N=Não) |
| NumEpi | Number(009,0) | Sim | Identificador da inspeção aberta para a liberação do item |
| PvpPai | String(008) | Sim | Código do Período gerador (Procedente) quando é necessário produtos intermediários |
| ProOri | String(001) | Sim | É Produto/Serviço original da O.P./O.S. ou foi incluído? |
| QtdExc | Number(014,5) | Sim | Quantidade excedente tanto do produto original da O.P. como de novos incluídos |
| CodMod | String(014) | Sim | Código do Modelo utilizado na O.P./O.S. |
| IndCob | String(001) | Sim | Indicativo se componente é cobrado |
| AgrNec | String(025) | Sim | Agrupamento de necessidades |
| AgrPai | String(025) | Sim | Agrupamento de necessidades pai |
| QtdRnf | Number(014,5) | Sim | Quantidade retornada dos componentes pela nota fiscal de retorno de industrialização |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodPro
- CodDer

---

## Índices

### E900QDOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodOri
- NumOrp

---

## Relacionamentos

### IR_E900QDO_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900QDO_011

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

### IR_E900QDO_014

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

