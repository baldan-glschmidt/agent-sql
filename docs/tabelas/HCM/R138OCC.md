# R138OCC

## Descrição

Orçamento por Centro de Custo - Cursos Aperfeiçoamento

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| AnoBas | Number(004,0) | Não | Ano Base do Orçamento |
| MesBas | Number(002,0) | Não | Mês Base do Orçamento |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| SeqCus | Number(003,0) | Não | Sequência de Custos |
| CodOem | Number(008,0) | Sim | Código da Entidade |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| PerDia | String(001) | Sim | Período Disponível do Dia |
| VagCur | Number(006,0) | Sim | Vagas Curso |
| TipRea | Number(003,0) | Sim | Tipo de Realização |
| CodMcu | Number(003,0) | Sim | Tipo de Motivo |

---

## Chave Primária

- NumEmp
- CodCcu
- AnoBas
- MesBas
- CodCua
- SeqCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R138OCC_003

**Tabela:** R138OCV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |
| AnoBas | AnoBas |
| MesBas | MesBas |

### IR_R138OCC_004

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

