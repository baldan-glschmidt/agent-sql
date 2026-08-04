# E085AEC

## Descrição

Cadastros - Clientes - Autenticadores Externos de Créditos de Clientes

---

## Resumo

- Campos: 15
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodAec | Number(004,0) | Não | Código do autenticador externo de crédito de clientes |
| DesAec | String(100) | Sim | Descrição do autenticador externo de crédito de clientes |
| FmtAec | Number(001,0) | Não | Formato do autenticador externo de crédito |
| TipAec | Number(001,0) | Não | Tipo do autenticador externo de crédito de clientes |
| DiaAec | Number(004,0) | Sim | Quantidade de dias de validade da autenticação realizada para análise crédito |
| SitAec | String(001) | Não | Situação do autenticador externo de crédito |
| CodReg | Number(004,0) | Sim | Código da Regra |
| ObrCvc | String(001) | Sim | Indicativo se obriga confirmação de venda das consultas realizadas |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodAec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
