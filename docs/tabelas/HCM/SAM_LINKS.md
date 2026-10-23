# SAM_LINKS

## Descrição

SAM Links

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 9
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| UUID | String(032) | Não | Universally Unique Identifier |
| TipoIdSAM | Number(002,0) | Sim | Tipo ID SAM |
| TipoIdBase | Number(002,0) | Sim | Tipo ID Base |
| IdtPes | String(023) | Sim | Identificador da Pessoa |
| IdSAM | Number(009,0) | Sim | ID SAM |
| IdG5 | Number(009,0) | Sim | G5_ID |
| Long1 | Number(012,0) | Sim | Long1 |
| Long2 | Number(012,0) | Sim | Long2 |
| Date1 | Date | Sim | Data1 |
| Date2 | Date | Sim | Data2 |
| Int1 | Number(009,0) | Sim | Int1 |
| Int2 | Number(009,0) | Sim | Int2 |
| Int3 | Number(009,0) | Sim | Int3 |
| Int4 | Number(009,0) | Sim | Int4 |
| String1 | String(255) | Sim | String 1 |
| String2 | String(255) | Sim | String 2 |

---

## Chave Primária

- UUID

---

## Índices

### SAMLinksIndice1

**Tipo:** Não unico

Campos:
- TipoIdSAM
- IdSAM

### SAMLinksIndice2

**Tipo:** Não unico

Campos:
- TipoIdBase
- IdtPes

### SAMLinksIndice3

**Tipo:** Não unico

Campos:
- IdtPes

### SAMLinksIndice4

**Tipo:** Não unico

Campos:
- TipoIdBase
- IdtPes
- Date1
- Date2

### SAMLinksIndice5

**Tipo:** Não unico

Campos:
- TipoIdBase
- IdtPes
- Int1
- Int2

### SAMLinksIndice6

**Tipo:** Não unico

Campos:
- TipoIdBase
- IdtPes
- Date1
- Int1
- Date2
- Int2

### SAMLinksIndice7

**Tipo:** Não unico

Campos:
- TipoIdBase
- Int1
- Int2

### SAMLinksIndice8

**Tipo:** Não unico

Campos:
- TipoIdBase
- String1
- String2

### SAMLinksIndice9

**Tipo:** Não unico

Campos:
- TipoIdBase
- IdG5

---

## Relacionamentos

Nenhum relacionamento cadastrado.
