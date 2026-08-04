# E055HSF

## Descrição

Cadastros - Histórico de alterações do serviço

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
| IdeHsf | Number(009,0) | Não | Identificador do registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodSer | String(014) | Não | Código do serviço |
| PerFim | Date | Não | Período final |
| TipHsf | String(001) | Não | Tipo alteração |
| CodIte | String(060) | Sim | Código fiscal do item |
| DesIte | String(255) | Sim | Descrição fiscal do item |

---

## Chave Primária

- IdeHsf

---

## Índices

### E055HSFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodSer
- PerFim
- TipHsf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
