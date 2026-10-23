# R340EXD

## Descrição

Exigibilidade Suspensa - S-1210 - Deduções Pensão Alimentícia e Dependentes

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpPag | Date | Não | Competência Pagamento |
| CodRec | Number(006,0) | Não | Código de receita relativo ao IRRF sobre rendimentos do trabalho |
| CodPro | Number(009,0) | Não | Código do Processo |
| CodSus | Number(014,0) | Não | Código Suspensão |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqExd | Number(003,0) | Não | Sequência |
| TipDed | Number(001,0) | Sim | Indicativo do tipo de dedução |
| CodDep | Number(002,0) | Não | Código do dependente |
| CpfDep | Number(011,0) | Sim | Número de inscrição no CPF |
| VlrDed | Number(014,2) | Sim | Valor da dedução relativa a dep. ou a pensão alimentícia com exigib. suspensa - Mensal |
| VlrFer | Number(014,2) | Sim | Valor da dedução relativa a dep. ou a pensão alimentícia com exigib. suspensa - Férias |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPag
- CodRec
- CodPro
- CodSus
- IndApu
- SeqExd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R340EXD_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R340EXD_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

