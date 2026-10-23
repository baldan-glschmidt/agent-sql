# R530AGR

## Descrição

Grupo de Requisitos - Cargos e Postos

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruReq | String(010) | Não | Código do grupo de requisitos |
| SeqIte | Number(008,0) | Não | Sequência do Cargo ou Posto |
| TipIte | Number(001,0) | Sim | Tipo do item |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Cargo vinculado ao Grupo |
| EstPos | Number(003,0) | Sim | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Sim | Posto de trabalho vinculado ao Grupo |
| DatIni | Date | Sim | Data de início da validade |
| DatTer | Date | Sim | Data de término da validade |

---

## Chave Primária

- GruReq
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R530AGR_000

**Tabela:** R530GRQ

| Origem | Destino |
|--------|---------|
| GruReq | GruReq |

