# R122CRQ

## Descrição

Candidatos Externos - Resposta Questionário

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Código do Candidato |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodGrq | Number(003,0) | Não | Código do Grupo |
| CodItq | Number(003,0) | Não | Código do Item do Questionário |
| CodRsp | Number(003,0) | Sim | Código da Resposta |
| CodOem | Number(008,0) | Sim | Código do Cliente Agência de Empregos |
| AnoRsp | String(2000) | Sim | Anotações da Resposta |

---

## Chave Primária

- NumCan
- EstCar
- CodGrq
- CodItq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CRQ_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CRQ_003

**Tabela:** R118GRI

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodGrq | CodGrq |
| CodItq | CodItq |

### IR_R122CRQ_004

**Tabela:** R118ITR

| Origem | Destino |
|--------|---------|
| CodItq | CodItq |
| CodRsp | CodRsp |

