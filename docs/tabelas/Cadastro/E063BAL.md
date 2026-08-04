# E063BAL

## Descrição

Tabelas - Cadastros - Balança de pesagem.

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodBal | Number(004,0) | Não | Código da Balança |
| CodExt | String(100) | Sim | Código da balança no sistema externo ao ERP |
| DesBal | String(100) | Não | Descrição da Balança de Pesagem |
| SitBal | String(001) | Não | Situação da Balança de Pesagem |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodBal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
