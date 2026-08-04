# E900CMR

## Descrição

O.P./O.S. - Agrupamento Componentes Utilizados Individualmente (Rastreabilidade Lote/Série)

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
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
| SeqCmr | Number(004,0) | Não | Sequência do agrupamento |
| CodRef | String(020) | Sim | Código de referência diverso |
| CodAgp | String(005) | Sim | Código de agrupamento de materiais/produtos para produção |
| IndCmr | String(001) | Sim | Indicativo do agrupamento (aberto, fechado ou utilizado) |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqCmr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900CMR_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900CMR_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

