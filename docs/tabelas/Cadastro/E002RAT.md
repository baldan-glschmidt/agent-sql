# E002RAT

## Descrição

Tabelas - Tipos de Título - Rateios

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTpt | String(003) | Não | Código interno do tipo de título |
| CodEmp | Number(004,0) | Não | Código da empresa |
| SeqRat | Number(009,0) | Não | Sequência de rateio |
| TipRsc | String(001) | Não | Tipo de rateio (composto, por conta, por c.custo, por projeto) |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| NumPrj | Number(008,0) | Sim | Número interno do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| PerCta | Number(007,4) | Sim | Percentual a ser rateado para a conta |
| CodCcu | String(009) | Sim | Código do centro de custos |
| PerRat | Number(007,4) | Sim | Percentual a ser rateado para o centro de custos |

---

## Chave Primária

- CodTpt
- CodEmp
- SeqRat

---

## Índices

### E002RATIndice2

**Tipo:** Não unico

Campos:
- CodTpt
- CodEmp
- CtaFin

### E002RATIndice3

**Tipo:** Não unico

Campos:
- CodTpt
- CodEmp
- CtaRed

### E002RATIndice4

**Tipo:** Não unico

Campos:
- CodTpt
- CodEmp
- CodCcu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
