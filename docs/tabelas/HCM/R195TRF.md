# R195TRF

## Descrição

Cenário - Transferências Coletivas p/ Local

---

## Resumo

- Campos: 20
- Chave Primária: 8 campo(s)
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
| EmpDes | Number(004,0) | Sim | Código da empresa de destino |
| CenDes | Number(004,0) | Sim | Código do cenário de destino |
| CodFil | Number(006,0) | Sim | Código da filial de destino |
| OrgDes | Number(004,0) | Sim | Código da tabela de organograma do local de destino |
| LocDes | Number(009,0) | Sim | Local do organograma de destino |
| EstDes | Number(004,0) | Sim | Código da estrutura de cargos de destino |
| CarDes | String(024) | Sim | Código do cargo de destino |
| QtdTrf | Number(004,0) | Sim | Quantidade de colaboradores envolvidos |
| CmpTer | Date | Sim | Data de término da transferência |
| ObsTrf | String(250) | Sim | Observação sobre a transferência |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| DefOnu | String(001) | Sim | Define se a transferência de empresa terá ônus |

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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195TRF_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195TRF_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R195TRF_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

