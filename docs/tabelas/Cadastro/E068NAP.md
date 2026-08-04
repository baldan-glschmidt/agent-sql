# E068NAP

## Descrição

Tabelas - Níveis de Aprovação

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa do nível de aprovação |
| RotNap | Number(002,0) | Não | Código da rotina para controle de níveis de aprovação |
| CodNap | Number(004,0) | Não | Código do nível de aprovação |
| DesNap | String(100) | Não | Descrição do nível de aprovação |
| AbrNap | String(020) | Não | Abreviatura do nível de aprovação |
| ObsNap | String(250) | Sim | Observação do nível de aprovação |
| SitNap | String(001) | Não | Situação do nível de aprovação |
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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
