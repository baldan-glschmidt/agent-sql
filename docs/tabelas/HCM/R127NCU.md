# R127NCU

## Descrição

Custos por Nível Curso de Formação - Geral

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NivCuf | Number(002,0) | Não | Nível de Formação do Curso |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodFlt | Number(003,0) | Sim | Código da Regra |
| ComCus | String(200) | Sim | Comentário |

---

## Chave Primária

- NivCuf
- CodOem
- CmpCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127NCU_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

