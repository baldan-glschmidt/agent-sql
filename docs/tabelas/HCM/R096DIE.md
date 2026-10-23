# R096DIE

## Descrição

Distribuição EPI

---

## Resumo

- Campos: 38
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodEpi | Number(008,0) | Não | Código do Epi |
| DatEnt | Date | Não | Data da Entrega |
| SeqDie | Number(003,0) | Não | Sequência da Distribuição |
| MedEpi | String(006) | Sim | Medida do EPI |
| QtdEnt | Number(003,0) | Sim | Quantidade da Entrega |
| DatDev | Date | Sim | Data da Devolução |
| QtdDev | Number(003,0) | Sim | Quantidade da Devolução |
| QtdDan | Number(003,0) | Sim | Quantidade Devolvida e Danificada |
| InsUso | String(001) | Sim | Instruções de Uso (S,N) |
| CodMtv | Number(003,0) | Sim | Motivo da Distribuição |
| ObsDis | String(080) | Sim | Observação |
| AssPro | String(001) | Sim | Indica se assinou protocolo de entrega |
| CodUsu | Number(010,0) | Sim | Código do Usuário que entregou o EPI |
| NumLot | Number(009,0) | Sim | Nr. de identificação do lote em que foi distribuído o EPI |
| CodOem | Number(008,0) | Sim | Código do Fornecedor |
| CerApr | String(020) | Sim | Certificado de Aprovação |
| RegCri | String(300) | Sim | Registro Criptografado |
| DhrAut | Number(014,6) | Sim | Data/Hora Autenticação Eletrônica |
| NumEip | String(015) | Sim | Endereço IP da máquina que colaborador assinou eletronicamente |
| USU_QtdDia | Number(002,0) | Sim | Dias Utilizar |
| USU_TipPro | String(001) | Sim | Tipo Processo |
| USU_ObsEst | Number(002,0) | Sim | Observação Estorno |
| USU_CODRQU | Number(009,0) | Sim | Codigo Requisição para Rota |
| USU_CODCCU | String(018) | Sim | Centro de Custo |
| USU_EmpOcp | Number(004,0) | Sim | Código da empresa da ordem de compra |
| USU_FilOcp | Number(005,0) | Sim | Código da filial da ordem de compra |
| USU_NumOcp | Number(008,0) | Sim | Número da ordem de compra |
| USU_SeqIpo | Number(004,0) | Sim | Sequência de item da ordem de compra |
| USU_StaGer | String(003) | Sim | Status da geração de ordem de compra |
| USU_ObsGer | String(200) | Sim | Observação da geração de ordem de compra |
| USU_EmpSol | Number(004,0) | Sim | Empresa da solicitação de compras |
| USU_NumSol | Number(009,0) | Sim | Número da solicitação de compras |
| USU_SeqSol | Number(006,0) | Sim | Sequência do item na solicitação de compras |
| USU_SitGer | String(030) | Sim | Situação da geração da solicitação de compras |
| USU_ObsSol | String(250) | Sim | Observação da geração da solicitação de compras |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodEpi
- DatEnt
- SeqDie

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096DIE_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R096DIE_003

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

### IR_R096DIE_012

**Tabela:** R096MTV

| Origem | Destino |
|--------|---------|
| CodMtv | CodMtv |

