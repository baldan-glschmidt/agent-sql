# E047LMN

## Descrição

Tabelas - Naturezas de Gasto - Ligação Natureza de Gasto x Motivo

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodNtg | Number(004,0) | Não | Código da natureza de gasto |
| CodMot | Number(006,0) | Não | Código do motivo |
| SitReg | String(001) | Não | Situação do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração do registro |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodNtg
- CodMot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E047LMN_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

