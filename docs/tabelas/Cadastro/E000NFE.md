# E000NFE

## Descrição

Tabelas - Integrações - Notas fiscais de entrada

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |

---

## Chave Primária

- SeqInt

---

## Índices

### E000NFEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
