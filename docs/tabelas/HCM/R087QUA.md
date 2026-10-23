# R087QUA

## Descrição

Quadro de Lotação p/ Centro de Custo - Agrupadora

---

## Resumo

- Campos: 19
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
- CodCcu
- EstCar
- CodCar
- CmpQua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R087QUA_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R087QUA_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

