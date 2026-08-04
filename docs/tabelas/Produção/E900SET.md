# E900SET

## Descrição

O.P./O.S. - Controle de Remessa/Retorno Serviços Terceiros

---

## Resumo

- Campos: 33
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SeqRot | Number(004,0) | Não | Sequência da Operação no Estágio (Quando Movimento por Operações) |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Não | Derivação do Produto |
| SeqSet | Number(004,0) | Não | Sequência da Remessa |
| NumGop | Number(004,0) | Sim | Número da Guia |
| QtdRm1 | Number(014,5) | Sim | Quantidade Remetida p/ Terceiros de 1ª Qualidade |
| QtdRm2 | Number(014,5) | Sim | Quantidade Remetida p/ Terceiros de 2ª Qualidade |
| QtdRm3 | Number(014,5) | Sim | Quantidade Remetida p/ Terceiros de 3ª Qualidade |
| FilNfv | Number(005,0) | Sim | Filial da Nota Fiscal de Saída |
| CodSnv | String(003) | Sim | Código da Série da Nota Fiscal de Saída |
| NumNfv | Number(009,0) | Sim | Número da Nota Fiscal de Saída da Remessa de Serviços p/ Terceiros |
| SeqIpv | Number(003,0) | Sim | Sequência do item produto na nota fiscal de saída |
| DatRem | Date | Não | Data da Remessa das quantidades no Estágio Produção |
| HorRem | Number(005,0) | Sim | Hora Remessa |
| QtdRt1 | Number(014,5) | Sim | Quantidade Retornada de Terceiros como 1ª Qualidade |
| QtdRt2 | Number(014,5) | Sim | Quantidade Retornada de Terceiros como 2ª Qualidade |
| QtdRt3 | Number(014,5) | Sim | Quantidade Retornada de Terceiros como 3ª Qualidade |
| FilNfc | Number(005,0) | Sim | Filial da Nota Fiscal de Entrada |
| CodNfc | String(003) | Sim | Código da Série da Nota Fiscal de Entrada |
| NumNfc | Number(009,0) | Sim | Número da Nota Fiscal de Retorno de Serviços p/ Terceiros |
| SeqIpc | Number(003,0) | Sim | Sequência do item produto na nota fiscal de entrada |
| DatRet | Date | Sim | Data do Retorno das quantidades no Estágio Produção |
| HorRet | Number(005,0) | Sim | Hora do Retorno |
| NumSep | String(050) | Sim | Número de série do produto |
| QtdIql | Number(014,5) | Sim | Quantidade Inspecionada pela Qualidade |
| QtdRfg | Number(014,5) | Sim | Quantidade Refugada |
| SeqSop | Number(004,0) | Não | Sequência |
| AgrRem | String(020) | Sim | Agrupamento de remessa de serviço para terceiros |
| UsuRem | Number(010,0) | Sim | Usuário responsável pela remessa do serviço |

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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900SET_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900SET_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E900SET_006

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E900SET_030

**Tabela:** E900SOP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |
| CodEtg | CodEtg |
| SeqRot | SeqRot |
| SeqSop | SeqSop |

