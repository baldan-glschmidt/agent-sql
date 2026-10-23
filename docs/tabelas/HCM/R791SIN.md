# R791SIN

## Descrição

Central alertas - Sindicato - Vencimento de Data Base

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(005,0) | Não | Código do sindicato |
| NomSin | String(060) | Não | Nome do sindicato |
| MesDis | Number(002,0) | Não | Mês da data base do sindicato (1-12) |
| InsLev | Number(001,0) | Não | Nível de severidade da ocorrência |
| DatGer | Date | Não | Data de geração do registro |

---

## Chave Primária

- CodSin

---

## Índices

### R791SINIndice1

**Tipo:** Não unico

Campos:
- InsLev

---

## Relacionamentos

Nenhum relacionamento cadastrado.
