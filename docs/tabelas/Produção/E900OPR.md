# E900OPR

## Descrição

O.P./O.S. - Ordens de Produção do processo de remessa para terceiros

---

## Resumo

- Campos: 33
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| NumPrc | Number(009,0) | Não | Número sequencial do processo de remessa para terceiros |
| SeqOpr | Number(009,0) | Não | Sequência |
| SitOpr | String(001) | Sim | Situação da OP no controle de processo |
| CodOri | String(003) | Sim | Código da origem |
| NumOrp | Number(009,0) | Sim | Número da OP/OS |
| CodEtg | Number(004,0) | Sim | Código do Estágio Produção (Etapas na Fabricação de um Produto) |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do Produto (tamanho, cor, etc.) |
| UniMed | String(003) | Sim | Código da unidade de medida |
| DtrIni | Date | Sim | Data real do início da O.P./O.S. |
| HorIni | Number(005,0) | Sim | Data real do início da O.P./O.S. |
| QtdPrv | Number(014,5) | Sim | Quantidade prevista para fabricação |
| QtdRm1 | Number(014,5) | Sim | Quantidade remetida para terceiros de 1ª qualidade |
| QtdRm2 | Number(014,5) | Sim | Quantidade remetida para terceiros de 2ª qualidade |
| QtdRm3 | Number(014,5) | Sim | Quantidade remetida para terceiros de 3ª qualidade |
| QtdMvp | Number(014,5) | Sim | Quantidade total realizada |
| QtdPro | Number(014,5) | Sim | Quantidade total remetida |
| QtdRfg | Number(014,5) | Sim | Quantidade total refugos |
| CodRot | String(014) | Sim | Código do Roteiro de Produção associado ao Produto |
| SeqRot | Number(004,0) | Sim | Sequência da operação no roteiro da OP/OS |
| DatIni | Date | Sim | Data real de início da operação na O.P./O.S. |
| HrrIni | Number(005,0) | Sim | Hora real de início da operação na O.P./O.S. |
| ForOri | Number(009,0) | Sim | Código do fornecedor original |
| CodFor | Number(009,0) | Sim | Código do fornecedor |
| CodMod | String(014) | Sim | Código do Modelo associado ao Produto. |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra |
| NumGop | Number(004,0) | Sim | Número da Guia de Produção |
| SeqSop | Number(004,0) | Sim | Sequência do serviço para terceiros |
| CodSer | String(014) | Sim | Código do serviço |
| SeqSet | Number(004,0) | Sim | Sequência da remessa |
| FilPro | Number(005,0) | Sim | Filial de produção do estágio |
| DtpFim | Date | Sim | Data final prevista para estágio de produção |

---

## Chave Primária

- CodEmp
- NumPrc
- SeqOpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900OPR_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E900OPR_001

**Tabela:** E900CPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| NumPrc | NumPrc |

