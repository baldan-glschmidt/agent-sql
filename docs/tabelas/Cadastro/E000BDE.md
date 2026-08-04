# E000BDE

## Descrição

Tabelas - Integrações - Log bloqueio/desbloqueio de estoque via WMS

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeReg | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| IdeWms | Number(009,0) | Não | Identificador de ligação com a tabela do WMS |
| TipOpe | String(001) | Sim | Indicativo se a operação é de bloqueio ou desbloqueio |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodDep | String(010) | Sim | Código do depósito |
| QtdBde | Number(012,3) | Sim | Quantidade utilizada na operação de bloqueio/desbloqueio |
| CodLot | String(050) | Sim | Código do lote de fabricação do produto |
| NumSep | String(050) | Sim | Número de série do produto |
| SitOpe | String(001) | Sim | Situação da operação de bloqueio/desbloqueio de estoque |
| MsgRet | String(3999) | Sim | Mensagem de retorno do processamento da operação de bloqueio/desbloqueio |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeReg

---

## Índices

### E000BDEIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- IdeWms

---

## Relacionamentos

Nenhum relacionamento cadastrado.
