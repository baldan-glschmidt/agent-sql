# R130DPI

## Descrição

Despesas da Turma - Participante p/ Item Despesa

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Participante |
| NumCad | Number(009,0) | Não | Cadastro do Participante |
| DatDes | Date | Não | Data de Pagamento da Despesa |
| CodTcu | Number(004,0) | Não | Item Custo |
| SeqIte | Number(002,0) | Não | Sequência do Item de Despesa |
| ValCus | Number(011,2) | Sim | Valor do Item |
| ValRee | Number(011,2) | Sim | Valor do Reembolso |
| OriLan | String(001) | Sim | Origem do Lançamento |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad
- DatDes
- CodTcu
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130DPI_004

**Tabela:** R130DPA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R130DPI_006

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

