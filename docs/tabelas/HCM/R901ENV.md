# R901ENV

## Descrição

LGPD - Campos de Informações de Envolvidos no Dossiê

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumSec | Number(014,0) | Não | Número interno |
| TipEnv | Number(001,0) | Não | Tipo do campo, ref. aos envolvidos no dossiê |
| DesEnv | String(030) | Sim | Descrição do campo, ref. aos envolvidos no dossiê |
| ConEnv | String(100) | Sim | Conteúdo do campo, ref. aos envolvidos no dossiê |

---

## Chave Primária

- NumSec
- TipEnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
