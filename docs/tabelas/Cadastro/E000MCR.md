# E000MCR

## Descrição

Tabelas - Integrações - Títulos a Receber - Movimentações

---

## Resumo

- Campos: 9
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
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código do tipo de título a receber |
| SeqMov | Number(004,0) | Não | Sequência de movimento do título |
| TipPen | String(001) | Não | Tipo da pendência de exportação |
| FilTit | Number(005,0) | Sim | Código da filial do título |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000MCRIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumTit
- CodTpt
- SeqMov
- TipPen
- FilTit

### E000MCRIndice2

**Tipo:** Não unico

Campos:
- IdeUni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
