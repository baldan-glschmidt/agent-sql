# E000CXU

## Descrição

Tabelas - Integrações - Ligação Categoria Produto x Usuarios

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
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodUsu | Number(010,0) | Não | Código do usuário |
| IdeCat | String(050) | Não | Identificador único da Categoria de Produtos |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CXUIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodUsu
- IdeCat

---

## Relacionamentos

Nenhum relacionamento cadastrado.
