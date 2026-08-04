# E900CMO

## Descrição

O.P./O.S. - Componentes Utilizados

---

## Resumo

- Campos: 54
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço Fabricado na O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Estágio de Produção |
| SeqCmp | Number(004,0) | Não | Sequência do Componente na utilização |
| CodCmp | String(014) | Não | Código do Componente (Produto) utilizado p/ consumo na O.P./O.S. |
| CodDer | String(007) | Sim | Código da Derivação do Componente (Produto) |
| QtdPrv | Number(014,5) | Não | Quantidade Proporcional Prevista p/ utilizar |
| QtdRes | Number(014,5) | Sim | Quantidade reservada no estoque (empenho) |
| QtdUti | Number(014,5) | Não | Quantidade Real utilizada |
| QtdSer | Number(014,5) | Sim | Quantidade Remetida de componentes p/ Serviços em Terceiros |
| QtdRts | Number(014,5) | Sim | Quantidade Retornada de sobras de componentes do Serviço em Terceiros |
| QtdSpa | Number(014,5) | Sim | Quantidade Separada no depósito |
| QtdReq | Number(014,5) | Sim | Quantidade requisitada de componentes pela produção |
| QtdTrf | Number(014,5) | Sim | Quantidade transferida (não atualiza quantidade utilizada) |
| UniMed | String(003) | Não | Unidade de medida do componente p/ Estoque |
| CodTns | String(005) | Não | Código da Transação p/ Movimentação de Estoques |
| CodDep | String(010) | Sim | Código do depósito de produto da quantidade utilizada |
| CodLot | String(050) | Sim | Lote de fabricação do componente (Produto Intermediário/Comprado) |
| CodCcu | String(009) | Sim | Código do Centro de Custo. |
| SolCmp | String(001) | Sim | Indica se componente foi solicitado/reservado/atendido no Estoque |
| NumSep | String(050) | Sim | Série de fabricação do Componente (matéria prima) utilizado |
| QtdMnc | Number(014,5) | Não | Quantidade de material não conforme |
| QtdCdr | Number(014,5) | Sim | Quantidade do componente destinado para refugo |
| BxaOrp | String(001) | Sim | Se for componente de alguma O.P./O.S., indica se o mesmo é baixado |
| NumCad | Number(009,0) | Sim | Número do Cadastro do Operador |
| CmpRep | String(001) | Sim | Indicativo se o componente poderá ter reposição |
| SeqRep | Number(004,0) | Sim | Seq. de indicação dos componentes de reposição |
| FotPro | String(014) | Sim | Código da Foto |
| FotDer | String(007) | Sim | Derivação da Foto |
| SeqFot | Number(004,0) | Sim | Número de Sequência da Foto no Cadastro de Fotos |
| CodCre | String(008) | Sim | Código do centro de recurso |
| QtdEnv | Number(014,5) | Sim | Quantidade enviada para o cliente através das notas de remessa |
| IndCob | String(001) | Sim | Indicativo se componente é cobrado |
| FrmBxa | String(001) | Sim | Indica se a forma da baixa de componente será automática ou manual |
| QtdRnf | Number(014,5) | Sim | Quantidade retornada dos componentes pela nota fiscal de retorno de industrialização |
| USU_CodReq | String(250) | Sim | Codigo da Requisicao e sequencia |
| USU_KitSeq | Number(004,0) | Sim | Sequencia Montagem Kit |
| USU_KidCod | String(020) | Sim | Código Kit |
| USU_CodCxa | Number(005,0) | Sim | Codigo da Caixa de Transporte do Corrinho |
| USU_nrocxa | Number(005,0) | Sim | Número da Caixa |
| USU_QtdInv | Number(014,5) | Sim | Qtde Inventário |
| USU_DatInv | Date | Sim | Data Inventário |
| USU_CodCre | String(008) | Sim | Código do Centro de Recurso (conjunto Máquina/Pessoa c/ mesma capacidade produtiva) |
| USU_IndRel | String(001) | Sim | Indicativo se Relaciona kit do componente com kit do Produto Pai |
| USU_nrprog | Number(006,0) | Sim | Numero Programa |
| USU_sqprog | Number(004,0) | Sim | Sequencia Programa |
| USU_QtdPic | Number(014,5) | Sim | Quantidade destinada ao Picking |
| USU_IndPgo | String(001) | Sim | Indicativo Pendente Geração OP (manuais produzidos que precisam de OP, motivo: agrupar e diminuir qtde OPs geradas) |
| USU_DatMov | Date | Sim | Data Movto OP |
| USU_CodCar1 | Number(005,0) | Sim | USU_CodCar1 |
| USU_SeqCar | Number(004,0) | Sim | Sequencia do Carrinho |
| USU_SeqRot | Number(004,0) | Sim | Seqüência lógica da operação no roteiro de produção |
| USU_NumEme | String(250) | Sim | Número da Requisição |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900CMO_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900CMO_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E900CMO_005

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCmp | CodPro |

### IR_E900CMO_015

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

### IR_E900CMO_016

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

