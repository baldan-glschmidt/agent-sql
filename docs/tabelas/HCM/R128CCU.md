# R128CCU

## Descrição

Custos por Cursos de Aperfeiçoamento - Geral

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
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodFlt | Number(003,0) | Sim | Código da Regra |
| ComCus | String(200) | Sim | Comentário |

---

## Chave Primária

- CodCua
- CodOem
- CmpCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128CCU_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128CCU_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

