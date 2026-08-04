# E720OAC

## Descrição

Ficha - Roteiro - Cadastro de Acessórios da Operação

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOpr | String(006) | Não | Código da operação |
| CodAcs | String(008) | Não | Código do Acessório associado a Operação |
| CodEtg | Number(004,0) | Sim | Código do Estágio que a operação será utilizada |
| QtdAcs | Number(009,0) | Não | Quantidade de Acessórios utilizados na Operação |
| ObsAcs | String(240) | Sim | Observações sobre o Acessório na Operação |
| DatAlt | Date | Sim | Data da Geração ou Alteração |
| CodUsu | Number(010,0) | Sim | Usuário Geração/alteração |

---

## Chave Primária

- CodEmp
- CodOpr
- CodAcs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
