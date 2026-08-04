# E020SCO

## Descrição

Cadastros - Relacionamento entre série origem e destino

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| EmpOri | Number(004,0) | Não | Código da empresa |
| FilOri | Number(005,0) | Não | Código da filial |
| SnfOri | String(003) | Não | Código da série da nota fiscal |
| EmpDes | Number(004,0) | Não | Código da empresa |
| FilDes | Number(005,0) | Não | Código da filial |
| SnfDes | String(003) | Não | Código da série da nota fiscal |

---

## Chave Primária

- IdeUni

---

## Índices

### E020SCOIndex2

**Tipo:** Unico

Campos:
- EmpOri
- FilOri
- SnfOri
- EmpDes
- FilDes
- SnfDes

---

## Relacionamentos

Nenhum relacionamento cadastrado.
