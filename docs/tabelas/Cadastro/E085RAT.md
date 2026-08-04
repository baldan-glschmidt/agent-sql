# E085RAT

## Descrição

Cadastros - Clientes - Rateios

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
| CodCli | Number(009,0) | Não | Código do cliente |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
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

- CodCli
- CodEmp
- CodFil
- SeqRat

---

## Índices

### E085RATIndice2

**Tipo:** Não unico

Campos:
- CodCli
- CodEmp
- CodFil
- CtaFin

### E085RATIndice3

**Tipo:** Não unico

Campos:
- CodCli
- CodEmp
- CodFil
- CtaRed

### E085RATIndice4

**Tipo:** Não unico

Campos:
- CodCli
- CodEmp
- CodFil
- CodCcu

---

## Relacionamentos

### IR_E085RAT_002

**Tabela:** E085HCL

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |
| CodEmp | CodEmp |
| CodFil | CodFil |

