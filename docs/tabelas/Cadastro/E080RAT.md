# E080RAT

## Descrição

Cadastros - Serviços - Rateios

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
| CodSer | String(014) | Não | Código do serviço |
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

- CodEmp
- CodSer
- SeqRat

---

## Índices

### E080RATIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodSer
- CtaFin

### E080RATIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodSer
- CtaRed

### E080RATIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- CodSer
- CodCcu

---

## Relacionamentos

### IR_E080RAT_001

**Tabela:** E080SER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodSer | CodSer |

