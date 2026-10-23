# R130DLI

## Descrição

Despesas da Turma - Local p/ Item Despesa

---

## Resumo

- Campos: 11
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
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| DatDes | Date | Não | Data de Pagamento da Despesa |
| CodTcu | Number(004,0) | Não | Item Custo |
| SeqIte | Number(002,0) | Não | Sequência do Item de Despesa |
| ValCus | Number(011,2) | Sim | Valor do Item |
| OriLan | String(001) | Sim | Origem do Lançamento |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TabOrg
- NumLoc
- DatDes
- CodTcu
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130DLI_004

**Tabela:** R130DLO

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R130DLI_006

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

