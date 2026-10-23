# R184QLO

## Descrição

PLR - Questionário do Local

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CmpPpr | Date | Não | Competência de Cálculo do PPR |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| LocAva | Number(009,0) | Não | Código do Local Avaliador |
| CodGrp | Number(006,0) | Não | Código do Grupo |
| CodIte | Number(003,0) | Não | Código do Item |
| RspPpr | Number(011,2) | Sim | Resposta (Nota) |
| ComQlo | String(255) | Sim | Comentário do Questionário |

---

## Chave Primária

- NumEmp
- CmpPpr
- TabOrg
- NumLoc
- LocAva
- CodGrp
- CodIte

---

## Índices

### R184QLOIndice2

**Tipo:** Não unico

Campos:
- NumLoc

---

## Relacionamentos

### IR_R184QLO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R184QLO_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R184QLO_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| LocAva | NumLoc |

### IR_R184QLO_005

**Tabela:** R182GRP

| Origem | Destino |
|--------|---------|
| CodGrp | CodGrp |

### IR_R184QLO_006

**Tabela:** R182GRI

| Origem | Destino |
|--------|---------|
| CodGrp | CodGrp |
| CodIte | CodIte |

