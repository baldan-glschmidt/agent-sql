# E900APT

## Descrição

Apontamentos originados da plataforma Senior X

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeUsx | Number(009,0) | Não | Identificador único do apontamento na plataforma Senior X |
| TipApt | String(001) | Não | Tipo do apontamento realizado |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| CodEtg | Number(004,0) | Não | Código do Estágio Produção (Etapas na Fabricação de um Produto) |
| CodCre | String(008) | Sim | Código do Centro de Recurso (conjunto Máquina/Pessoa c/ mesma capacidade produtiva) |
| CodOpr | String(006) | Sim | Código da operação |
| SeqOpr | Number(004,0) | Sim | Sequência operacional |
| CodOpe | Number(009,0) | Sim | Código do operador |
| DatApt | Date | Não | Data do apontamento |
| HorApt | Number(005,0) | Não | Hora do apontamento |
| GerEst | String(001) | Sim | Indicativo se o apontamento gera estoque |
| SeqCmp | Number(004,0) | Sim | Sequência do Componente na utilização |
| CodMtv | String(004) | Sim | Código do motivo de parada |
| Aux001 | String(050) | Sim | Auxiliar 001 |
| Aux002 | String(050) | Sim | Auxiliar 002 |

---

## Chave Primária

- IdeUni

---

## Índices

### E900APTIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- IdeUsx

---

## Relacionamentos

### IR_E900APT_006

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

