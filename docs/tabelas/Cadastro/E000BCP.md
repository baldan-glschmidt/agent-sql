# E000BCP

## Descrição

Tabelas - Integrações - Títulos a Pagar - Baixas por compensação

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial da pendência |
| NumTit | String(015) | Não | Número do título a pagar |
| CodTpt | String(003) | Não | Código de Tipo de Título a pagar |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| SeqMov | Number(004,0) | Não | Sequência de movimento do título |
| TipPen | String(001) | Não | Tipo da pendência de exportação |
| FilTit | Number(005,0) | Sim | Código da filial do título |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000BCPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumTit
- CodTpt
- CodFor
- SeqMov
- TipPen
- FilTit

### E000BCPIndice2

**Tipo:** Não unico

Campos:
- IdeUni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
