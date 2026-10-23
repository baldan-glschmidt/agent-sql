# R080EFD

## Descrição

Quadro Efetivo p/ Local - Detalhada

---

## Resumo

- Campos: 19
- Chave Primária: 7 campo(s)
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
| TipVag | Number(002,0) | Não | Código do tipo de vaga |
| CmpQua | Date | Não | Data |
| VagGer | Number(004,0) | Sim | Vagas no Turno Geral |
| VagTu1 | Number(004,0) | Sim | Vagas no 1º Turno |
| VagTu2 | Number(004,0) | Sim | Vagas no 2º Turno |
| VagTu3 | Number(004,0) | Sim | Vagas no 3º Turno |
| VagTu4 | Number(004,0) | Sim | Vagas no 4º Turno |
| VagMis | Number(004,0) | Sim | Vagas Turno Misto |
| VagGeA | Number(004,0) | Sim | Qtd. Afastados Turno Geral |
| VagT1A | Number(004,0) | Sim | Qtd. Afastados 1º Turno |
| VagT2A | Number(004,0) | Sim | Qtd. Afastados no 2º Turno |
| VagT3A | Number(004,0) | Sim | Qtd. Afastados no 3º Turno |
| VagT4A | Number(004,0) | Sim | Qtd. Afastados  no 4º Turno |
| VagMiA | Number(004,0) | Sim | Qtd. Afastados Turno Misto |

---

## Chave Primária

- NumEmp
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

### IR_R080EFD_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R080EFD_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R080EFD_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

