# R016DLO

## Descrição

Duplicação Organograma - Locais

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código do organograma de origem |
| DatDup | Date | Não | Data da duplicação |
| NumLoc | Number(009,0) | Não | Número do local de origem |
| CodLoc | String(150) | Sim | Código do local de origem |
| OrgDes | Number(004,0) | Sim | Código do organograma de destino |
| NumDes | Number(009,0) | Sim | Número do local de destino |
| LocDes | String(150) | Sim | Código do local de destino |
| NomDes | String(060) | Sim | Descrição do local de destino |
| TipOpe | Number(001,0) | Sim | Operação sobre o local de origem na estrutura de destino |

---

## Chave Primária

- TabOrg
- DatDup
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016DLO_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

### IR_R016DLO_001

**Tabela:** R016DUP

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| DatDup | DatDup |

