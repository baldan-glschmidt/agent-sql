# E055CIU

## Descrição

Cadastros - Usuários - Cadastro Ligação da Apuração Imposto x Usuário

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 4
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| CodUsu | Number(010,0) | Não | Código do Usuário |

---

## Chave Primária

- IdeUni

---

## Índices

### E055CIU_FKIndex1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

### E055CIU_FKIndex2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodImp

### E055CIU_FKIndex3

**Tipo:** Não unico

Campos:
- CodUsu

### E055CIU_Indice2

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodImp
- CodUsu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
