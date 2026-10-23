# R101BLO

## Descrição

Ciclos - Classificação de Objetivos - Blocos

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo da avaliação |
| CodCla | Number(004,0) | Não | Código da classe de objetivos |
| CodBlo | Number(004,0) | Não | Código do Bloco |
| DesBlo | String(040) | Sim | Descrição do Bloco do Objetivo |
| QtdMin | Number(003,0) | Sim | Define a quantidade mínima de Blocos |
| QtdMax | Number(003,0) | Sim | Define a quantidade máxima de Blocos |

---

## Chave Primária

- CodCic
- TipAva
- CodCla
- CodBlo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101BLO_002

**Tabela:** R101CLA

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |
| TipAva | TipAva |
| CodCla | CodCla |

