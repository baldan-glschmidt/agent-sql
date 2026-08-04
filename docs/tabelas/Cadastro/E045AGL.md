# E045AGL

## Descrição

Tabelas - Aglutinação Contábil

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAgl | Number(009,0) | Não | Código da aglutinação contábil |
| DesAgl | String(250) | Sim | Descrição da aglutinação contábil |
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodMpc | Number(004,0) | Sim | Código do modelo de plano contábil utilizado |
| CodMpu | Number(004,0) | Sim | Código do modelo de plano de centro de custos utilizado |
| TipAgl | Number(001,0) | Sim | Tipo de aglutinação contábil |
| PerAgl | String(001) | Sim | Periodicidade para retorno da aglutinação contábil |
| DesZer | String(001) | Sim | Indicativo que a busca dos valores irá desconsiderar o zeramento contábil |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitAgl | String(001) | Não | Situação da aglutinação contábil |

---

## Chave Primária

- CodAgl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
