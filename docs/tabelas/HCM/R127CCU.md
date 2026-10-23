# R127CCU

## Descrição

Custos por Cursos de Formação - Geral

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
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodFlt | Number(003,0) | Sim | Código da Regra |
| ComCus | String(200) | Sim | Comentário |

---

## Chave Primária

- CodCuf
- CodOem
- CmpCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127CCU_000

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

### IR_R127CCU_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

