# E046VNE

## Descrição

Tabelas - Visões Contábeis - Notas Explicativas

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodVis | String(020) | Não | Código da visão |
| CtaVis | Number(009,0) | Não | Conta da visão |
| SeqCol | Number(003,0) | Não | Seqüência da coluna |
| SeqCmp | Number(003,0) | Não | Seqüência da composição da coluna |
| PerIni | Date | Não | Período inicial da nota explicativa para a visão contábil |
| PerFim | Date | Não | Período final da nota explicativa para a visão contábil |
| NumFtc | Number(010,0) | Não | Número do fato contábil |
| GruNex | String(030) | Sim | Grupo de notas explicativas |
| SeqNex | Number(007,0) | Sim | Sequência do grupo de notas explicativas |

---

## Chave Primária

- CodEmp
- CodVis
- CtaVis
- SeqCol
- SeqCmp
- PerIni
- PerFim
- NumFtc

---

## Índices

### E046VNEIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodVis
- SeqCol

---

## Relacionamentos

### IR_E046VNE_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E046VNE_001

**Tabela:** E046VIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |

### IR_E046VNE_002

**Tabela:** E046PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |
| CtaVis | CtaVis |

### IR_E046VNE_003

**Tabela:** E046COL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |
| SeqCol | SeqCol |

