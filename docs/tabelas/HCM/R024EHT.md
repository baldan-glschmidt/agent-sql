# R024EHT

## Descrição

Exceções de Requisitos - Habilidade Técnica

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
| BloHte | String(004) | Não | Bloco de Habilidades Técnicas |

---

## Chave Primária

- TabOrg
- NumLoc
- EstCar
- CodCar
- DatRqu
- BloHte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024EHT_003

**Tabela:** R024ERL

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024EHT_005

**Tabela:** R077BLO

| Origem | Destino |
|--------|---------|
| BloHte | BloHte |

