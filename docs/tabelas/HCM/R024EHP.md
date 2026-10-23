# R024EHP

## Descrição

Exceções de Requisitos - Habilidade Pessoal

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| BloHpe | String(004) | Não | Bloco de Habilidades Pessoais |

---

## Chave Primária

- TabOrg
- NumLoc
- EstCar
- CodCar
- DatRqu
- BloHpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024EHP_003

**Tabela:** R024ERL

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024EHP_005

**Tabela:** R079BLO

| Origem | Destino |
|--------|---------|
| BloHpe | BloHpe |

