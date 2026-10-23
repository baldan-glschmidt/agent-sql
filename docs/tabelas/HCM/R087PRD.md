# R087PRD

## Descrição

Proposta Quadro Lotação p/ C. Custo - Detalhada

---

## Resumo

- Campos: 19
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código do Centro de Custo |
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
| SitPrp | Number(001,0) | Sim | Situação da Proposta |
| ObsPql | String(250) | Sim | Observação Quadro de Lotação |
| TipCol | Number(001,0) | Sim | Tipo de Responsável |
| NumCad | Number(009,0) | Sim | Responsável |
| EmpSol | Number(004,0) | Sim | Código da Empresa do Solicitante |
| TipSol | Number(001,0) | Sim | Tipo de Colaborador Solicitante |
| CadSol | Number(009,0) | Sim | Cadastro do Colaborador Solicitante |

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

### IR_R087PRD_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R087PRD_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R087PRD_004

**Tabela:** R022VAG

| Origem | Destino |
|--------|---------|
| TipVag | TipVag |

