# R182GQO

## Descrição

PLR - Grupos de Questionários do Objetivo

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodObj | Number(004,0) | Não | Código do Objetivo |
| CodGrp | Number(006,0) | Não | Código do Grupo |

---

## Chave Primária

- CodObj
- CodGrp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R182GQO_000

**Tabela:** R182OBJ

| Origem | Destino |
|--------|---------|
| CodObj | CodObj |

### IR_R182GQO_001

**Tabela:** R182GRP

| Origem | Destino |
|--------|---------|
| CodGrp | CodGrp |

