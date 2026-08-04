# E039RAT

## Descrição

Cadastros - Portadores - Rateios

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPor | String(004) | Não | Código do portador |
| CodFil | Number(005,0) | Não | Código da filial |
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

- CodEmp
- CodPor
- CodFil
- SeqRat

---

## Índices

### E039RATIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodPor
- CodFil
- CtaFin

### E039RATIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodPor
- CodFil
- CtaRed

### E039RATIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- CodPor
- CodFil
- CodCcu

---

## Relacionamentos

### IR_E039RAT_002

**Tabela:** E039HPO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPor | CodPor |
| CodFil | CodFil |

