# E900IRS

## Descrição

O.P./O.S. - Informações para Remessa/Retorno de Serviço de Terceiros

---

## Resumo

- Campos: 20
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção da O.P./O.S. |
| SeqRot | Number(004,0) | Não | Sequência lógica da Operação no Roteiro de Produção |
| RemSer | String(001) | Não | É remessa ou retorno de serviço?? (Remessa - RemSer='S', Retorno - RemSer='N') |
| CodPro | String(014) | Sim | Código do Produto/Serviço |
| CodFor | Number(009,0) | Sim | Código do Fornecedor do Serviço |
| CodSer | String(014) | Sim | Código do serviço solicitado |
| DatGer | Date | Não | Data da Geração do Registro |
| HorGer | Number(005,0) | Sim | Hora da Geração do Registro |
| CodUsu | Number(010,0) | Sim | Código do Usuário que gerou o registro |
| QtdRfg | Number(014,5) | Sim | Quantidade de Refugo |
| QtdRe1 | Number(014,5) | Sim | Quantidade real de 1ª qualidade no Estágio |
| QtdRe2 | Number(014,5) | Sim | Quantidade real de 2ª qualidade no Estágio |
| QtdRe3 | Number(014,5) | Sim | Quantidade real de 3ª qualidade no Estágio |
| StsPro | String(001) | Sim | Status do Processo |
| RemFil | String(001) | Sim | Indica que a remessa foi feita para que a operação seja executada em outra filial |
| FilOri | Number(005,0) | Sim | Código da filial de origem da remessa |
| FilDes | Number(005,0) | Sim | Código da filial de destino da remessa |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqRot
- RemSer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900IRS_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900IRS_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

