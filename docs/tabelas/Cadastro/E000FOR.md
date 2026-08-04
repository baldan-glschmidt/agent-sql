# E000FOR

## Descrição

Tabelas - Integrações - Fornecedores

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor |

---

## Chave Primária

- SeqInt

---

## Índices

### E000FORIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodFor

### E000FOREmpresaFilial

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
