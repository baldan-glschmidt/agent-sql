# R089EFE

## Descrição

Quadro Efetivo p/ Função

---

## Resumo

- Campos: 8
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
| DatTer | Date | Sim | Data de Término |

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

### IR_R089EFE_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R089EFE_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R089EFE_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

