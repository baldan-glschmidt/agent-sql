# E066OTE

## Descrição

Cadastros - Operadoras de Telefonia

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOte | Number(004,0) | Não | Código da operadora de telefonia |
| NomOte | String(100) | Sim | Nome da operadora de telefonia |
| SitOpe | String(001) | Não | Situação da operadora |
| CodCli | Number(009,0) | Sim | Código do cliente relacionado ao cadastro da operadora |
| CodFor | Number(009,0) | Sim | Código do fornecedor relacionado ao cadastro da operadora |
| PerRep | Number(005,2) | Sim | Percentual de comissão a ser pago ao representante da venda. |
| PerCom | Number(005,2) | Sim | Percentual de comissão a ser paga a loja pela venda |
| OpeTef | String(020) | Sim | Operadora identificada pelo TEF |
| ObsOte | String(200) | Sim | Observação sobre a operada de telefonia |

---

## Chave Primária

- CodEmp
- CodOte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
