# R032FAS

## Descrição

Outras Empresas - Assuntos de Cursos

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
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| CodAss | Number(004,0) | Não | Código do Assunto de Curso |

---

## Chave Primária

- CodOem
- CodAss

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032FAS_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

### IR_R032FAS_001

**Tabela:** R128ASS

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |

