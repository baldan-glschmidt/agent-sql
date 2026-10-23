# R195LAC

## Descrição

Cenário - Adicionais p/ Local e Cargo

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TabOrg | Number(004,0) | Não | Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatAlt | Date | Não | Data da Alteração |
| PerIns | Number(005,2) | Sim | % Insalubridade |
| PerPer | Number(005,2) | Sim | % Periculosidade |
| FatTph | Number(004,2) | Sim | Fator Tempo Serviço p/ Homens |
| FatTpm | Number(004,2) | Sim | Fator Tempo Serviço p/ Mulheres |
| ApoEsp | Number(002,0) | Sim | Número de Anos p/ Aposentadoria Especial |
| CmpTer | Date | Sim | Competência Término |

---

## Chave Primária

- NumEmp
- CodCen
- TabOrg
- NumLoc
- EstCar
- CodCar
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195LAC_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195LAC_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R195LAC_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

