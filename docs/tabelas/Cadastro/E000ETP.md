# E000ETP

## Descrição

Tabelas - Integrações - Exclusão de Títulos a Pagar

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
| NumTit | String(015) | Não | Número do título a pagar |
| CodTpt | String(003) | Não | Código de Tipo de Título |
| CodFor | Number(009,0) | Não | Código do Fornecedor |

---

## Chave Primária

- SeqInt

---

## Índices

### E000ETPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumTit
- CodTpt
- CodFor

---

## Relacionamentos

Nenhum relacionamento cadastrado.
