# E900COP

## Descrição

OP/OS - Cabeçalho (Dados Gerais)

---

## Resumo

- Campos: 57
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Código da origem do produto/serviço fabricado na OP |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| CodPro | String(014) | Sim | Código do Produto/Serviço |
| CodPvp | String(008) | Sim | Código do Período de Produção |
| CodFil | Number(005,0) | Sim | Código da Filial do Pedido |
| NumPed | Number(008,0) | Sim | Número do Pedido |
| DtpIni | Date | Não | Data prevista para início da O.P./O.S. |
| DtpFim | Date | Não | Data prevista para final da O.P./O.S. |
| DtrIni | Date | Sim | Data real do início da O.P./O.S. |
| DtrFim | Date | Sim | Data real do final da O.P./O.S. (Normal ou Cancelada) |
| CodFam | String(006) | Não | Código da Família do Produto/Serviço |
| CodRot | String(014) | Não | Código do Roteiro Utilizado p/ fabricação do Produto/Serviço desta O.P./O.S. |
| TmpPrv | Number(012,3) | Sim | Tempo Previsto para produção (em dias) |
| SitOrp | String(001) | Não | Situação (E=Explodida, L=Liberada, S=Suspensa, F=Finalizada, A=Em Andamento, C=Cancelada, R=Reabilitada) |
| RotAlt | String(001) | Não | Indicador para detectar se o Roteiro utilizado foi alterado após geração O.P./O.S. |
| SitAnt | String(001) | Não | Situação anterior da O.P./O.S. |
| UltGop | Number(004,0) | Sim | Número da Última Guia Gerada |
| TipOrp | String(001) | Não | Tipo da Ordem de Produção/Serviço |
| DatGer | Date | Não | Data da Geração da O.P./O.S. |
| QtdPrv | Number(014,5) | Não | Quantidade Prevista para Fabricação |
| QtdRe1 | Number(014,5) | Sim | Quantidade Realizada de 1ª Qualidade |
| QtdRe2 | Number(014,5) | Sim | Quantidade Realizada de 2ª Qualidade |
| QtdRe3 | Number(014,5) | Sim | Quantidade Realizada de 3ª Qualidade |
| ObsOrp | String(240) | Sim | Observações complementares geradas pelo Usuário |
| ObsOr2 | String(240) | Sim | Observações complementares geradas pelo Sistema |
| NumPri | Number(004,0) | Sim | Número da Prioridade da O.P./O.S. p/ execução no Período |
| LotTec | Number(010,3) | Sim | Lote Técnico de fabricação determinado no Roteiro de Fabricação |
| UsuGer | Number(010,0) | Sim | Usuário Responsável pela Geração do Registro |
| CodMnf | String(010) | Sim | Código da Minifábrica |
| RelPrd | String(015) | Sim | Código do Relatório de Produção |
| SubLot | String(017) | Sim | Sublote do Relatório de Produção |
| CodFxa | String(015) | Sim | Código da faixa da grade |
| CodPgr | String(005) | Sim | Código da Proporcionalidade da Grade de Derivações |
| IdxGrd | Number(006,0) | Sim | Indexador da Grade |
| FilPrd | Number(005,0) | Sim | Código da filial de produção do item de produto |
| VerMod | String(015) | Sim | Última versão do modelo na qual é incrementada em cada nova alteração |
| VerRot | String(015) | Sim | Última versão do roteiro na qual é incrementada em cada nova alteração |
| UtiEqi | String(001) | Sim | Indicativo se a O.P./O.S. gerada possui componente equivalente |
| CodEqp | String(020) | Sim | Código do equipamento que sofreu manutenção |
| NumMnt | Number(009,0) | Sim | Número da manutenção do equipamento |
| CcuOri | String(009) | Sim | Código do centro de custo origem |
| CcuDes | String(009) | Sim | Código do centro de custo destino |
| PrcOrp | String(001) | Sim | Procedência da ordem |
| QtdIcp | Number(014,5) | Sim | Quantidade de produto incorporada na OP |
| USU_codccu | String(009) | Sim | Codigo Centro de Custo |
| USU_StsDsc | String(001) | Sim | Status Discos |
| USU_StsAce | String(001) | Sim | Status Acessorios |
| USU_StsPnt | String(001) | Sim | Status Pintura |
| USU_stssld | String(001) | Sim | Status Solda |
| USU_stsrod | String(001) | Sim | Status Roda |
| USU_stspro | String(001) | Sim | Status Produto Final |
| USU_StsEmb | String(001) | Sim | Status Embalagem |
| USU_DatSts | Date | Sim | Data da Geracao do Status |
| USU_AtuDat | String(001) | Sim | Atualizou Data (Defasagem) |
| USU_IndRel | String(001) | Sim | Indicativo Relacionamento |
| USU_CodBa2 | String(030) | Sim | Código de barras livre |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp

---

## Índices

### E900COPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- DtrFim

### E900COPIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri
- NumOrp
- SitOrp

### USU_E900COP1

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri
- NumOrp
- RelPrd

---

## Relacionamentos

### IR_E900COP_001

**Tabela:** E083ORI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |

### IR_E900COP_011

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E900COP_012

**Tabela:** E710ROT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodRot | CodRot |

