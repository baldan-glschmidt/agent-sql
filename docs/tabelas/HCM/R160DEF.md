# R160DEF

## Descrição

BS - Definições Empréstimos

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
| CodEnt | Number(003,0) | Não | Código da Entidade |
| NomEnt | String(040) | Sim | Nome da Entidade Beneficente |
| NumCgc | Number(015,0) | Sim | Número do CNPJ da Entidade - Obsoleto |
| CfjIns | String(014) | Sim | Número do CNPJ da Entidade |
| UltEmp | Number(004,0) | Sim | Número Último Empréstimo |
| IndJur | Number(003,0) | Sim | Tabela de Índice de Juros |
| JurSub | Number(005,2) | Sim | % Juros Subsidiado |
| DiaInd | Number(002,0) | Sim | Dia de Aplicação do Índice |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| EvePar | Number(004,0) | Sim | Evento para Desconto das Parcelas |
| EveJur | Number(004,0) | Sim | Evento para Desconto dos Juros |
| JurPar | String(001) | Sim | Juros Descontados nas Parcelas ou no Final |
| RgrPar | Number(003,0) | Sim | Código da Regra Especial Parcelas |
| RgrJur | Number(003,0) | Sim | Código da Regra Especial Juros |
| JunEmp | String(001) | Sim | Juntar Solicitações de Empréstimos |

---

## Chave Primária

- CodEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
