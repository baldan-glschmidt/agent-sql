# R195LAG

## Descrição

Cenário - Adicionais p/ Cargo

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| EstCar | Number(004,0) | Não | Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatAlt | Date | Não | Data da Alteração |
| PerIns | Number(005,2) | Sim | % Insalubridade |
| PerPer | Number(005,2) | Sim | % Periculosidade |
| FatTph | Number(004,2) | Sim | Fator Tempo Serviço p/ Homens |
| FatTpm | Number(004,2) | Sim | Fator Tempo Serviço p/ Mulheres |
| ApoEsp | Number(002,0) | Sim | Número de Anos p/ Aposentadoria Especial |
| CmpTer | Date | Sim | Competência Término do Adicional |

---

## Chave Primária

- NumEmp
- CodCen
- EstCar
- CodCar
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195LAG_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195LAG_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

