# R195QUD

## Descrição

Cenário - Quadro de Lotação p/ Local - Detalhada

---

## Resumo

- Campos: 22
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 4

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
| TipVag | Number(002,0) | Não | Código do tipo de vaga |
| CmpQua | Date | Não | Data do Quadro |
| VagGer | Number(004,0) | Sim | Vagas no Turno Geral |
| VagTu1 | Number(004,0) | Sim | Vagas no Primeiro Turno |
| VagTu2 | Number(004,0) | Sim | Vagas no Segundo Turno |
| VagTu3 | Number(004,0) | Sim | Vagas no Terceiro Turno |
| VagTu4 | Number(004,0) | Sim | Vagas no Quarto Turno |
| VagMis | Number(004,0) | Sim | Vagas no Turno Misto |
| ObsQua | String(250) | Sim | Observação Quadro de Lotação |
| VagGet | Number(004,0) | Sim | Vagas temporárias no turno geral |
| VagT1t | Number(004,0) | Sim | Vagas temporárias no primeiro turno |
| VagT2t | Number(004,0) | Sim | Vagas temporárias no segundo turno |
| VagT3t | Number(004,0) | Sim | Vagas temporárias no terceiro turno |
| VagT4t | Number(004,0) | Sim | Vagas temporárias no quarto turno |
| VagMit | Number(004,0) | Sim | Vagas temporárias no turno misto |
| CodFil | Number(006,0) | Sim | Código da filial do nível do organograma |

---

## Chave Primária

- NumEmp
- CodCen
- TabOrg
- NumLoc
- EstCar
- CodCar
- TipVag
- CmpQua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195QUD_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195QUD_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R195QUD_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R195QUD_006

**Tabela:** R022VAG

| Origem | Destino |
|--------|---------|
| TipVag | TipVag |

