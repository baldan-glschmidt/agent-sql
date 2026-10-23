# R130DCI

## Descrição

Despesas da Turma - Curso p/ Item Despesa

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| DatDes | Date | Não | Data de Pagamento da Despesa |
| CodTcu | Number(004,0) | Não | Item  de Custo |
| SeqIte | Number(002,0) | Não | Sequência do Item de Despesa |
| ValCus | Number(011,2) | Sim | Valor do Item |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |

---

## Chave Primária

- CodCua
- TmaCua
- DatDes
- CodTcu
- SeqIte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130DCI_001

**Tabela:** R130DCU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R130DCI_003

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

