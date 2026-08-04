# E900LRR

## Descrição

Leitura de OP's para Remessa e Retorno de Serviço de Terceiros

---

## Resumo

- Campos: 11
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
| StaReg | String(001) | Sim | Status da Registro |
| CodUsu | Number(010,0) | Sim | Código do Usuário que gerou o registro |

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

### IR_E900LRR_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900LRR_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

