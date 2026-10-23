# R080PRO

## Descrição

Proposta Quadro Lotação p/ Local - Agrupadora

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

### IR_R080PRO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R080PRO_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R080PRO_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

