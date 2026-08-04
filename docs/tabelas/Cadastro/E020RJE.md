# E020RJE

## Descrição

Cadastros - Relacionamento série do ERP X JDE

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SerOri | String(003) | Não | Código da série da nota fiscal |
| SerDes | String(003) | Não | Código da série da nota fiscal |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E020RJEIndex2

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- SerOri
- SerDes

---

## Relacionamentos

Nenhum relacionamento cadastrado.
