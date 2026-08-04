# E000MCP

## Descrição

Tabelas - Integrações - Títulos a Pagar - Movimentações

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
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial da pendência |
| NumTit | String(015) | Não | Número do título a pagar |
| CodTpt | String(003) | Não | Código do tipo do título a pagar |
| CodFor | Number(009,0) | Não | Código do fornecedor do título a pagar |
| SeqMov | Number(004,0) | Não | Sequência do movimento do título a pagar |
| FilTit | Number(005,0) | Sim | Código da filial do título |

---

## Chave Primária

- SeqInt

---

## Índices

### E000MCPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodFor
- CodTpt
- NumTit
- SeqMov
- FilTit

---

## Relacionamentos

Nenhum relacionamento cadastrado.
