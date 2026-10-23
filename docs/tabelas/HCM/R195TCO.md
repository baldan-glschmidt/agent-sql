# R195TCO

## Descrição

Cenário - Transferências Coletivas - Colaboradores

---

## Resumo

- Campos: 17
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpQua | Date | Não | Data do Quadro |
| SeqTrf | Number(003,0) | Não | Sequência dos registros de transferências |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| EmpDes | Number(004,0) | Sim | Código da Nova Empresa |
| CenDes | Number(004,0) | Sim | Código do cenário de destino |
| CadDes | Number(009,0) | Sim | Cadastro do colaborador na empresa de destino |
| OriTrf | Number(001,0) | Sim | Origem da transferência |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| EstDes | Number(004,0) | Sim | Código da Estrutura de Cargos de Destino |
| CarDes | String(024) | Sim | Código do cargo de destino |

---

## Chave Primária

- NumEmp
- CodCen
- TabOrg
- NumLoc
- EstCar
- CodCar
- CmpQua
- SeqTrf
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195TCO_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195TCO_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R195TCO_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

