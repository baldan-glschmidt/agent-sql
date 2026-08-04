# E900CMI

## Descrição

O.P./O.S. - Componentes Utilizados Individualmente (Rastreabilidade Lote/Série)

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Origem do produto/serviço fabricado na OP/OS |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| CodEtg | Number(004,0) | Não | Código do estágio de produção |
| SeqCmp | Number(004,0) | Não | Sequência do componente utilizado |
| SeqCmi | Number(004,0) | Não | Sequência do componente utilizado individualmente |
| CodCmp | String(014) | Não | Código do componente utilizado |
| CodDer | String(007) | Não | Código da derivação do componente utilizado |
| SeqCmr | Number(004,0) | Sim | Sequência do agrupamento |
| CodLot | String(050) | Sim | Código do lote de fabricação do componente |
| NumSep | String(050) | Sim | Número de série de fabricação do componente |
| QtdUti | Number(014,5) | Sim | Quantidade real utilizada |
| IndCmi | String(001) | Não | Indicativo do componente (aberto ou fechado) |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqCmp
- SeqCmi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900CMI_004

**Tabela:** E900CMO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |
| CodEtg | CodEtg |
| SeqCmp | SeqCmp |

### IR_E900CMI_006

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCmp | CodPro |

