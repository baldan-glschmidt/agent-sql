# R127FCU

## Descrição

Custos por Fases Curso de Formação - Geral

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NivCuf | Number(002,0) | Não | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Não | Sequência do Nível |
| FasCuf | String(003) | Não | Fase do Curso de Formação |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodFlt | Number(003,0) | Sim | Código da Regra |
| ComCus | String(200) | Sim | Comentário |

---

## Chave Primária

- NivCuf
- SeqNiv
- FasCuf
- CodOem
- CmpCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127FCU_002

**Tabela:** R127FAS

| Origem | Destino |
|--------|---------|
| NivCuf | NivCuf |
| SeqNiv | SeqNiv |
| FasCuf | FasCuf |

### IR_R127FCU_003

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

