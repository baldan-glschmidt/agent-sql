# R112ITR

## Descrição

Itens de Questionário - Respostas

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodItq | Number(003,0) | Não | Código da Pergunta do Questionário |
| CodRsp | Number(003,0) | Não | Código da Resposta |
| DesRsp | String(200) | Sim | Descrição Resposta |
| IdeItq | String(001) | Sim | Mostrar esta resposta na ficha e no atendimento |
| RspPad | String(001) | Sim | Identifica a resposta padrão |
| CodSun | Number(006,0) | Sim | Código da subnormalidade |
| CodDef | Number(002,0) | Sim | Código da Deficiência |
| PreDat | Number(001,0) | Sim | Preenchimento Data |

---

## Chave Primária

- CodItq
- CodRsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R112ITR_000

**Tabela:** R112ITE

| Origem | Destino |
|--------|---------|
| CodItq | CodItq |

