# R530GRQ

## Descrição

Grupo de Requisitos - Cadastro

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruReq | String(010) | Não | Código do grupo de requisitos |
| DesGRq | String(200) | Sim | Descrição do grupo de requisitos. |
| PrfReq | Number(004,0) | Sim | Indica qual será a utilização do grupo de requisitos |
| ObjGRq | String(2000) | Sim | Objetivo do grupo de requisitos |
| CodUsu | Number(009,0) | Sim | Usuário responsável pela última modificação do grupo |
| DthMod | Number(014,6) | Sim | Data/Hora da última alteração do grupo |

---

## Chave Primária

- GruReq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R530GRQ_002

**Tabela:** R530PRF

| Origem | Destino |
|--------|---------|
| PrfReq | PrfReq |

