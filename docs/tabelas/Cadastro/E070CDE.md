# E070CDE

## Descrição

Cadastros - Filiais - Dependências

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodDep | String(015) | Não | Código da dependência |
| DesDep | String(100) | Não | Descrição da dependência |
| InsMun | String(016) | Sim | Inscrição municipal |
| NumCgc | Number(014,0) | Sim | Número do cadastro nacional de pessoa jurídica |
| DocIdeDep | String(014) | Sim | Número do cadastro nacional de pessoa jurídica |
| TipDep | Number(002,0) | Sim | Tipo dependência DESIF |
| EndDep | String(100) | Sim | Endereço completo da dependência |
| IniAti | Date | Sim | Início da atividade |
| FimAti | Date | Sim | Fim da atividade |

---

## Chave Primária

- CodEmp
- CodFil
- CodDep

---

## Índices

### E070CDE_FKIndex1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
