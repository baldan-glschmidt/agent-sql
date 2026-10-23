# R130OCU

## Descrição

Orçamento Local - Cursos Aperfeiçoamento

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| AnoBas | Number(004,0) | Não | Ano Base do Orçamento |
| MesBas | Number(002,0) | Não | Mês Base do Orçamento |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| SeqCus | Number(002,0) | Não | Sequência de Custos |
| CodOem | Number(008,0) | Sim | Código da Entidade |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| PerDia | String(001) | Sim | Período Disponível do Dia |
| VagCur | Number(006,0) | Sim | Vagas Curso |
| TipRea | Number(003,0) | Sim | Tipo de Realização |
| CodMcu | Number(003,0) | Sim | Tipo de Motivo |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- AnoBas
- MesBas
- CodCua
- SeqCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130OCU_004

**Tabela:** R130OLV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| AnoBas | AnoBas |
| MesBas | MesBas |

### IR_R130OCU_005

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

