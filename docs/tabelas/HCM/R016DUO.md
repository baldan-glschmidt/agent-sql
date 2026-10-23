# R016DUO

## Descrição

Dados da Duplicação do Organograma

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| OrgDes | Number(004,0) | Não | Código do Organograma Destino |
| OrgOri | Number(004,0) | Sim | Código do Organograma Origem |
| DatAlt | Date | Sim | Data de Alteração do Organograma |
| NivCol | Number(002,0) | Sim | Nível do Local p/ Cadastramento dos Colaboradores |
| NivQua | Number(002,0) | Sim | Nível do QL |
| AbrEmp | String(100) | Sim | Empresas que Utilizam o Organograma Destino |
| DatDup | Date | Sim | Data de Início da Duplicação |
| HorDup | Number(005,0) | Sim | Hora de Início da Duplicação |

---

## Chave Primária

- OrgDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016DUO_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| OrgDes | TabOrg |

### IR_R016DUO_001

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| OrgOri | TabOrg |

