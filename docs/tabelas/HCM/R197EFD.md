# R197EFD

## Descrição

Cenário - Quadro Efetivo p/ Centro de Custo - Detalhada

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
| CodCen | Number(004,0) | Não | Código do cenário |
| CodCcu | String(018) | Não | Código do Centro de Custo |
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
- CodCen
- CodCcu
- EstCar
- CodCar
- TipVag
- CmpQua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R197EFD_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R197EFD_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R197EFD_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

