# R089PRO

## Descrição

Proposta de Quadro de Lotação p/ Função

---

## Resumo

- Campos: 17
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
| CmpQua | Date | Não | Data de Alteração do Quadro |
| VagGer | Number(004,0) | Sim | Vagas no Turno Geral |
| EstSal | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial Inicial |
| NivSal | String(005) | Sim | Nível Salarial Inicial |
| PerFun | Number(009,5) | Sim | % de Índice da Função |
| DatTer | Date | Sim | Data de Término |
| ResFun | String(001) | Sim | Responsável pelo Local |
| SitPrp | Number(001,0) | Sim | Situação da Proposta |
| ObsPro | String(250) | Sim | Observação Proposta Quadro de Função |
| TipCol | Number(001,0) | Sim | Tipo de Responsável |
| NumCad | Number(009,0) | Sim | Responsável |

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

### IR_R089PRO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R089PRO_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R089PRO_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

