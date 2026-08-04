# E440EXS

## Descrição

Compras - Ligação entre nota de entrada e nota de saída

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqExs | Number(004,0) | Não | Sequencia da ligação |
| EmpRlc | Number(004,0) | Não | Empresa da nota fiscal de saída relacionada |
| FilRlc | Number(005,0) | Não | Filial da nota fiscal de saída relacionada |
| NfvRlc | Number(009,0) | Não | Número da nota fiscal de saída relacionada |
| SnfRlc | String(003) | Não | Código da série da nota fiscal de saída relacionada |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqExs

---

## Índices

### E440EXSIndice2

**Tipo:** Não unico

Campos:
- EmpRlc
- FilRlc
- NfvRlc
- SnfRlc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
