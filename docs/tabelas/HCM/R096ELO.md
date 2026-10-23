# R096ELO

## Descrição

Epi por Local

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodEpi | Number(008,0) | Não | Código do EPI |
| UsoEpi | Number(001,0) | Sim | Uso do Epi |
| DiaVal | Number(004,0) | Sim | Dias de validade do Epi |
| DiaRev | Number(004,0) | Sim | Dias de revisão do Epi |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096ELO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R096ELO_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R096ELO_003

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

