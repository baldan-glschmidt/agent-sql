# R075BHT

## Descrição

Carreira - Bloco Habilidades Técnicas

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCrr | Number(003,0) | Não | Código da Carreira |
| DatAlt | Date | Não | Data da Última Revisão das Habilidades da Carreira |
| CodHie | Number(003,0) | Não | Código da Hierarquia |
| BloHte | String(004) | Não | Bloco de Habilidades Técnicas do Cargo |

---

## Chave Primária

- EstCar
- CodCrr
- DatAlt
- CodHie
- BloHte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R075BHT_001

**Tabela:** R075CRR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCrr | CodCrr |

### IR_R075BHT_004

**Tabela:** R077BLO

| Origem | Destino |
|--------|---------|
| BloHte | BloHte |

