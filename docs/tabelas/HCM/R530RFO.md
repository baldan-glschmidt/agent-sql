# R530RFO

## Descrição

Grupo de Requisitos - Formação

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruReq | String(010) | Não | Código do grupo de requisitos |
| RevGRq | String(010) | Não | Revisão do grupo de requisitos |
| CodCuf | Number(004,0) | Não | Curso de Formação que é requisito para esta revisão |
| SitCuf | Number(001,0) | Sim | Indica a situação requisitada para o curso |
| ExiRqu | String(001) | Sim | Exigência do requisito |
| PtsReq | Number(008,4) | Sim | Pontuação do requisito de formação |

---

## Chave Primária

- GruReq
- RevGRq
- CodCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R530RFO_001

**Tabela:** R530REV

| Origem | Destino |
|--------|---------|
| GruReq | GruReq |
| RevGRq | RevGRq |

### IR_R530RFO_002

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

