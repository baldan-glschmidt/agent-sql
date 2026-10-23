# R016HRS

## Descrição

Histórico Reestruturação Organograma - Sublocais

---

## Resumo

- Campos: 7
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| DatAlt | Date | Sim | Data da Reestruturação do Organograma |
| LocOri | String(150) | Sim | Local de Origem |
| SubOri | String(150) | Sim | Sublocal de Origem |
| DesOri | String(060) | Sim | Descrição do Sublocal Origem |
| SubDes | String(150) | Sim | Sublocal de Destino |
| DesDes | String(060) | Sim | Descrição do Sublocal Destino |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016HRS_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

