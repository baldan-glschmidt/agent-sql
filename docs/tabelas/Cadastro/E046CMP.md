# E046CMP

## Descrição

Tabelas - Visões Contábeis - Plano de Contas

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodVis | String(020) | Não | Código da visão |
| CtaVis | Number(009,0) | Não | Conta da visão |
| SeqCol | Number(003,0) | Não | Seqüência da coluna |
| SeqCmp | Number(003,0) | Não | Seqüência da composição da coluna |
| ForCal | String(250) | Sim | Fórmula a ser calculada |
| CtaRef | Number(009,0) | Sim | Conta da própria visão |
| ColRef | Number(003,0) | Sim | Seqüência da coluna da conta da própria visão |
| CodMpc | Number(004,0) | Sim | Código do modelo de plano contábil utilizado na composição |
| CtaRed | Number(007,0) | Sim | Número da conta reduzida |
| TipVlr | String(001) | Sim | Tipo de valor da conta reduzida |
| CodAgl | Number(009,0) | Sim | Código da aglutinação contábil |
| CodSql | Number(009,0) | Sim | Código de geração do SQL |
| SeqSql | Number(004,0) | Sim | Sequencial de montagem do SQL |
| IndNeg | String(001) | Sim | Indica se a seqüência deverá ser multiplicada por -1 |
| CodReg | Number(004,0) | Sim | Código da regra para cálculo da composição |

---

## Chave Primária

- CodEmp
- CodVis
- CtaVis
- SeqCol
- SeqCmp

---

## Índices

### E046CMPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodVis
- SeqCol

---

## Relacionamentos

### IR_E046CMP_001

**Tabela:** E046VIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |

### IR_E046CMP_002

**Tabela:** E046PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |
| CtaVis | CtaVis |

### IR_E046CMP_003

**Tabela:** E046COL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |
| SeqCol | SeqCol |

