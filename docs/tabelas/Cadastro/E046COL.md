# E046COL

## Descrição

Tabelas - Visões contábeis - Colunas

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodVis | String(020) | Não | Código da visão |
| SeqCol | Number(003,0) | Não | Seqüência da coluna |
| DesCol | String(020) | Não | Descrição que aparecerá na consulta e no relatório |
| RefPer | String(001) | Sim | Indicativo que a coluna possui referência com a periodicidade da visão |
| ObsCol | String(1999) | Sim | Observações da coluna |
| IndTot | String(001) | Sim | Indicativo se a coluna é uma totalizadora |
| IndNex | String(001) | Sim | Indicativo se a coluna é utilizada para representação das notas explicativas |

---

## Chave Primária

- CodEmp
- CodVis
- SeqCol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E046COL_001

**Tabela:** E046VIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodVis | CodVis |

