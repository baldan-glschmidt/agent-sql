# E000TCP

## Descrição

Tabelas - Integrações - Títulos a Pagar

---

## Resumo

- Campos: 7
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
| NumTit | String(015) | Não | Número do título a pagar |
| CodTpt | String(003) | Não | Código do tipo do título a pagar |
| CodFor | Number(009,0) | Não | Código do fornecedor do título a pagar |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000TCPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodFor
- CodTpt
- NumTit

### E000TCPIndice2

**Tipo:** Não unico

Campos:
- IdeUni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
