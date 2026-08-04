# E068CNA

## Descrição

Tabelas - Centros de Custos por Usuário e Nível de Aprovação

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa do centro de custo por usuário do nível de aprovação |
| RotNap | Number(002,0) | Não | Código da rotina para controle de níveis de aprovação |
| CodNap | Number(004,0) | Não | Código do nível de aprovação |
| CodUsu | Number(010,0) | Não | Código do usuário pertencente ao nível de aprovação |
| CodCcu | String(009) | Não | Código do centro de custos que o usuário pode aprovar |
| CriCna | Number(001,0) | Não | Critério para centro de custos válidos (1=Só ele, 2=Todos subordinados a ele) |
| ObsCna | String(250) | Sim | Observação do centro de custos por usuário do nível de aprovação do projeto |
| SitCna | String(001) | Não | Situação do centro de custo por usuário e nível de aprovação |
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
- CodCcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E068CNA_003

**Tabela:** E068UNA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| RotNap | RotNap |
| CodNap | CodNap |
| CodUsu | CodUsu |

