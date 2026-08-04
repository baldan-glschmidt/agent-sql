# E001LTE

## Descrição

Tabelas - Transações - Transação por Tipo de Empresa

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| TipEmp | Number(002,0) | Não | Tipo de empresa |
| CodEdc | String(003) | Não | Espécie de documento para fins fiscais |
| TnsPin | String(005) | Sim | Código da transação para produtos em operação interna |
| TnsPit | String(005) | Sim | Código da transação para produtos em operação interestadual |
| TnsPet | String(005) | Sim | Código da transação para produtos em operação para exterior |
| TnsSin | String(005) | Sim | Código da transação para serviços em operação interna |
| TnsSit | String(005) | Sim | Código da transação para serviços em operação interestadual |
| TnsSet | String(005) | Sim | Código da transação para serviços em operação para exterior |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- TipEmp
- CodEdc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
