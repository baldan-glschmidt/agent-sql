# E046PCP

## Descrição

Tabelas - Visões Contábeis - Parâmetros Processados - Detalhamento

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 4
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador sequencial dos valores do cálculo da visão contábil |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodVis | String(020) | Não | Código da visão |
| IdePar | Number(009,0) | Não | Identificador sequencial dos parâmetros do cálculo da visão contábil |
| CtaVis | Number(009,0) | Não | Conta da visão |
| SeqCol | Number(003,0) | Não | Seqüência da coluna |
| SeqCmp | Number(003,0) | Não | Seqüência da composição da coluna |
| VlrCmp | Number(017,2) | Não | Valor calculado para a visão contábil |
| CtaRed | Number(007,0) | Sim | Número reduzido da conta contábil |
| CodAgl | Number(009,0) | Sim | Código da aglutinação contábil |
| VlrCre | Number(017,2) | Sim | Valor a crédito calculado pela visão contábil |
| VlrDeb | Number(017,2) | Sim | Valor a débito calculado pela visão contábil |
| NatVlr | String(001) | Sim | Natureza do Valor |
| DefGru | String(001) | Sim | Grupo que a conta pertence |

---

## Chave Primária

- IdeUni

---

## Índices

### E046PCPIndice1

**Tipo:** Não unico

Campos:
- SeqCmp
- SeqCol
- CodEmp
- CodVis
- CtaVis

### E046PCPIndice2

**Tipo:** Não unico

Campos:
- IdePar

### E046PCPIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodVis
- CtaVis

### E046PCPIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- CodVis
- SeqCol

---

## Relacionamentos

### IR_E046PCP_002

**Tabela:** E046VIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |

### IR_E046PCP_003

**Tabela:** E046PAR

| Origem | Destino |
|--------|---------|
| IdePar | IdeUni |

### IR_E046PCP_004

**Tabela:** E046PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |
| CtaVis | CtaVis |

### IR_E046PCP_005

**Tabela:** E046COL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |
| SeqCol | SeqCol |

