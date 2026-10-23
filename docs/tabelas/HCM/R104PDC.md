# R104PDC

## Descrição

JR - Definição do Cenário

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatCen | Date | Não | Data do cenário |
| SeqCen | Number(002,0) | Não | Sequência do cenário |
| DesCen | String(040) | Sim | Descrição do cenário do pedido |
| TipCen | Number(001,0) | Sim | Tipo do cenário (Original, Simulado, Proposta Acordo, Sentença ou Execução) |
| CodCom | Number(004,0) | Sim | Código da vara |
| GrpInc | Number(003,0) | Sim | Código da tabela de Incidência |
| CenPrv | String(001) | Sim | Define o cenário a ser provisionado |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104PDC_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

