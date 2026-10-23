# R235REC

## Descrição

Recursos de compromissos

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRec | Number(010,0) | Não | Código do recurso |
| TipRec | Number(001,0) | Sim | Tipo do recurso |
| CodSla | Number(004,0) | Sim | Código da sala |
| CodPes | Number(009,0) | Sim | Código da Pessoa |
| CodRei | Number(004,0) | Sim | Código do Recurso Instrucional |
| NomRei | String(060) | Sim | Nome do recurso |

---

## Chave Primária

- CodRec

---

## Índices

### R235RECIndice1

**Tipo:** Não unico

Campos:
- CodSla

### R235RECIndice2

**Tipo:** Não unico

Campos:
- CodPes

### R235RECIndice3

**Tipo:** Não unico

Campos:
- CodRei

---

## Relacionamentos

Nenhum relacionamento cadastrado.
