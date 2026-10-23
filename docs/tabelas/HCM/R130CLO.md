# R130CLO

## Descrição

Custos do Orçamento - Por Local

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| CmpCus | Date | Não | Competência de Custos |
| SeqCus | Number(002,0) | Não | Sequência de Custos |
| CodOem | Number(008,0) | Sim | Código da Entidade |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| TipRea | Number(003,0) | Sim | Tipo de Realização |
| CodIdm | Number(003,0) | Sim | Código do Índice |
| ObsCus | String(200) | Sim | Observação do Custo |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodCua
- CmpCus
- SeqCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130CLO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R130CLO_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R130CLO_003

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R130CLO_008

**Tabela:** R140REA

| Origem | Destino |
|--------|---------|
| TipRea | TipRea |

