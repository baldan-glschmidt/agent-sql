# R087EFD

## Descrição

Quadro Efetivo p/ Centro de Custo - Detalhada

---

## Resumo

- Campos: 18
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
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

### IR_R087EFD_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R087EFD_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

