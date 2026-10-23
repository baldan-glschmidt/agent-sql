# R081RES

## Descrição

Reserva Vaga Quadro Lotação p/ Time

---

## Resumo

- Campos: 20
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodTim | String(008) | Não | Código do Time |
| CmpQua | Date | Não | Data do Quadro |
| VagGer | Number(004,0) | Sim | Vagas no Turno Geral |
| VagTu1 | Number(004,0) | Sim | Vagas no Primeiro Turno |
| VagTu2 | Number(004,0) | Sim | Vagas no Segundo Turno |
| VagTu3 | Number(004,0) | Sim | Vagas no Terceiro Turno |
| VagTu4 | Number(004,0) | Sim | Vagas no Quarto Turno |
| VagMis | Number(004,0) | Sim | Vagas no Turno Misto |
| VagTer | Number(004,0) | Sim | Vagas de Terceiros |
| VmuGer | Number(004,0) | Sim | Vagas Multifuncional Turno Geral |
| VmuTu1 | Number(004,0) | Sim | Vagas Multifuncional Primeiro Turno |
| VmuTu2 | Number(004,0) | Sim | Vagas Multifuncional Segundo Turno |
| VmuTu3 | Number(004,0) | Sim | Vagas Multifuncional Terceiro Turno |
| VmuTu4 | Number(004,0) | Sim | Vagas Multifuncional Quarto Turno |
| VmuMis | Number(004,0) | Sim | Vagas Multifuncional Turno Misto |
| TipCol | Number(001,0) | Sim | Tipo de Responsável |
| NumCad | Number(009,0) | Sim | Responsável |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodTim
- CmpQua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R081RES_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R081RES_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R081RES_003

**Tabela:** R078TIM

| Origem | Destino |
|--------|---------|
| CodTim | CodTim |

