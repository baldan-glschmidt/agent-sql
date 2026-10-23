# R036PFI

## Descrição

Pensão Judicial - Valor Fixo

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
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
| DatAlt | Date | Não | Data de Alteração do Valor Fixo |
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

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036PFI_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

