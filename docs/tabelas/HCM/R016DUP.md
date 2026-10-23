# R016DUP

## Descrição

Duplicação Organograma - Controle

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código do organograma de origem |
| DatDup | Date | Não | Data da duplicação |
| OrgDup | Number(004,0) | Sim | Código do organograma de destino |
| NomOrg | String(030) | Sim | Nome do organograma de duplicação |
| SitDup | Number(001,0) | Sim | Situação da duplicação |

---

## Chave Primária

- TabOrg
- DatDup

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016DUP_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

