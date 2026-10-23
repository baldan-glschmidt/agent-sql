# R940LNG

## Descrição

Cadastro de Idiomas

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| LngKey | Number(005,0) | Não | Chave do idioma |
| LngCod | String(005) | Não | Código do idioma |
| LngNam | String(255) | Não | Nome do idioma |
| CurFmt | Number(002,0) | Sim | Regra para formato de moeda por extenso |
| CurNam | String(255) | Sim | Nome da moeda |
| CurNmP | String(255) | Sim | Nome da moeda no plural |
| CurFNm | String(255) | Sim | Nome da fração de moeda |
| CurFNP | String(255) | Sim | Nome da fração de moeda no plural |
| NumSep | String(010) | Sim | Separadores Numéricos |

---

## Chave Primária

- LngKey

---

## Índices

### R940LNGLngCod

**Tipo:** Unico

Campos:
- LngCod

---

## Relacionamentos

Nenhum relacionamento cadastrado.
