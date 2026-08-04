# E066DVP

## Descrição

Integrações - Varejo - Desconto por valor de parcela

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFpg | Number(002,0) | Não | Código da forma de pagamento |
| VlrIni | Number(015,2) | Sim | Valor inicial da parcela |
| VlrFim | Number(015,2) | Sim | Valor final da parcela |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |

---

## Chave Primária

- IdeUni

---

## Índices

### E066DVPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodFpg
- VlrIni
- VlrFim

---

## Relacionamentos

Nenhum relacionamento cadastrado.
