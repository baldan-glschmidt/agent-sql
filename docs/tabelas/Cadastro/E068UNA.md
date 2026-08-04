# E068UNA

## Descrição

Tabelas - Usuários por Nível de Aprovação

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa do usuário do nível de aprovação do projeto |
| RotNap | Number(002,0) | Não | Código da rotina de controle de níveis de aprovação |
| CodNap | Number(004,0) | Não | Código do nível de aprovação |
| CodUsu | Number(010,0) | Não | Usuário pertencente ao nível da rotina de controle de aprovação |
| DtiVal | Date | Sim | Data validade inicial para o usuário no nível da rotina de controle de aprovação |
| DtfVal | Date | Sim | Data validade final para o usuário no nível da rotina de controle de aprovação |
| ObsUna | String(250) | Sim | Observação para o usuário no nível da rotina de controle de aprovação |
| SitUna | String(001) | Sim | Situação do usuário no nível da rotina de controle de aprovação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |

---

## Chave Primária

- CodEmp
- RotNap
- CodNap
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E068UNA_002

**Tabela:** E068NAP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| RotNap | RotNap |
| CodNap | CodNap |

