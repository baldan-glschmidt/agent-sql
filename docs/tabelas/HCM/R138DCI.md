# R138DCI

## Descrição

Despesas da Turma - Centro de Custo p/ Item Despesa

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| DatDes | Date | Não | Data de Pagamento da Despesa |
| CodTcu | Number(004,0) | Não | Item Custo |
| SeqIte | Number(002,0) | Não | Sequência do Item de Despesa |
| ValCus | Number(011,2) | Sim | Valor do Item |
| OriLan | String(001) | Sim | Origem do lançamento |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- CodCcu
- DatDes
- CodTcu
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R138DCI_005

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

