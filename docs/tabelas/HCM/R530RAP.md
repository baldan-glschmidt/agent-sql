# R530RAP

## Descrição

Grupo de Requisitos - Aperfeiçoamento

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruReq | String(010) | Não | Código do grupo de requisitos |
| RevGRq | String(010) | Não | Revisão do grupo de requisitos |
| CodCua | Number(009,0) | Não | Curso de Aperfeiçoamento que é requisito para esta revisão |
| ExiRqu | String(001) | Sim | Exigência do requisito |
| PtsReq | Number(008,4) | Sim | Pontuação do requisito |

---

## Chave Primária

- GruReq
- RevGRq
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R530RAP_001

**Tabela:** R530REV

| Origem | Destino |
|--------|---------|
| GruReq | GruReq |
| RevGRq | RevGRq |

### IR_R530RAP_002

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

