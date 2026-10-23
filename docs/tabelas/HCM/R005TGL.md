# R005TGL

## Descrição

Terminais do Grupo de Localização

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
| CodGLo | Number(002,0) | Não | Grupo de Localização |
| CodTrm | Number(002,0) | Não | Terminal |

---

## Chave Primária

- CodGLo
- CodTrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005TGL_000

**Tabela:** R005GLO

| Origem | Destino |
|--------|---------|
| CodGLo | CodGLo |

### IR_R005TGL_001

**Tabela:** R005TRM

| Origem | Destino |
|--------|---------|
| CodTrm | CodTrm |

