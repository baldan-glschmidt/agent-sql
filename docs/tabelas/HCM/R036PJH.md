# R036PJH

## Descrição

Pensão Judicial - Histórico

---

## Resumo

- Campos: 27
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do Dependente |
| IniPen | Date | Não | Data de Início da Concessão |
| SeqPen | Number(002,0) | Não | Sequência da Pensão |
| CotSaf | Number(001,0) | Sim | Cotas Salário Família |
| BasPju | String(001) | Sim | Tipo Base Cálculo (F,R) |
| ValIni | Number(011,2) | Sim | Valor Fixo Inicial |
| DatIni | Date | Sim | Data Início Correção |
| CodIdm | Number(003,0) | Sim | Código Tabela Índices Correção |
| DiaInd | Number(002,0) | Sim | Dia Índice Correção |
| PerCor | Number(002,0) | Sim | Periodicidade da Correção |
| Pag13s | String(001) | Sim | Pensão Judicial 13° Salário qdo tipo=F |
| PagAdt | Number(001,0) | Sim | Pensão Judicial no Adiantamento Salarial |
| PerAdt | Number(002,0) | Sim | Percentual que será pago no Adiantamento Salarial |
| PagPlr | String(001) | Sim | Pensão Judicial Particip. Lucros |
| PagFer | String(001) | Sim | Pensão Judicial Férias |
| PagMes | Number(001,0) | Sim | Tratamento de pensão judicial no mês |
| Per13s | Number(005,2) | Sim | %  Pensão 13° Salário |
| PerPlr | Number(005,2) | Sim | %  Pensão no PLR |
| PerFer | Number(005,2) | Sim | %  Pensão nas férias |
| FimPen | Date | Sim | Data de Fim da Concessão |
| PerPen | Number(005,2) | Sim | %  Pensão Judicial |
| PerFgt | Number(005,2) | Sim | % Pensão FGTS |
| VlrMin | Number(011,2) | Sim | Valor mínimo para pensão judicial |
| USU_ValDes | Number(011,2) | Sim | Valor para Descontar do valor final da pensão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- IniPen
- SeqPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036PJH_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

