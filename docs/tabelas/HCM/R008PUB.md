# R008PUB

## Descrição

Cadastro de Eventos - Órgão Público

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CmpAlt | Date | Não | Competência |
| EstOrg | String(002) | Não | Estado |
| SCNaCo | Number(002,0) | Sim | Natureza do Componente Estado Santa Catarina |
| SCIdCo | String(001) | Sim | Indicador de Componente Estado Santa Catarina |
| CodPlc | Number(006,0) | Sim | Código da Conta - Plano de Contas da Folha de Pagamento |
| PisMag | String(001) | Sim | Compõe Piso do Magistério |
| ComEmp | String(001) | Sim | Compõe Empenho |

---

## Chave Primária

- CodTab
- CodEve
- CmpAlt
- EstOrg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008PUB_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

