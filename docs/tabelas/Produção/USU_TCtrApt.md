# USU_TCtrApt

## Descrição

Controle de Apontamento

---

## Resumo

- Campos: 20
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_CodEmp | Number(004,0) | Não | Código da empresa |
| USU_CodOri | String(003) | Não | Código da Origem do Produto |
| USU_NumOrp | Number(009,0) | Não | Número da OP/OS |
| USU_CodEtg | Number(004,0) | Não | Estagio da OP |
| USU_SeqRot | Number(004,0) | Não | Seq. do Roteiro |
| USU_QtdApt | Number(013,4) | Sim | Quantidade Apontada |
| USU_CodUsu | Number(010,0) | Sim | Codigo do Usuario |
| USU_DatMov | Date | Não | Data da movimentação da OP |
| USU_HorMov | Time | Não | Hora do Movimento da OP |
| USU_IndApt | String(001) | Sim | Indicativo se Apontou a OP |
| USU_DatEnv | Date | Sim | Data do Ultimo Envio de E-mail |
| USU_HorEnv | Time | Sim | Hora do Envio do Ultimo Email |
| USU_DesErr | String(1000) | Sim | Descricao do Erro do Apontamento |
| USU_NumCad | Number(009,0) | Sim | Cadastro do Operador |
| USU_SeqApt | Number(004,0) | Não | Sequencia do Apontamento |
| USU_CCuDev | String(999) | Sim | Centro de Custo Devedor |
| USU_QtdRfg | Number(013,4) | Sim | Quantidade Refugada |
| USU_CodFil | Number(005,0) | Sim | Código da filial |
| USU_codpro | String(014) | Sim | Cod Produto |
| USU_CodDer | String(007) | Sim | Código da derivação |

---

## Chave Primária

- USU_CodEmp
- USU_CodOri
- USU_NumOrp
- USU_CodEtg
- USU_SeqRot
- USU_DatMov
- USU_HorMov
- USU_SeqApt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
