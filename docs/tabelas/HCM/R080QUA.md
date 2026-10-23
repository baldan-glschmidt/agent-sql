# R080QUA

## Descrição

Quadro de Lotação p/ Local - Agrupadora

---

## Resumo

- Campos: 20
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpQua | Date | Não | Data do Quadro |
| VagGer | Number(004,0) | Sim | Vagas no Turno Geral |
| VagTu1 | Number(004,0) | Sim | Vagas no Primeiro Turno |
| VagTu2 | Number(004,0) | Sim | Vagas no Segundo Turno |
| VagTu3 | Number(004,0) | Sim | Vagas no Terceiro Turno |
| VagTu4 | Number(004,0) | Sim | Vagas no Quarto Turno |
| VagMis | Number(004,0) | Sim | Vagas no Turno Misto |
| VagTer | Number(004,0) | Sim | Vagas de Terceiros |
| ObsQua | String(250) | Sim | Observação Quadro de Lotação |
| VagGet | Number(004,0) | Sim | Vagas temporárias no turno geral |
| VagT1t | Number(004,0) | Sim | Vagas temporárias no primeiro turno |
| VagT2t | Number(004,0) | Sim | Vagas temporárias no segundo turno |
| VagT3t | Number(004,0) | Sim | Vagas temporárias no terceiro turno |
| VagT4t | Number(004,0) | Sim | Vagas temporárias no quarto turno |
| VagMit | Number(004,0) | Sim | Vagas temporárias no turno misto |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- EstCar
- CodCar
- CmpQua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R080QUA_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R080QUA_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R080QUA_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

