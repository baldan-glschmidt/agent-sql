# E900RCP

## Descrição

O.P./O.S. - Remessa de componentes da OP

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Código da Origem do Produto |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| CodEtg | Number(004,0) | Não | Código do Estágio Produção (Etapas na Fabricação de um Produto) |
| SeqCmp | Number(004,0) | Não | Sequência do Componente na utilização |
| SeqDls | Number(006,0) | Não | Sequência de movimento de item |
| CmpRem | String(001) | Sim | Indicativo se o componente foi remetido |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqCmp
- SeqDls

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900RCP_004

**Tabela:** E900CMO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |
| CodEtg | CodEtg |
| SeqCmp | SeqCmp |

