# USU_TCtrImpEti

## Descrição

Controle de Impressao de Etiquetas

---

## Resumo

- Campos: 30
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_CodEmp | Number(004,0) | Não | Código da empresa |
| USU_CodOri | String(003) | Não | Código da Origem do Produto |
| USU_NumOrp | Number(009,0) | Não | Número da OP/OS |
| USU_CodPro | String(014) | Não | Código do produto |
| USU_CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc.) |
| USU_SeqMov | Number(006,0) | Não | Sequência de movimento na data de movimentação |
| USU_DatMov | Date | Não | Data da movimentação do estoque |
| USU_IndImp | String(001) | Sim | Indica Impressao |
| USU_NomImp | String(050) | Sim | Nome da Impressora |
| USU_IndDbq | String(001) | Sim | Indicativo se Desbloqueou Quantidade |
| USU_RegAti | String(001) | Não | Registro Ativo |
| USU_SeqEti | Number(010,0) | Não | Sequência Impressão Etiqueta |
| USU_DatDbq | Date | Não | Data Desbloqueio |
| USU_HorDbq | Time | Não | Hora Desbloqueio |
| USU_QtdMov | Number(014,5) | Sim | Quantidade Movimentada |
| USU_TipReg | String(001) | Não | Tipo Registro (etiqueta pátio, bloqueio/desbloqueio ou controle de rotas) |
| USU_CodCcu | String(009) | Sim | Código do centro de custos |
| USU_CodEtg | Number(004,0) | Sim | Código do Estágio Produção (Etapas na Fabricação de um Produto) |
| USU_SeqRot | Number(004,0) | Sim | Seqüência Roteiro |
| USU_DatCol | Date | Sim | Data Coleta |
| USU_HorCol | Time | Sim | Hora Coleta |
| USU_DatEnt | Date | Sim | Data Entrega |
| USU_HorEnt | Time | Sim | Hora Entrega |
| USU_UsuGer | Number(010,0) | Sim | Usuário Responsável pela Geração do Registro |
| USU_IndAOP | String(001) | Sim | Indicativo Apontou OP |
| USU_NroSer | String(016) | Sim | Numero de Serie do Produto |
| USU_NumUma | Number(010,0) | Sim | Numero da UMA |
| USU_SeqRotEnt | Number(004,0) | Sim | USU_SeqRotEnt |
| USU_CodCcuDes | String(009) | Sim | Código do Centro de Custo de Destino |
| USU_CodPrat | String(020) | Sim | USU_CodPrat |

---

## Chave Primária

- USU_CodEmp
- USU_CodOri
- USU_NumOrp
- USU_CodPro
- USU_CodDer
- USU_SeqMov
- USU_SeqEti

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
