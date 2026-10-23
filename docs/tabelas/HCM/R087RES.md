# R087RES

## Descrição

Reserva Vaga Quadro Lotação p/ C. Custo - Agrupadora

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
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
| CmpQua | Date | Não | Data do Quadro |
| VagGer | Number(004,0) | Sim | Vagas no Turno Geral |
| VagTu1 | Number(004,0) | Sim | Vagas no Primeiro Turno |
| VagTu2 | Number(004,0) | Sim | Vagas no Segundo Turno |
| VagTu3 | Number(004,0) | Sim | Vagas no Terceiro Turno |
| VagTu4 | Number(004,0) | Sim | Vagas no Quarto Turno |
| VagMis | Number(004,0) | Sim | Vagas no Turno Misto |
| VagTer | Number(004,0) | Sim | Vagas de Terceiros |
| TipCol | Number(001,0) | Sim | Tipo de Responsável |
| NumCad | Number(009,0) | Sim | Responsável |

---

## Chave Primária

- NumEmp
- CodCcu
- EstCar
- CodCar
- CmpQua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R087RES_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R087RES_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

