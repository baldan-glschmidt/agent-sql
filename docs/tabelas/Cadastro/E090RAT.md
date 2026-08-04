# E090RAT

## Descrição

Cadastros - Representantes - Rateios

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
| CodRep | Number(009,0) | Não | Código do representante |
| CodEmp | Number(004,0) | Não | Código da empresa |
| SeqRat | Number(009,0) | Não | Sequência de rateio |
| TipRsc | String(001) | Não | Tipo de rateio (composto,por conta, por c.custo, por projeto) |
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

- CodRep
- CodEmp
- SeqRat

---

## Índices

### E090RATIndice2

**Tipo:** Não unico

Campos:
- CodRep
- CodEmp
- CtaFin

### E090RATIndice3

**Tipo:** Não unico

Campos:
- CodRep
- CodEmp
- CtaRed

### E090RATIndice4

**Tipo:** Não unico

Campos:
- CodRep
- CodEmp
- CodCcu

---

## Relacionamentos

### IR_E090RAT_001

**Tabela:** E090HRP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |
| CodEmp | CodEmp |

