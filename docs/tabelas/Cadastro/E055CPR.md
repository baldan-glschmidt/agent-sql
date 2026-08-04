# E055CPR

## Descrição

Cadastros - Tributos - Tabela de presunção por Competência

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPre | String(004) | Não | Código da tabela de presunção |
| DatCmp | Date | Não | Data de competência da presunção |
| PerPre | Number(007,4) | Sim | Percentual de presunção |
| CodBnf | Number(004,0) | Sim | Código do benefício fiscal |
| VlrLfa | Number(014,2) | Sim | Limite anual do percentual favorecido |
| PerFav | Number(007,4) | Sim | Percentual favorecido |
| SitReg | String(001) | Sim | Situação da competência |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodPre
- DatCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
