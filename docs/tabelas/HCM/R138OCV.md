# R138OCV

## Descrição

Orçamento por Centro de Custo - Vagas/Mês

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| AnoBas | Number(004,0) | Não | Ano Base do Orçamento |
| MesBas | Number(002,0) | Não | Mês Base do Orçamento |
| QtdVag | Number(006,0) | Sim | Quantidade de Vagas |
| ValOrc | Number(011,2) | Sim | Valor do Orçamento |

---

## Chave Primária

- NumEmp
- CodCcu
- AnoBas
- MesBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R138OCV_002

**Tabela:** R138ORC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |
| AnoBas | AnoBas |

