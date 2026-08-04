# E027NOP

## Descrição

Ligação entre NBS/IndOp para NFS-e

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeNbs | Number(009,0) | Sim | Identificador NBS |
| CodIop | String(006) | Não | Código indicador da operação de fornecimento para NFS-e |
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| TplPsf | Number(001,0) | Sim | Tipo de local da prestação para serviços prestados fisicamente |
| CodNbs | String(015) | Sim | Nomenclatura brasileira de seviços, intangíveis e outras operações |

---

## Chave Primária

- IdeUni

---

## Índices

### E027NOP_UK

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodNbs
- CodIop

### E027NOPIndice1

**Tipo:** Não unico

Campos:
- CodNbs

### E027NOPIndice2

**Tipo:** Não unico

Campos:
- CodIop

---

## Relacionamentos

Nenhum relacionamento cadastrado.
