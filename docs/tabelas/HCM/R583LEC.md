# R583LEC

## Descrição

GHE - Revisão do GHE - Locais e Cargos

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| TabOrg | Number(004,0) | Não | Código da tabela de organograma do local |
| NumLoc | Number(009,0) | Não | Local do organograma |
| EstCar | Number(004,0) | Não | Código da estrutura de cargos |
| CodCar | String(024) | Não | Código do cargo |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- TabOrg
- NumLoc
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583LEC_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

### IR_R583LEC_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R583LEC_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

