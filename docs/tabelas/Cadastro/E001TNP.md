# E001TNP

## Descrição

Tabelas - Transações - Ligação Transação x Natureza de Operação

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodTns | String(005) | Não | Código da transação |
| ComNop | String(005) | Não | Natureza de operação correspondente (CFOP) |
| SigUfs | String(002) | Não | Sigla do estado do cliente |
| SitReg | String(001) | Não | Situação do registro |
| EntSai | String(001) | Não | Indicativo de entrada/saída |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração do registro |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodTns
- ComNop
- SigUfs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E001TNP_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

