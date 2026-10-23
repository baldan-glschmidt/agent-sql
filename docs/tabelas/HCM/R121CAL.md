# R121CAL

## Descrição

Concurso - Cargos por local

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |
| NumEmp | Number(004,0) | Não | Código da empresa solicitante |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| QtdVga | Number(004,0) | Sim | Quantidade de vagas solicitadas pela área |
| ObsCon | String(420) | Sim | Observação sobre a vaga |
| EscNot | Number(009,0) | Sim | Código da Escala |
| EstRqu | Number(004,0) | Sim | Código da Estrutura de Cargos p/ Requisição |
| CarRqu | String(024) | Sim | Código do Cargo p/ Requisição |

---

## Chave Primária

- AnoCon
- NumCon
- EstCar
- CodCar
- NumEmp
- TabOrg
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121CAL_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121CAL_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R121CAL_004

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R121CAL_006

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

