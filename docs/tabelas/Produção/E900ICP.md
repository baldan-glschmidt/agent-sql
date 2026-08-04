# E900ICP

## Descrição

OP - Incorporação Produtos

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Código da origem do produto/serviço fabricado na OP |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| SeqIcp | Number(004,0) | Não | Sequência da incorporação de produto na OP |
| CodEtg | Number(004,0) | Não | Estágio onde ocorreu a incorporação do produto |
| SeqRot | Number(004,0) | Não | Sequência de roteiro onde ocorreu a incorporação do produto |
| CodPro | String(014) | Não | Código do produto incorporado |
| CodDer | String(007) | Sim | Código da derivação do produto incorporado |
| CodDep | String(010) | Não | Código do depósito origem do produto incorporado |
| CodLot | String(050) | Sim | Código do lote do produto incorporado |
| NumSep | String(050) | Sim | Número de série do produto incorporado |
| UniMed | String(003) | Não | Unidade de medida do produto incorporado |
| QtdIcp | Number(014,5) | Sim | Quantidade de produto incorporada |
| QtdCnv | Number(014,5) | Sim | Quantidade incorporada convertida na unidade de medida do produto final da OP |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- SeqIcp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900ICP_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

