# R160EPT

## Descrição

BS - Empréstimos

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Codigo da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CmpEpt | Date | Não | Competência do Empréstimo |
| SeqEpt | Number(002,0) | Não | Sequência do Empréstimo |
| CodEnt | Number(003,0) | Sim | Código da Entidade |
| NroEpt | Number(008,0) | Sim | Número do Empréstimo |
| DatEpt | Date | Sim | Data do Empréstimo |
| NroPar | Number(003,0) | Sim | Número de Parcelas |
| NroAbe | Number(003,0) | Sim | Número de Parcelas em Aberto |
| CmpIni | Date | Sim | Competência Início Desconto |
| MotEpt | Number(003,0) | Sim | Motivo do Empréstimo |
| CodCal | Number(005,0) | Sim | Código de Cálculo Última Integração |
| VlrEpt | Number(011,2) | Sim | Valor do Empréstimo |
| VlrJur | Number(011,2) | Sim | Valor dos Juros |
| VlrPar | Number(011,2) | Sim | Valor da Parcela |
| TotAbe | Number(011,2) | Sim | Total em Aberto |
| JurInt | Number(011,2) | Sim | Valor dos Juros Integrado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpEpt
- SeqEpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R160EPT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R160EPT_011

**Tabela:** R160MOT

| Origem | Destino |
|--------|---------|
| MotEpt | CodMot |

