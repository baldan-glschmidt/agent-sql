# E001RAT

## Descrição

Tabelas - Transações - Rateios

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da Transação |
| SeqRat | Number(009,0) | Não | Sequência de rateio |
| TipRsc | String(001) | Não | Tipo de rateio (composto, por conta, por c.custo, por projeto) |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| NumPrj | Number(008,0) | Sim | Número interno do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| PerCta | Number(007,4) | Sim | Percentual a ser rateado para a conta |
| CodCcu | String(009) | Sim | Código do centro de custo |
| PerRat | Number(007,4) | Sim | Percentual a ser rateado para o centro de custos |

---

## Chave Primária

- CodEmp
- CodTns
- SeqRat

---

## Índices

### E001RATIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns
- CtaFin

### E001RATIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns
- CtaRed

### E001RATIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns
- CodCcu

---

## Relacionamentos

### IR_E001RAT_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

