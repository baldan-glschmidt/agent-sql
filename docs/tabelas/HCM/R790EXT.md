# R790EXT

## Descrição

Ligação de usuário G5 com usuário G7

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de Registro |
| CodUsu | Number(010,0) | Sim | Código do usuário |
| UsuHCM | String(100) | Sim | Usuário G6 |
| Apptk6 | String(2000) | Sim | Usuário G6 |
| UsuPlt | String(100) | Sim | Usuário G7 |
| Apptkn | String(2000) | Sim | Token G7 |
| XtdDef | Number(009,0) | Sim | Definições XTended |
| DatDef | Date | Sim | Data definições XTended |

---

## Chave Primária

- IdeUni

---

## Índices

### R970EXTIndice1

**Tipo:** Unico

Campos:
- UsuHCM
- UsuPlt

### R970EXTIndice2

**Tipo:** Unico

Campos:
- UsuHCM

---

## Relacionamentos

Nenhum relacionamento cadastrado.
