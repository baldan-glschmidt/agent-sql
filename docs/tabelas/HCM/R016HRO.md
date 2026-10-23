# R016HRO

## Descrição

Histórico Reestruturação Organograma

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
| SitPro | Number(001,0) | Sim | Situação do Processo |
| LocOri | String(150) | Sim | Local de Origem |
| DesOri | String(060) | Sim | Descrição do Local Origem |
| LocDes | String(150) | Sim | Local de Destino |
| DesDes | String(060) | Sim | Descrição do Local Destino |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016HRO_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

