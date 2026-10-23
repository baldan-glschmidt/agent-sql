# R142DCU

## Descrição

Diagnósticos Treinamento - Cursos Aperfeiçoamento

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDia | Number(009,0) | Não | Código do Diagnóstico |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| CmpCua | Date | Não | Competência do Curso |
| CodOem | Number(008,0) | Não | Código da Entidade |

---

## Chave Primária

- CodDia
- CodCua
- CmpCua
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R142DCU_000

**Tabela:** R142DIA

| Origem | Destino |
|--------|---------|
| CodDia | CodDia |

### IR_R142DCU_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R142DCU_003

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

