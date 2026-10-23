# R134DTL

## Descrição

Turmas - Vagas p/Local

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| VagDis | Number(006,0) | Sim | Qtde Vagas Distribuídas |
| VagCon | Number(006,0) | Sim | Qtde Vagas Confirmadas |
| OriVag | String(001) | Sim | Origem Vagas: (R)eserva ou (D)igitada |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TabOrg
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134DTL_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134DTL_002

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R134DTL_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

